#!/usr/bin/env python3
"""One-shot migration of this study to the hardened ai-tutor v2 contract.

Applies the 12/09/2026 hardening of the ai-tutor skill:

* canonical ID prefixes (``topic-`` -> ``topic_`` and siblings), applied recursively so
  ID lists (``prerequisite_topic_ids``), ID-bearing prose (``next_step``, ``checkpoint``)
  and references are all rewritten;
* ``lessons[].topic_ids`` -> ``lessons[].topic_id``;
* ``weak_points[].entry_date`` -> ``entered_at`` and ``open`` -> ``active``;
* ``evidences[].reference`` -> ``{type, id}`` with ``location`` preserved;
* ``study-config.accessibility`` -> list;
* canonical ``.ai-tutor/cards.json`` and ``.ai-tutor/sources.json`` registries;
* ``revision`` on every canonical JSON that lacked it, and a CAS bump on ``state.json``.

The pre-migration files are copied to ``.ai-tutor/migrations/pre-hardening/`` and the
migrated payloads are validated on a staging copy before any canonical file is replaced.

Usage:
    python 2026-09-12-migrate-hardened-v2.py --study-root <dir> --skill-root <dir> [--apply]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ID_PREFIXES = ("topic", "evidence", "session", "lesson", "weak", "project", "card", "source")
CONFORMANT_ID = re.compile(r"^(?:" + "|".join(ID_PREFIXES) + r")_[A-Za-z0-9][A-Za-z0-9._-]*$")
SHORTHAND_PREFIX = re.compile(
    r"(?<![A-Za-z0-9_-])(" + "|".join(ID_PREFIXES) + r")-(?![Ll]og\b)"
)
BACKUP_FILES = (
    ".ai-tutor/state.json",
    ".ai-tutor/study-config.json",
    ".ai-tutor/media-index.json",
    "curriculum.md",
    "session-log.md",
    "flashcards.md",
)
MARKDOWN_RENAME_TARGETS = (
    "curriculum.md",
    "session-log.md",
    "lessons/00-diagnostico-e-ambiente.md",
    ".cursor/rules/obsidian-lesson-diary.mdc",
)
PROJECTION_FILES = ("curriculum.md", "session-log.md", "flashcards.md")
WEAK_POINT_STATUSES = {"open": "active", "active": "active", "resolved": "resolved", "archived": "archived"}


class MigrationError(RuntimeError):
    """Raised when the study cannot be migrated safely."""


def hardened_id(value: str) -> str:
    """Return the canonical form of a legacy identifier."""

    for prefix in ID_PREFIXES:
        if value.startswith(f"{prefix}-"):
            return f"{prefix}_{value[len(prefix) + 1:]}"
    return value


def read_json(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise MigrationError(f"{path.name} must contain a JSON object")
    return payload


def build_id_map(state: dict, sources: list) -> dict[str, str]:
    """Collect every legacy ID and its canonical replacement."""

    mapping: dict[str, str] = {}
    for collection, field in (
        ("topics", "topic_id"),
        ("evidences", "evidence_id"),
        ("sessions", "session_id"),
        ("lessons", "lesson_id"),
        ("weak_points", "weak_point_id"),
        ("projects", "project_id"),
    ):
        for item in state.get(collection, []):
            old = item.get(field)
            if isinstance(old, str):
                mapping[old] = hardened_id(old)
    for source in sources:
        old = source.get("source_id")
        if isinstance(old, str):
            mapping[old] = hardened_id(old)

    new_values = list(mapping.values())
    duplicates = sorted({value for value in new_values if new_values.count(value) > 1})
    if duplicates:
        raise MigrationError(f"ID collision after rename: {duplicates}")
    non_conformant = sorted(value for value in new_values if not CONFORMANT_ID.match(value))
    if non_conformant:
        raise MigrationError(f"non-conformant ID after rename: {non_conformant[:5]}")
    return mapping


def rename_tree(node, mapping: dict[str, str]):
    """Rewrite every legacy ID occurrence anywhere in a JSON tree.

    Matching is token-bounded, so filenames such as ``session-log.md`` are untouched.
    After the exact-ID pass, a second pass normalizes partial references such as the
    prose shorthand ``lesson-02`` to the same separator rule.
    """

    if isinstance(node, dict):
        return {key: rename_tree(value, mapping) for key, value in node.items()}
    if isinstance(node, list):
        return [rename_tree(value, mapping) for value in node]
    if isinstance(node, str):
        updated = node
        for old, new in sorted(mapping.items(), key=lambda item: -len(item[0])):
            updated = re.sub(
                rf"(?<![A-Za-z0-9_-]){re.escape(old)}(?![A-Za-z0-9_-])",
                new,
                updated,
            )
        return SHORTHAND_PREFIX.sub(r"\1_", updated)
    return node


def assert_no_legacy(node, mapping: dict[str, str], path: str = "root") -> None:
    """Fail loudly if any legacy identifier survived the rename."""

    if isinstance(node, dict):
        for key, value in node.items():
            assert_no_legacy(value, mapping, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            assert_no_legacy(value, mapping, f"{path}[{index}]")
    elif isinstance(node, str):
        for old in mapping:
            if re.search(rf"(?<![A-Za-z0-9_-]){re.escape(old)}(?![A-Za-z0-9_-])", node):
                raise MigrationError(f"legacy ID survived at {path}: {old}")
        shorthand = SHORTHAND_PREFIX.search(node)
        if shorthand:
            raise MigrationError(
                f"legacy ID prefix survived at {path}: {shorthand.group(0)}"
            )


def migrate_state(state: dict, mapping: dict[str, str]) -> dict:
    """Apply the structural changes, then rewrite every ID in one recursive pass."""

    migrated = {key: value for key, value in state.items() if key != "sources"}

    for lesson in migrated.get("lessons", []):
        topic_ids = lesson.pop("topic_ids", [])
        if len(topic_ids) != 1:
            raise MigrationError(
                f"lesson {lesson['lesson_id']} has {len(topic_ids)} topic_ids; "
                "the contract allows exactly one topic_id"
            )
        lesson["topic_id"] = topic_ids[0]

    for evidence in migrated.get("evidences", []):
        location = (evidence.get("reference") or {}).get("location")
        evidence["reference"] = {"type": "session", "id": evidence["session_id"]}
        if location:
            evidence["reference"]["location"] = location

    for weak_point in migrated.get("weak_points", []):
        if "entry_date" in weak_point:
            weak_point["entered_at"] = weak_point.pop("entry_date")
        status = weak_point.get("status")
        if status not in WEAK_POINT_STATUSES:
            raise MigrationError(f"unsupported weak point status: {status}")
        weak_point["status"] = WEAK_POINT_STATUSES[status]

    revision = migrated.get("revision")
    if isinstance(revision, bool) or not isinstance(revision, int) or revision < 0:
        raise MigrationError(f"state revision must be a non-negative integer: {revision!r}")
    migrated["revision"] = revision + 1

    migrated = rename_tree(migrated, mapping)
    assert_no_legacy(migrated, mapping)
    return migrated


def migrate_sources(sources: list, mapping: dict[str, str], topic_ids: set, lesson_ids: set) -> list:
    migrated = []
    for source in sources:
        migrated.append({
            "source_id": source["source_id"],
            "title": source.get("title", ""),
            "author_or_institution": source.get("institution", ""),
            "url": source.get("url", ""),
            "publication_date": source.get("publication_date"),
            "accessed_at": source.get("accessed_at"),
            "source_type": source.get("source_type", ""),
            "lesson_ids": list(source.get("lesson_ids", [])),
            "topic_ids": list(source.get("linked_topic_ids", [])),
            "authority_reason": source.get("why_authoritative", ""),
        })
    migrated = rename_tree(migrated, mapping)
    assert_no_legacy(migrated, mapping)

    known_topics = {hardened_id(value) for value in topic_ids}
    known_lessons = {hardened_id(value) for value in lesson_ids}
    for source in migrated:
        unknown = [value for value in source["topic_ids"] if value not in known_topics]
        if unknown:
            raise MigrationError(
                f"source {source['source_id']} references unknown topics: {unknown}"
            )
        unknown = [value for value in source["lesson_ids"] if value not in known_lessons]
        if unknown:
            raise MigrationError(
                f"source {source['source_id']} references unknown lessons: {unknown}"
            )
    return migrated


def migrate_config(config: dict) -> dict:
    migrated = dict(config)
    accessibility = migrated.get("accessibility")
    if isinstance(accessibility, str):
        migrated["accessibility_notes"] = accessibility
        migrated["accessibility"] = []
    migrated.setdefault("external_consents", {})
    return migrated


def rename_markdown(path: Path, mapping: dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in sorted(mapping.items(), key=lambda item: -len(item[0])):
        updated = re.sub(
            rf"(?<![A-Za-z0-9_-]){re.escape(old)}(?![A-Za-z0-9_-])",
            new,
            updated,
        )
    updated = SHORTHAND_PREFIX.sub(r"\1_", updated)
    if updated != text:
        path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study-root", required=True, type=Path)
    parser.add_argument("--skill-root", required=True, type=Path)
    parser.add_argument("--apply", action="store_true", help="write the migrated files")
    args = parser.parse_args()

    study_root = args.study_root.resolve()
    sys.path.insert(0, str(args.skill_root.resolve()))
    from scripts.init_study import atomic_write  # noqa: PLC0415
    from scripts.projections import render_flashcards  # noqa: PLC0415
    from scripts.validate_study import validate_study  # noqa: PLC0415

    metadata = study_root / ".ai-tutor"
    if (metadata / "cards.json").exists() and (metadata / "sources.json").exists():
        raise MigrationError("study already migrated: cards.json and sources.json exist")

    state = read_json(metadata / "state.json")
    config = read_json(metadata / "study-config.json")
    media = read_json(metadata / "media-index.json")
    sources = state.get("sources", [])
    if not isinstance(sources, list) or not sources:
        raise MigrationError("state.json has no `sources` array to migrate")

    mapping = build_id_map(state, sources)
    new_state = migrate_state(state, mapping)
    study_id = new_state["study_id"]
    new_config = migrate_config(config)
    new_media = {**media, "revision": media.get("revision", 0)}
    new_sources = {
        "schema_version": 2,
        "study_id": study_id,
        "revision": 0,
        "sources": migrate_sources(
            sources, mapping,
            {topic["topic_id"] for topic in state["topics"]},
            {lesson["lesson_id"] for lesson in state["lessons"]},
        ),
    }
    new_cards = {"schema_version": 2, "study_id": study_id, "revision": 0, "cards": []}
    payloads = {
        "state.json": new_state,
        "study-config.json": new_config,
        "media-index.json": new_media,
        "cards.json": new_cards,
        "sources.json": new_sources,
    }

    # Stage the full candidate and validate it before touching the real study.
    with tempfile.TemporaryDirectory() as temporary:
        candidate = Path(temporary) / "study"
        (candidate / ".ai-tutor").mkdir(parents=True)
        for name, payload in payloads.items():
            (candidate / ".ai-tutor" / name).write_text(
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8", newline="\n",
            )
        for name in PROJECTION_FILES:
            shutil.copy2(study_root / name, candidate / name)
        staging_errors = validate_study(candidate)

    if staging_errors:
        for error in staging_errors:
            print(f"STAGING ERROR: {error}")
        print(f"STAGING: FAIL ({len(staging_errors)} errors) — nothing written")
        return 1

    if not args.apply:
        print(f"DRY RUN OK: {len(mapping)} IDs renamed, {len(new_sources['sources'])} sources migrated")
        print("candidate study validates clean; re-run with --apply to write")
        return 0

    backup = metadata / "migrations" / "pre-hardening"
    backup.mkdir(parents=True, exist_ok=True)
    for relative in BACKUP_FILES:
        source = study_root / relative
        if source.is_file():
            shutil.copy2(source, backup / Path(relative).name)

    for name, payload in payloads.items():
        atomic_write(metadata / name, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    for relative in MARKDOWN_RENAME_TARGETS:
        path = study_root / relative
        if path.is_file():
            changed = rename_markdown(path, mapping)
            print(f"{'updated' if changed else 'unchanged'}: {relative}")

    atomic_write(study_root / "flashcards.md", render_flashcards(new_cards))

    errors = validate_study(study_root)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"STUDY VALIDATION: FAIL ({len(errors)} errors)")
        return 1
    print(f"MIGRATED: {len(mapping)} IDs renamed, backup in {backup}")
    print("STUDY VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
