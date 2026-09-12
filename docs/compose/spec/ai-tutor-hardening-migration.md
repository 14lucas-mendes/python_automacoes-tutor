---
feature: ai-tutor-hardening-migration
status: delivered
updated: 2026-09-12
branch: migrate/ai-tutor-hardening
commits: 7e4a891..c460270
---

# Migração do estudo para o núcleo ai-tutor endurecido

## Report

**O que foi construído** — O estudo `python_automacoes-tutor`, criado sobre a versão de 03/09 da skill, agora satisfaz o contrato endurecido de 12/09. Os 105 IDs de entidade (7 tópicos, 61 evidências, 9 sessões, 14 lições, 3 pontos fracos, 4 projetos, 7 fontes) passaram ao prefixo canônico com sublinhado, e a renomeação cobriu listas de IDs, referências e prosa (`next_step`, `checkpoint`, além da abreviação `lesson-02`). As lições trocaram `topic_ids` pelo `topic_id` único, os pontos fracos passaram a `entered_at` com `open` → `active`, e cada evidência ganhou `reference: {type, id}` preservando o `location` original.

Os dois registries que o contrato tornou canônicos existem agora: `.ai-tutor/cards.json` (vazio, sem cards no estudo) e `.ai-tutor/sources.json` com as 7 fontes que antes moravam dentro de `state.json`, já com `author_or_institution`, `authority_reason`, `topic_ids`, `lesson_ids` e `publication_date`. Todo JSON canônico carrega `revision`, e `state.json` avançou de 79 para 80 como token CAS. Nenhum dado foi perdido: as contagens de entidades são idênticas às de antes, e a narrativa de 21 KB do `session-log.md` foi preservada byte a byte, com o `curriculum.md` recebendo apenas a troca de IDs.

A skill endurecida está instalada no MiMo Desktop em `~/.config/mimocode/skills/ai-tutor/`, com os três `locales/*.json` que a página de Plugins lê.

**Verificação** — do `skill_root` (`ai-tutor-base`), com todas as varreduras próprias do estudo:

| Comando | Resultado |
| --- | --- |
| `py -m scripts.validate_study <study>` | PASS — `STUDY VALIDATION: PASS` |
| `py scripts/validate_study.py <study>` | PASS — mesmo resultado pelo entrypoint direto |
| `py scripts/validate_skill.py <skill_root>` | PASS — `VALIDATION: PASS` |
| `py -m pytest tests -q` (skill_root) | PASS — 82 passed, 5 subtests |
| `py <installed>/scripts/validate_skill.py <installed>` | PASS |
| `py -m pytest tests -q` (installed) | PASS — 82 passed, 5 subtests |
| migração `--dry-run` sobre candidato em staging | PASS — valida limpo, nada escrito |
| replay do script corrigido sobre cópia limpa do baseline | PASS — 10 arquivos com SHA256 idêntico ao entregue |
| varredura de tokens legados no estudo | 0 tokens legados vivos |

A revisão independente não encontrou achado crítico: nenhum ID deixado para trás, nenhuma referência quebrada, nenhum campo perdido, nenhuma prosa corrompida. Os três achados de robustez e as duas divergências pré-existentes estão registrados em D4/D5 e no journey log.

**Journey log**

- O primeiro corte da migração validou limpo nos dois entrypoints do `validate_study` e ainda assim deixou 9 IDs obsoletos: `topics[].prerequisite_topic_ids` e as menções em prosa não eram conferidos por nenhum validador. Renomear só os campos que o validador olha é uma armadilha real — a verificação tem de varrer a árvore inteira.
- `validate_study` retorna cedo quando falta `cards.json` ou `sources.json`, então a contagem inicial de 258 não conformidades só apareceu depois de montar um candidato em staging com os arquivos vazios no lugar.
- A abreviação `lesson-02` na prosa não era chave do mapa de 105 IDs e escapou da primeira passagem; passou a exigir uma segunda regra de prefixo, com guarda para não reescrever o nome de arquivo `session-log.md`.
- `scripts/projections.py` reescreve `flashcards.md` e `session-log.md` incondicionalmente, apesar de `references/architecture.md` descrever a escrita como seletiva. Num estudo com log escrito à mão, rodar o comando documentado destrói a narrativa — por isso o estudo carrega um aviso no topo do arquivo.
- Divergências pré-existentes que a migração não introduziu e não corrigiu: o `session-log.md` marca a sessão de debugging como "em andamento" enquanto o estado canônico diz `completed`; e as fontes FastAPI apontam para tópicos cujo escopo foi renomeado na migração curricular (SQL relacional, HTTP e APIs REST).

