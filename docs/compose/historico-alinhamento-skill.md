# Histórico de alinhamento com a skill ai-tutor

Este registro saiu do `AGENTS.md` em 2026-10-07, quando a skill passou a ser versionada no git. O detalhe de cada alinhamento, com os hashes, continua no `session-log.md`.

## Até 2026-10-07: alinhamento por hashes

Sem controle de versão na skill instalada, o alinhamento era conferido assim: hash SHA-256 dos contratos e scripts instalados contra o último registro no `session-log.md`, `validate_skill` sobre o pacote instalado e `validate_study` sobre o estado. O resultado e os hashes novos eram registrados no log.

- **Onda de 12/09 (v2 endurecido).** Alinhamento no `session-log.md`; migração descrita em `docs/compose/spec/ai-tutor-hardening-migration.md`.
- **Onda adaptativa de 21–22/09.** Diagnóstico, learner profile, espaçamento e protocolo adaptativo de aula. A atualização do estado foi feita com `scripts.migrate_state` (`_upgrade_v2_support_files`). A skill instalada foi sincronizada com a pasta `E:\Lucas\Documents\Faculdade AI\ai-tutor-base`, que depois deixou de existir.
- **2026-10-06.** Unificação em uma só cópia ativa (`docs/compose/unificar-skill-ai-tutor.ps1`), com backups em `C:\Users\lucka\skill-backups\`.

## A partir de 2026-10-07: alinhamento por commit

A onda adaptativa estava só na pasta instalada; o repositório público `14lucas-mendes/ai-tutor-skill` tinha parado na v2. Ela foi publicada no PR [14lucas-mendes/ai-tutor-skill#1](https://github.com/14lucas-mendes/ai-tutor-skill/pull/1) (merge `19379a9`), e a pasta instalada virou um clone do repositório. O backup da pasta antes da conversão está em `C:\Users\lucka\skill-backups\installed-pre-git-20261007-224824`.

Desde então, o alinhamento registra o commit da skill em uso, e não mais os hashes.