## [S1] Problem

O estudo em `python_automacoes-tutor` foi criado sobre o commit `425c088` da skill `ai-tutor` (v2, 03/09/2026). Em 12/09/2026 a skill recebeu um endurecimento que ainda não está commitado no repositório `ai-tutor-base`: os registries `.ai-tutor/cards.json` e `.ai-tutor/sources.json` passam a ser canônicos, todos os IDs ganham prefixo obrigatório, todo JSON canônico carrega `revision`, a atualização concorrente usa lock/CAS (`scripts/state_io.py`) e as projeções Markdown passam a ser geradas de forma explícita (`scripts/projections.py`).

Rodando o validador oficial endurecido contra o estudo, o resultado é **258 não conformidades** (medido com `scripts/validate_study.py`, já contando `cards.json`/`sources.json` vazios e `revision` em `media-index.json` para que o validador não aborte na primeira checagem):

| Qtde | Categoria |
| --- | --- |
| 108 | ID de entidade sem o prefixo canônico (`topic-…` em vez de `topic_…`) |
| 61 | `evidence.reference` sem `{type, id}` — usa `session_response` / `git_commit`, tipos não suportados |
| 52 | Campo obrigatório ausente (14 lições sem `topic_id`, 7 fontes × 5 campos, 3 pontos fracos sem `entered_at`) |
| 36 | `author_or_institution`/`authority_reason`/`lesson_ids`/`topic_ids` nas fontes, `invalid weak point status: open`, cascatas de lição concluída |
| 1 | `study-config.accessibility` é string; o contrato exige lista ou objeto |

Além dessas, o estudo não possui os arquivos canônicos `.ai-tutor/cards.json` e `.ai-tutor/sources.json`, não tem `revision` em `media-index.json`, não tem `.ai-tutor/migrations/`, e guarda as 7 fontes dentro de `state.json` (campo `sources`), onde o contrato endurecido não as valida nem as reconhece.

O efeito prático é que o estudo está fora do contrato: a skill atualizada não consegue validar, retomar ou atualizar a sessão com segurança, e nenhum workflow novo (cards, fontes, projeções) encontra os dados no lugar esperado.

## [S2] Design

### D1 — Layout canônico após a migração

```text
<study_root>/
├── .ai-tutor/
│   ├── study-config.json     # schema_version 2, accessibility como lista
│   ├── state.json            # schema_version 2, revision ≥ 0, sem a chave `sources`
│   ├── media-index.json      # + revision
│   ├── cards.json            # NOVO — registry canônico de cards (vazio)
│   ├── sources.json          # NOVO — 7 fontes migradas
│   └── migrations/           # NOVO — backup pré-migração + o script desta migração
├── curriculum.md             # projeção, narrativa preservada
├── session-log.md            # projeção, narrativa preservada
├── flashcards.md             # projeção regenerada de cards.json
├── lessons/  media/  projects/
```

`revision` em `cards.json`, `sources.json` e `media-index.json` começa em `0`. `state.json` passa de `79` para `80`: o arquivo foi reescrito e `revision` é o token CAS do contrato, então avançá-la é o que impede um escritor concorrente que ainda espera `79` de sobrescrever a migração.

### D2 — Regra de ID

Formato obrigatório: `^(topic|evidence|session|lesson|weak|project|card|source)_`. Apenas o **separador inicial** muda de `-` para `_`; o restante é preservado para manter datas e slugs legíveis (`session_2026-08-31-diagnostico`, `lesson_03-testes-git`, `evidence_debugging-diagnosis-01`).

O mapeamento é gerado a partir dos IDs realmente presentes em `state.json` (7 tópicos, 61 evidências, 9 sessões, 14 lições, 3 pontos fracos, 4 projetos, 7 fontes). A aplicação tem duas passagens: substituição **exata** dos 105 IDs conhecidos, token-delimitada; e, depois, uma passagem que normaliza **referências parciais** ao mesmo separador (a prosa usava `lesson-02` como abreviação), desativada para nomes de arquivo como `session-log.md`. O `-`→`_` só troca o separador inicial, preservando datas e slugs legíveis (`session_2026-08-31-diagnostico`, `lesson_03-testes-git`). O resultado é verificado por pós-condições sobre os JSON **e** sobre as projeções Markdown, e por uma varredura independente de tokens legados.

### D3 — Renomes de campo por entidade

- **lessons**: `topic_ids` (lista) → `topic_id` (único). Cada uma das 14 lições tem exatamente um tópico, então o mapeamento é sem perda. `title`, `objective`, `prerequisite_lesson_ids`, `required_evidence_types`, `delivery_criteria` e `session_ids` permanecem.
- **weak_points**: `entry_date` → `entered_at` (os valores já são datas ISO); `status: "open"` → `"active"`; `"resolved"` permanece. As categorias existentes (`precision`, `application`, `procedural`) já são válidas.
- **evidences**: `reference` passa a `{type, id}`:
  - `session_response` (57) → `{type: "session", id: <session_id da própria evidência>}`; o `location` original é preservado como chave extra.
  - `git_commit` (4) → `{type: "session", id: <session_id da própria evidência>}`, com a URL do repositório/commit preservada em `location`. O commit aconteceu dentro da sessão; apontar para `project` ou `lesson` atribuiria a evidência à entidade errada.
  - Verificado: nenhuma evidência referencia sessão diferente da sua própria.
- **study-config**: `accessibility: "nenhuma"` → `[]`, com a resposta original preservada em `accessibility_notes`, para não perder a informação de setup.
- **sources** (movidas para `sources.json`): `institution` → `author_or_institution`, `why_authoritative` → `authority_reason`, `linked_topic_ids` → `topic_ids` (com IDs renomeados), `lesson_ids: []` e `publication_date: null` adicionados, `accessed_at` e `source_type` mantidos, `source_id` renomeado para o prefixo `source_`.

### D4 — Política de projeções

`session-log.md` **não é regenerado**: mantém a narrativa escrita à mão (checkpoints, 13 evidências da sessão de debugging, ajuste pedagógico, seção de migração curricular). O validador exige apenas que o arquivo exista; o conteúdo não é conferido. Cópias pré-migração dos 8 arquivos alterados ficam em `.ai-tutor/migrations/pre-hardening/`. `flashcards.md` é regenerado a partir de `cards.json` porque hoje é apenas um stub — não há narrativa a perder. `curriculum.md` mantém a narrativa e recebe só a renomeação de IDs.

`scripts/projections.py` **não** é executado contra `session-log.md`, e isso é uma exceção consciente ao contrato: `sync_projections` reescreve `flashcards.md` **e** `session-log.md` incondicionalmente, então o comando documentado em `references/architecture.md` destruiria a narrativa. O `session-log.md` do estudo carrega um aviso no topo para impedir a execução acidental. Quem quiser o formato mecânico precisa arquivar a narrativa antes.

### D5 — Verificação

Do `skill_root`, com o estudo como argumento:

```text
python -m scripts.validate_study "<study_root>"     # deve imprimir STUDY VALIDATION: PASS
python -m scripts.validate_skill <skill_root>       # pacote da skill íntegro
```

Critério de aceite: `validate_study` retorna `PASS` para `python_automacoes-tutor`, com os 258 erros de [S1] zerados e os arquivos canônicos novos presentes.

Desvios conscientes, registrados porque o revisor os levantou: a migração escreve com `atomic_write` em vez do lock/CAS de `scripts/state_io.py` — é uma operação offline de um único escritor, e o script aplica sua própria atomicidade entre arquivos, restaurando do backup os arquivos já substituídos se qualquer escrita falhar. Ela também não é re-executável: aborta se `cards.json` e `sources.json` já existirem. Verificado por replay que as correções de robustez não mudam a saída: o script corrigido, rodado sobre uma cópia limpa do baseline, produz os 10 arquivos com hash idêntico ao entregue.

### D6 — Instalação no MiMo Desktop

Payload copiado do snapshot endurecido para `~/.config/mimocode/skills/ai-tutor/`: `SKILL.md`, `references/`, `assets/`, `scripts/`, `agents/`, `tests/`. Adicionados `locales/pt-BR.json`, `locales/en-US.json` e `locales/zh-CN.json` com `displayName` e `brief` (metadados de exibição da página de Plugins). O `name` do frontmatter (`ai-tutor`) e a `description` em inglês permanecem intactos. O diretório instalado deve passar `validate_skill.py`.

## [S3] Out of Scope

- Os outros estudos da máquina (`engenharia_ai-tutor`, `ingles-tutor`, `formação-n8n`, `generative-ai-for-beginners`, `formação-Claude-GPT`) — apenas `python_automacoes-tutor` foi nomeado.
- Criar os 13 arquivos de lição ausentes em `lessons/` (14 lições no estado, 1 arquivo): é trabalho de conteúdo, não de formato.
- Commitar o endurecimento no repositório `ai-tutor-base`: o snapshot é usado como está, sem escrever no worktree main daquela skill.
- Popular `cards.json` com cards reais: não existem cards no estudo hoje; o registry entra vazio.
- Reescrever a narrativa de `session-log.md` para o formato mecânico do `projections.py`.

## Tasks

- [x] T1: Preparar workspace (git init, commit de baseline, branch) — aceite: `main` com o estudo intacto em `7e4a891` e branch `migrate/ai-tutor-hardening` ativa (covers: S1)
- [x] T2: Escrever esta spec — aceite: documento presente em `docs/compose/spec/` (covers: S2)
- [x] T3: Migrar o estado canônico — aceite: `validate_state` e `_validate_config` sem erros sobre os payloads migrados; `cards.json`/`sources.json`/`revision` criados; `sources` removido de `state.json` (covers: D1, D2, D3; depends: T1)
- [x] T4: Renomear IDs nas projeções Markdown — aceite: nenhum ID legado com `prefix-` resta em `curriculum.md`, `session-log.md`, `lessons/00-diagnostico-e-ambiente.md` e `.cursor/rules/obsidian-lesson-diary.mdc`; `session-log.md` preserva a narrativa (covers: D2, D4; depends: T3)
- [x] T5: Criar `.ai-tutor/migrations/` com backup pré-migração e o script da migração, e regenerar `flashcards.md` — aceite: backup contém os arquivos originais; `flashcards.md` corresponde à saída de `render_flashcards` (covers: D1, D4; depends: T3)
- [x] T6: Validar com o validador oficial — aceite: `python -m scripts.validate_study "<study_root>"` imprime `STUDY VALIDATION: PASS` (covers: D5; depends: T3, T4, T5)
- [x] T7: Instalar a skill no MiMo Desktop — aceite: `~/.config/mimocode/skills/ai-tutor/` com SKILL.md, references, assets, scripts, agents, tests e os três `locales/*.json`; `validate_skill.py` retorna `PASS` sobre o diretório instalado (covers: D6; depends: T1)
- [x] T8: Revisão independente e relatório final — aceite: revisão separada de conformidade e consistência, achados críticos tratados (covers: S2; depends: T6, T7)
