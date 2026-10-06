# Registro de sessões

<!-- Projeção legível mantida à mão. NÃO execute `python -m scripts.projections` neste
     estudo: o gerador reescreve session-log.md sem condição e substituiria toda esta
     narrativa por um resumo mecânico de 6 linhas por sessão. -->

## `session_2026-10-06-revisao-cond-tempos-01` — concluída em 2026-10-06 (`revision` 173 → 182)

- Cerca de 55 min de 90 pedidos. Modo `assessment` na revisão, prática em bloco (`weak_condicionais-ordem-guarda` ativo).
- Recuperação (`retrieval_first`, não é evidência):
  - `cond-01` **parcial**. O enunciado do café da manhã era ambíguo de novo e a leitura com `and` era válida (falha do material). Na reformulação (lista de compras), escolheu `if` separados, mas acrescentou um `else` para "os dois". No semáforo, chamou de "independentes" situações que se excluem. Volta 07/10.
  - `cond-02` **correto** (a cadeia para no primeiro verdadeiro; o mais restrito vem primeiro). `cond-03` **correto** (`if len(pecas) > 0:`; em 02/10 tinha sido incorreto). `cond-04` **correto**, agora com o porquê. Os três voltam 09/10.
  - `cond-05` **incorreto** de primeira: pela 3ª vez propôs comparar com o CSV original. Depois de duas perguntas direcionais (degrau 3) — o `esperado` do próprio `ordens_json.py` e o contraexemplo `split(",")` com um esperado copiado do JSON —, autocorrigiu: o esperado é escrito à mão, com o formato de saída correto. Volta 07/10. `weak_verificacao-valor-esperado` segue ativo.
- `tempos-01..08` adiados a pedido do aluno; o `tempos-01` foi apresentado e não foi respondido.
- O aluno declarou que não quer informar confiança nos cards. Registrado como preferência em `learner-profile.json`; o tutor parou de pedir.
- README: aula antes da tarefa (definição, analogia do manual na caixa, Markdown e dois exemplos de outros contextos). 1ª versão boa, mas faltavam como rodar, a verificação e o fechamento de um bloco de código. O tutor apontou os critérios (degrau 1) e relatou o teste numa cópia. 2ª versão completa (sha256 `d54a6c63…`). Conferido numa cópia: OS-101 alterada → `Erro de gravação do arquivo!` com o `ordens.json` intacto.
- Evidência: `evidence_lesson02-readme-01`, aplicação **autônoma correta** (`topic_automacao-confiavel`). A seção "Como rodar" reaproveita o relato do tutor, por isso não conta para `weak_caminho-relativo-pasta-trabalho`.
- **Regra 9:** `topic_automacao-confiavel` continua em **80**. Para 100, é preciso repetir o desempenho de 80 em outra sessão e outro contexto, com detecção de limite ou autocorreção.
- **`lesson_02-arquivos-erros` concluída**: entrada inválida tratada, módulos separados e README. Diário no cofre: `AI Tutor - Python automações - lesson-02-arquivos-erros.md`, linkado no MOC. `next_focus` passou a ser `lesson_14-git-fluxo-profissional`.
- Perfil: uma observação (`strategy_outcome`): pergunta direcional ancorada no código do aluno mais um contraexemplo já vivido.
- Pendente: o aluno ainda vai commitar o `README.md` (`?? README.md`).
- Próximo passo: em 07/10, os cards `cond-01`, `cond-05` e `tempos-01..08`. Depois, a `lesson_14` com aula antes de avaliar.

## Unificação da skill `ai-tutor` — 2026-10-06

- Não é sessão de aprendizagem. Nenhum arquivo `.ai-tutor/*.json` foi alterado.
- Decisão do aluno: manter **uma só cópia ativa** da skill. A fonte única é `C:\Users\lucka\.config\mimocode\skills\ai-tutor`. A regra está no `AGENTS.md` e o script, em `docs/compose/unificar-skill-ai-tutor.ps1`. O script foi escrito numa sessão na nuvem (commit `38469cf`) e executado nesta máquina.
- Diagnóstico: além de `~/.claude`, havia cópias em `~/.cursor`, `~/.agents` e `~/.codex`. As de `.claude` e `.agents` eram clones git da versão pública antiga, sem `learning-strategies`, `diagnostic-contract` e `retrieval.py`. As de `.cursor` e `.codex` eram subconjuntos da oficial (48 e 52 arquivos, contra 87). Nenhuma tinha conteúdo mais novo que a oficial.
- Aplicado: as quatro cópias foram movidas para `C:\Users\lucka\skill-backups\{claude,cursor,agents,codex}-ai-tutor-20261006-182622`. No lugar de cada uma ficou uma *junction* para a fonte única. O `SKILL.md` lido pela junction do Claude Code é o mesmo da fonte única. A segunda execução do diagnóstico confirma uma única versão ativa.
- `validate_skill` e `validate_study`: PASS antes e depois.
- Hashes SHA-256 da fonte única em 06/10. Os 17 arquivos restantes do registro de 22/09 continuam iguais. Diferem estes 3, todos com data de modificação 22/09 12:23, a mesma hora da sincronização. A origem mais provável é uma edição feita depois de os hashes terem sido anotados naquele dia. Não foi possível confirmar, porque `ai-tutor-base` não existe mais em `E:\Lucas\Documents\Faculdade AI\`. Esta tabela resolve a pendência de 28/09.

| Arquivo | 22/09 | 06/10 |
|---|---|---|
| `references/state-contract.md` | `a74e0312…` | `2aa3339db77647f6e6e072563d79e98dbe87ebc3e8c866e5c753b9aacfe5aec3` |
| `references/diagnostic-contract.md` | `8d17f429…` | `f25cea3805ec0d56149f8a3479b3202a662ec916804df4db23b6da6bdc6776fb` |
| `scripts/retrieval.py` | `f372cd0b…` | `efb0a722fa82a8e2923f6ed9c39759bafc14361fb22ded0bdde7bbf2b3d0f7ef` |

- Pendente: reiniciar o Claude Code e o Cursor para recarregarem as skills.

## Revisão de roadmap: Segundo Cérebro — 2026-10-05 (`revision` 171 → 172)

- Não é sessão de aprendizagem. Nenhuma evidência, domínio, ponto fraco ou sessão foi alterado.
- Origem: o aluno trouxe o vídeo [Super memória vs. Segundo Cérebro](https://youtu.be/3CBIhTVAGCE) (Vini Lana) e decidiu transformar o próprio segundo cérebro no projeto de portfólio da formação. Ideias aproveitadas: memória fora do agente, memórias versionadas no tempo, busca que traz só o trecho certo e síntese periódica ("sonhar").
- Decisões do aluno: um cofre só (o vault "Projeto Transição de Carreira" virou `C:\Users\lucka\Documents\Segundo Cérebro` e recebeu as notas do antigo cofre "Segundo Cerebro", arquivado em `Segundo Cerebro - arquivado 2026-10-05`); a demo de manutenção vira módulo; interface web local em **React com TypeScript** (Vite), por já ter base de React/Next da Mate Academy e para se alinhar ao mercado; **fluxo Git profissional de dev solo** (`main`/`develop`, feature branches, PR, CI, releases); Selenium mantido no Ciclo 8; captura contínua de cada sessão no cofre.
- Proposta e raciocínio: `docs/compose/spec/segundo-cerebro-roadmap.md` (aprovada).
- `state.json`: `lesson_05` a `lesson_13` com novos títulos, objetivos, critérios e `programming_plan` (âncora, revisita, nova restrição, transferência esperada), IDs mantidos; nova `lesson_14-git-fluxo-profissional` (pré-requisito da `lesson_05`); novo `topic_frontend-react` (domínio 0, conhecimento prévio não conta); novo `project_segundo-cerebro`; `project_automacao-processo-real` e `project_api-llm-servico` arquivados como módulos absorvidos. `lesson_02` só ganhou a ligação ao projeto na `progress_note`, com os critérios inalterados. Gravação via `atomic_update_json` com `expected_revision=171`. `validate_study` PASS antes e depois.
- `curriculum.md`, `AGENTS.md` (seções *Projeto Segundo Cérebro* e *Captura contínua*), skill `segundo-cerebro` e regra do Cursor atualizados à mão. `scripts.projections` não foi executado.
- Observação: a cópia da skill `ai-tutor` em `~/.claude/skills/ai-tutor` está desatualizada em relação a `~/.config/mimocode/skills/ai-tutor` (faltam os contratos de diagnóstico, perfil e estratégias). Esta revisão seguiu a cópia oficial.
- Próximo passo da formação não muda: fechar a `lesson_02-arquivos-erros` (README).

## Calendário oficial — 2026-09-29

- Não é sessão de aprendizagem. O aluno escolheu **2026-08-31** (primeira sessão) como data oficial de início.
- `study-config.json` ganhou `program_start_date`, `program_start_note` e `cycle_calendar` (13 janelas de 21 dias, até 30/05/2027). Gravação feita com `FileLock` + `atomic_write`, porque o arquivo não tem `revision` e o `atomic_update_json` recusa esse caso. `validate_study` PASS.
- `curriculum.md` ganhou a seção *Calendário de referência*. Leitura em 29/09: pelo calendário seria o Ciclo 2, dia 9; o trabalho real está no Ciclo 4, cerca de 6 semanas à frente. A folga veio dos ciclos 1 a 3, fechados com evidência prévia; os ciclos 5 em diante são conteúdo novo.

## `session_2026-10-02-condicionais-01` — retomada e concluída em 2026-10-05

- Retomada com orçamento de **45 min** pedido pelo aluno; prioridade na tarefa independente do `ordens_json.py`. Cards `cond-01..05` e `tempos-03..07` adiados.
- O aluno perguntou se relembrar a aula contaria como ajuda. Resposta: não (pré-requisito, regra 7), desde que o tutor não diga onde mexer no código. Recuperação livre **correta** (verificar antes de gravar, porque gravar não tem volta); nome impreciso: chamou a lista na memória de "arquivo transformado".
- Tarefa independente, 1ª versão: os 4 cenários antigos passaram; `split(',')` **truncou o `ordens.json` (572 → 0 bytes)**, porque o `open(..., "w")` vinha antes do `if`; o aviso saía por `return` sem `print`; o `case _` imprimia `ordens` indefinida (`NameError`). O tutor só apontou os critérios com a tabela dos 6 cenários (degrau 1) e ensinou que `open(..., "w")` apaga na abertura (pré-requisito, lacuna do material).
- 2ª versão: `with open` dentro do `if lista[0] == esperado`, aviso impresso, `case _` com mensagem própria. **6/6 cenários** numa cópia, JSON intacto em todas as falhas.
- Evidências (`topic_automacao-confiavel`):
  - `evidence_ordens-falhas-ordem-02`: aplicação **autônoma correta**, transferida (projeto real).
  - `evidence_ordens-falhas-feynman-01`: Feynman autônomo **parcial** (ordem certa, analogia do bolo; não explicou o `[]`).
  - `evidence_ordens-falhas-feynman-02`: seguimento **correto** (CSV ausente → lista sem dados → gravada sem verificação).
- **Regra 9 / domínio:** `topic_automacao-confiavel` **60 → 80**. Elementos cumpridos: aplicação autônoma transferida que agora cobre transformação, caso vazio, caminhos e tratamento de falhas. A verificação com valor esperado tem origem guiada (01/10). Para 100: repetir em outra sessão e outro contexto com detecção de limite ou autocorreção.
- Refinamentos opcionais: o aviso diz "erro de gravação" quando a falha é da transformação; a conferência olha só a OS-101.
- Perfil: 1 observação (`strategy_outcome`). A lição `lesson_02-arquivos-erros` continua em andamento (falta README), então não há diário no Obsidian.
- Próximo passo: revisar os cards `cond-01..05` e `tempos-03..07` (`retrieval_first`); depois o README.

### Interrupção de 2026-10-02

- Status: **interrompida** a pedido do aluno, depois de cerca de 1h20 (`resumable: true`). Modo `learning`, prática em bloco (aquisição; o interleaving não se aplica).
- Recuperação (`retrieval_first`, não é evidência). Todos os cards voltam em 03/10:
  - `cond-01` **parcial**: usou `or` no lugar de `if/elif` para situações que se excluem. O enunciado era ambíguo.
  - `cond-02` **parcial**: atribuiu a causa ao `=`. O tutor mostrou que `> 9` dá o mesmo resultado.
  - `cond-03` **incorreto**: disse `TypeError` em vez de `IndexError` e trocou o dado em vez de escrever uma guarda.
  - `cond-04` **parcial**: ordem certa, mas sem dizer por que gravar é sem volta.
  - `cond-05` **incorreto**: repetiu a ideia de comparar com o dado original.
- Aula com o passo a passo, agora em **tema escuro** a pedido do aluno. A sensibilidade à luminosidade alta foi registrada em `study-config.json`.
  - O aluno rastreou sem erro as cenas 1, 4 (com `nota = 6`), 6 (com `fila = ["Bia"]`, curto-circuito) e 9 (`case _`).
  - O termo **curinga** foi ensinado (lacuna do material).
- Evidências (`topic_python-fundamentos`):
  - `evidence_condicionais-ordem-feynman-01`: Feynman **guiado e correto**, com analogia própria das gavetas. Guiado porque o tutor tinha dado a causa no card `cond-02`.
  - `evidence_condicionais-ordem-aplicacao-01`: exercício da temperatura, **autônomo e correto**, com fronteiras testadas.
  - `evidence_condicionais-guarda-aplicacao-01`: exercício `primeiro_e_urgente`, **autônomo e correto**. A guarda já estava na primeira versão; o tutor só apontou os critérios que não batiam.
  - Nenhuma conta como transferência, porque as estruturas são próximas dos exemplos.
- **Regra 9:** `weak_condicionais-ordem-guarda` já tem uma aplicação autônoma correta (a guarda). Faltam outra em sessão diferente e uma em contexto novo. `weak_verificacao-valor-esperado` não avançou (`cond-05` incorreto).
- Tarefa independente do `ordens_json.py` **apresentada, mas não iniciada**: o defeito deve avisar e não gravar (esse ponto tem degrau 3, de 01/10), um `case _` para mensagem inesperada, e os cenários antigos mantidos.
- Perfil: 1 observação (`strategy_outcome`).
- Retomada: a tarefa do `ordens_json.py` com 6 cenários de teste; depois Feynman sobre o `[]`; depois os cards `cond` e `tempos`.

## `session_2026-09-29-revisao-json-01` — retomada e concluída em 2026-10-01

- Status: **concluída** em 2026-10-01 às 20:13, a pedido do aluno (transições `in_progress → interrupted → resumed → completed`). A lição `lesson_02-arquivos-erros` continua em andamento.
- Ambiente: Claude Code. A sessão foi conduzida pelo `skill_root` do `AGENTS.md` (`~/.config/mimocode/skills/ai-tutor`); o `~/.claude/skills/ai-tutor` continua sendo a versão pública anterior às ondas.

### Retomada de 2026-10-01

- `card_tempos-01`: **correto** (`retrieval_first`, suporte 0). Deu os dois nomes e o momento de cada erro: sintaxe "o programa nem roda"; exceção no meio da execução, com traceback. Volta em 04/10. Os cards `tempos-03` a `07`, vencidos em 01/10, ficaram para a próxima.
- **Critério 4, verificar a transformação** (guiado, degraus 3 → 4/5): o aluno pediu explicação. O tutor usou a analogia do troco: conferir com a conta feita de cabeça, e não com o papel do caixa.
  - Primeiro, o aluno apontou `ler_ordens_servico` como fonte verdadeira; mas ela é a entrada ainda não transformada.
  - Depois, colou o esperado da OS-101 copiado do `ordens.json`, dizendo que já sabia a estrutura.
  - Com exemplos de valor esperado literal + `==`, escreveu `esperado == ordens[0]` e, **por decisão própria**, um booleano `verificar_item` que condiciona a impressão.
  - O tutor confirmou numa cópia com `split(",")` que a verificação detecta o defeito.
- **Critério 3, falhas** (guiado, degrau 6): o CSV ausente gerava `IndexError` em `ordens[0]` e **sobrescrevia `ordens.json` com `[]`**, porque a transformação rodava antes de conferir a mensagem.
  - O aluno explicou o traceback pela metade: "sem dados" está certo, mas disse que `ordens` era o arquivo JSON, quando é a lista na memória.
  - Uma comparação usava `"Arquivo não existe"` sem o `!`.
  - **Correção após o fechamento, pelo relato do aluno:** o aluno escreveu a versão final **sozinho, por tentativa e erro**, trocando a ordem e testando, depois da pista parcial do tutor (degrau 4: "dois motivos, um na ordem, outro no texto"). Só depois de o código funcionar ele pediu a **outra IA** uma explicação de *por que* funcionou. Por isso, a classificação é degrau 4 do tutor (teto 40), e não degrau 6. A lacuna é de **compreensão**, não de implementação. A versão final (`match`/`case`, sha256 `38f62581…`) só transforma no caso de sucesso. O `ler_ordens.py` passou a tratar o CSV só com cabeçalho.
  - Cinco cenários verificados em cópias: certo, ausente, vazio e só-cabeçalho corretos, com o JSON intacto.
- **Pendente:** com defeito na transformação, nada é impresso e o JSON errado **já foi gravado**, porque a gravação fica dentro de `transformar_ordens_json`, antes da verificação. Também falta a frase Feynman do critério 2.
- Evidências:
  - `evidence_ordens-transformacao-01`: transferência **autônoma correta**, restrita à transformação, ao caso vazio e aos caminhos.
  - `evidence_ordens-verificacao-esperado-01`: guiada, correta.
  - `evidence_ordens-falhas-ordem-01`: guiada, parcial.
- **Regra 9:** `topic_automacao-confiavel` continua em **60**. O elemento do 80 já cumprido é a parte de transformação, aplicada sozinho num contexto novo. O que falta é uma aplicação transferida **inteira** autônoma, porque a verificação e o tratamento de falhas desta tarefa foram guiados.
- Pontos fracos novos, ambos `conceptual` (lacuna do material): `weak_condicionais-ordem-guarda` (pedido explícito do aluno) e `weak_verificacao-valor-esperado`.
- Cards novos `cond-01` a `05` (condicionais, guarda, gravar depois de verificar, valor esperado), com vencimento em 02/10. Fontes novas: `source_python-controlflow` e `source_python-boolean-ops`.
- Perfil: 1 observação (`help_usage`, corrigida para degrau 4).
- Mídias pedidas pelo aluno, geradas localmente e sem envio externo: `media/lesson_01-python-core/notebooklm/` (`media_5fa40819…`, status `verified`).
  - Principal: `local/condicionais-passo-a-passo.html`, com 9 cenas que avançam linha por linha e pedem uma previsão antes de cada avanço.
  - Complementar: `local/roteiro-condicoes.md`, um fluxograma de decisão com texto alternativo.
  - Todos os exemplos foram executados em Python 3.11.15. O `prompts.md` está pronto caso o aluno queira um vídeo do NotebookLM, a ser feito pelo Cursor.
- Próximo passo, uma nova sessão com cinco etapas:
  1. `retrieval_first` nos cards `cond` e `tempos`.
  2. Aula explicativa com o passo a passo.
  3. Exercícios guiados em contextos novos.
  4. Tarefa independente no `ordens_json.py`: o defeito avisa e não grava; acrescentar um `case _`.
  5. Feynman.

### Registro de 2026-09-29
- Revisão (`retrieval_first`, não é evidência): `card_tempos-01` parcial (citou `TypeError`, que é um exemplo, no lugar da categoria exceção; volta em 30/09). `card_tempos-02` e `card_tempos-08` **corretos**, depois de terem sido incorretos em 28/09 (voltam em 06/10).
- Tarefa de transferência (modo `assessment`, sem ajuda sobre o núcleo; o tutor só apontou quais critérios faltavam): ordens de manutenção `src/ordens.csv` → `src/modulo-02/ler_ordens.py` + `ordens_json.py` → `src/ordens.json`.
  - Primeira versão, verificada numa cópia a partir da raiz. Critérios cumpridos por decisão própria: 1 (peças em lista), 2 (`== ""` antes do `split` → `[]`) e 5 (caminhos `src/...` escolhidos sozinho). Critério 3 pela metade (sem o CSV, a saída é só `None`). Critério 4 não cumprido (repetiu a verificação por ida e volta).
  - Segunda versão, em andamento: mensagem para CSV vazio adicionada. Faltam a mensagem para arquivo ausente e o critério 4, que o aluno declarou não saber resolver. O arquivo termina num `if __name__ == "__main__":` sem corpo.
- **Regra 9:** nenhuma evidência foi registrada ainda, porque a tarefa está aberta. Até agora estão cumpridos, de forma autônoma, a transformação, o caso de borda e a escolha de caminhos; faltam a verificação da transformação (critério 4), a mensagem de falha e a frase Feynman sobre o critério 2. O domínio continua 60.
- Perfil: 1 observação (`autonomous_attempt`, parcial, suporte 0).
- Retomada: rodar a versão atual, pedir a frase do critério 2, fechar o critério 3 e oferecer ao aluno a escolha para o critério 4 (nova tentativa só com o prompt, ou escada de ajuda; o degrau 3 em diante torna só a verificação guiada).

## `session_2026-09-28-git-uso-real-01` — 2026-09-28 (gravada em 29/09)

- Status: concluída (modo `assessment`, ~10 min). A gravação no estado ficou pendente em 28/09 porque o classificador de segurança do ambiente falhou; foi feita em 29/09 com o horário original.
- O aluno versionou e publicou sozinho o trabalho do dia em `formacao-python`: `git add .`, `git status` (conferência por iniciativa própria), `git commit -m "feat: add função que lê um csv e transforma em json"` → `28bc5e0` e `git push` → `0a00c47..28bc5e0 main -> main`. O tutor conferiu as refs: `main` e `origin/main` estão em `28bc5e0`.
- Evidência: `evidence_git-uso-real-formacao-python-01`, aplicação **autônoma, transferida e correta** em repositório real. O único suporte foi o tutor ter nomeado as etapas add, commit e push (degrau 1).
- `topic_workflow-profissional` continua em 80. `weak_git-formas-exatas-comandos` **segue ativo**: a evidência não exercitou comandos de configuração e leitura de remoto (`remote add`, `remote -v`, `log` com flags), que são a causa do ponto fraco, e o remoto tinha sido configurado pelo tutor. Não criar tarefa sintética; aguardar o uso real.

## `session_2026-09-28-csv-json-01` — 2026-09-28

- Status: concluída. A lição `lesson_02-arquivos-erros` continua em andamento.
- Ambiente: primeira sessão no Claude Code (desktop). O `/ai-tutor` do Claude Code carrega `C:\Users\lucka\.claude\skills\ai-tutor`, um clone da versão pública (`14lucas-mendes/ai-tutor-skill`, HEAD `5102ec9`), **anterior** às ondas endurecida e adaptativa (sem `delegation-contract`, `learning-strategies`, `learner_profile`, `retrieval`). A sessão foi conduzida pelo `skill_root` do `AGENTS.md` (`~/.config/mimocode/skills/ai-tutor`, `validate_skill` PASS). Os hashes de `references/state-contract.md` (`2aa3339d…`) e `scripts/retrieval.py` (`efb0a722…`) instalados diferem do registro de 22/09; os arquivos são de 22/09 12:23 e o `ai-tutor-base` não existe mais nesse caminho para conferir.
- Duração: 16:16 às 18:33 (~2h17 de relógio; orçamento 90 min). O excedente inclui tempo de resposta entre turnos.
- Objetivo: recuperar os cards vencidos de `lesson_03` e transformar os clientes do CSV em JSON válido com telefones em lista, verificado por leitura de volta.
- **Recuperação** (`retrieval_first`, 8 tentativas em `retrieval_attempts`; não é evidência): corretos 03 (apoio 2: exemplo visível), 04, 05, 06, 07; parcial 01 ("sintaxe e estrutura de código", sem exceções); incorretos 02 (achou que a falta de traceback prova que o código rodou) e 08 (achou que o traceback aponta sempre o defeito). Confirma `weak_error-model-tempo-deteccao`. Os cards 01, 02 e 08 voltam em 29/09 e os demais em 01/10. Explicações dadas com a analogia da receita e do alarme de fumaça, mais execução real.
- **Pré-requisitos ensinados** (regra 7, não rebaixam): `json.dump`/`json.load` (`ensure_ascii`, `indent`, modo `"w"` sobrescreve) com dois exemplos de falhas de equipamento; `split` com separador; **pasta de trabalho** (caminho relativo resolvido a partir do terminal, `os.getcwd`), com demonstração do mesmo script rodado de duas pastas.
- Projeto: `E:/Lucas/Documents/formação_python/src/tarefas/modulos/leitor_json.py` → `src/clientes.json`. Trajetória: `[].append(...)` (devolve `None`), depois `split(",")`, depois `split()` e por fim `split(" e ")`. Caminho `../../dados.csv` falhava em silêncio a partir da raiz; o aluno diagnosticou pela `mensagem` e escolheu sozinho `src/dados.csv` e `src/clientes.json` após a explicação. Criou por conta própria a verificação por ida e volta (`pacote == dados`) no lugar do `len` sugerido.
- Evidência: `evidence_csv-json-transformacao-01`, aplicação **guiada** correta. Sobre o núcleo houve o degrau 2 (o que há em `pacote`) e o degrau 3 (a `/` aparece no resultado do `split`?), com teto de 40 nesta tentativa.
- Evidência: `evidence_csv-json-limite-verificacao-01`, Feynman **autônoma correta** (suporte 0). O aluno disse que `pacote == dados` daria `True` mesmo com o `split` errado, porque prova que o arquivo guardou fielmente os dados, não que a transformação esteja certa. É detecção de limite da própria verificação.
- **Regra 9, prestação de contas:** `topic_automacao-confiavel` continua em **60**. A Feynman e a aplicação autônomas do 60 já estavam cumpridas desde 21 e 22/09. Hoje soma-se mais uma Feynman autônoma, que não muda o número. Para **80**, falta uma aplicação **autônoma com transferência**. Para fechar a lição falta o README (o JSON está entregue em prática guiada).
- Ponto fraco novo: `weak_caminho-relativo-pasta-trabalho` (`conceptual`), por lacuna do material. Houve recorrência em 23/09 (import) e hoje (arquivo).
- Perfil: 1 observação (`help_usage`, degrau 3).
- Próximo passo: o aluno faz o commit e o push de `leitor_json.py` e `clientes.json` em `formacao-python` sem comandos fornecidos (uso real para `weak_git-formas-exatas-comandos`); cards 01, 02 e 08 em 29/09; README; depois tarefa autônoma de transferência.
- Repositório do aluno: `formação_python` ganhou Git nesta data (commit inicial `0a00c47`, feito pelo tutor a pedido do aluno) e remoto privado `14lucas-mendes/formacao-python`. Como foi feito pelo tutor, **não é evidência**.
- Sem diário no Obsidian: a lição não foi concluída.

## `session_2026-09-23-csv-modulos-01` — retomada e fechamento em 2026-09-24

- Status: concluida; a licao `lesson_02-arquivos-erros` continua em andamento.
- Objetivo: separar o leitor CSV e o script de apresentacao e verificar que importar o modulo nao executa o fluxo.
- Retomada: a pergunta Feynman aberta sobre `csv.reader` versus `DictReader` ja havia sido respondida corretamente e de forma autonoma em 23/09 (`evidence_csv-feynman-reader-dictreader-01`).
- Pratica guiada: o aluno implementou em `E:/Lucas/Documents/formacao_python/src/tarefas/modulos/leitor_csv.py` a contagem de campos com `csv.reader`, reposicionamento com `seek(0)`, leitura de dicionarios com `DictReader` e mensagens distintas para arquivo ausente, vazio e incompatibilidade.
- Verificacao observada: cinco cenarios — CSV completo (cabecalho + cinco registros, sucesso); caminho incorreto (arquivo nao existe); apenas cabecalho (sucesso com lista vazia); arquivo vazio (`Arquivo csv vazio`); colunas incompatíveis (mensagem de incompatibilidade).
- `mostrar_clientes.py` importa `ler_clientes`, apresenta o retorno com `print` no fluxo principal e usa `if __name__ == "__main__"`. Execucao com CSV valido mostrou os dados esperados. `python -c "import mostrar_clientes"` no diretorio `src/tarefas/modulos` encerrou sem saida. A tentativa inicial na raiz nao encontrou o modulo; repetir no diretorio correto funcionou.
- A implementacao recebeu pistas e feedback do tutor; registrar como pratica guiada, sem criar evidencia autonoma nem elevar dominio. `topic_automacao-confiavel` permanece em 60.
- Proximo passo: nova sessao para transformar os registros em JSON; depois README. Para dominio 80 ainda falta aplicacao autonoma em contexto de transferencia.
- Arquivos do projeto alterados fora do estudo: `leitor_csv.py` e `mostrar_clientes.py`.


## `session_2026-09-22-csv-entrada-invalida-01` — fechamento em 2026-09-22

- Status: concluída, encerrada a pedido do aluno **depois** de concluir a tarefa de entrada inválida.
- Duração: 14:32 às 16:13 (~101 min de relógio; orçamento declarado 60 min). Excedente em parte tempo de resposta do aluno entre turnos.
- Lição: `lesson_02-arquivos-erros` — Ciclo 4. Permanece **em andamento**.
- Objetivo: fazer o leitor reconhecer e informar entrada inválida (valores da linha ≠ cabeçalho) sem entregar dado corrompido, com verificação por execução.
- Modo: `learning`; núcleo cognitivo: decidir o contrato nesse caso e implementar a detecção sem devolver o dado torto. Suporte sobre o núcleo: **0** (apenas o prompt).
- Cenário: `E:/Lucas/Documents/formação_python/src/exercicios/exercicios_03.py`.
- Sonda (`retrieval_csv-deslocamento-01`): descreveu corretamente o deslocamento e o `None` final no `DictReader`. Outcome `correct`, support 0. Não é evidência de domínio.
- Observação de material: o pacote torto ainda saía com `msg_success` — quem chama recebia dado corrompido ao lado de “Sucesso”.
- Evidência: `evidence_csv-entrada-invalida-01` — aplicação **autônoma correta**. Duas passadas: `next(csv.reader(arquivo), None)` para o cabeçalho (StopIteration tratado), comparação `len(linha)` × cabeçalho em `csv.reader` (contagem real, antes do `DictReader` mascarar com `None`), retorno `PACOTE_ERROR` + `msg_incompatible` no primeiro desvio, `seek(0)` e `DictReader` só no caminho válido. Cinco casos verificados por execução: CSV válido com mapeamento correto, arquivo ausente, só cabeçalho, arquivo vazio e o caso-alvo (quatro títulos e três valores) devolvendo a mensagem de incompatibilidade. O `next(..., None)` do vazio é mecanismo ensinado em 18/09 e não ganha crédito independente; o núcleo (contagem + contrato de erro) é do aluno.
- Refinamentos opcionais registrados sem rebaixar: mensagem sem número da linha/contadores; `PACOTE_ERROR` com listas mutáveis compartilhadas; linha em branco classificada como incompatível.
- **Domínio de `topic_automacao-confiavel`: 60.** Regra 9 — Feynman autônoma: `evidence_csv-justificativa-02` (21/09); aplicação autônoma independente: `evidence_csv-entrada-invalida-01` (hoje). Para 80 falta transferência a contexto novo. Para fechar a lição: módulos separados, JSON e README.
- `weak_csv-return-flow`: **resolvido** (2/2 autônomas corretas em sessões diferentes: `evidence_csv-duas-vias-03` e `evidence_csv-entrada-invalida-01`).
- Perfil: 1 observação factual (`autonomous_attempt`, result `correct`, support 0). Nenhuma inferência (sinal isolado).
- Pergunta de Feynman de fechamento **ficou sem resposta**: por que a contagem usou `csv.reader` e não `DictReader`. Levar para a próxima sessão.
- `next_focus`: `lesson_02-arquivos-erros`. Próximo passo: Feynman aberta + módulos separados; depois JSON e README. Opcional: `/review` dos 8 cards de `lesson_03-testes-git` vencidos desde 2026-09-13.
- Sem diário no Obsidian: a lição não foi concluída.

## Revisão do contrato AI Tutor — onda adaptativa de 21–22/09, aplicada em 2026-09-22

- Motivo: o aluno informou que a skill `ai-tutor` recebeu uma versão nova e mais completa e pediu alinhamento do estudo ao funcionamento novo.
- Fonte da versão nova: repositório `E:\Lucas\Documents\Faculdade AI\ai-tutor-base` (HEAD `1beabd4`, 2026-09-21, com alterações de trabalho até 22/09). A instalação em `~/.config/mimocode/skills/ai-tutor/` ainda era a onda de 12/09.
- O que a onda nova acrescenta: **diagnóstico** (`/diagnostic`, `references/diagnostic-contract.md`, `state.diagnostics`), **learner profile** (`/profile`, `references/learner-profile-contract.md`, canônico `.ai-tutor/learner-profile.json`), **estratégias** (`references/learning-strategies.md`, `retrieval_attempts`, `spacing_policy`, `practice_strategy` em sessões), **protocolo adaptativo de aula de programação** (`references/programming.md`, fases 60–90 min flexíveis), e scripts novos (`learner_profile`, `practice_strategy`, `representation`, `retrieval`, `spaced_repetition`). Contratos de aprendizagem e delegação mantêm a matriz de domínio; diagnóstico e perfil **não** são evidência.
- **Migração aplicada** (idempotente, oficial): `python -m scripts.migrate_state --study-root <study_root>` a partir de `ai-tutor-base` → `changed: true`, `valid: true`, `warnings: []`. Efeito:
  - criado `.ai-tutor/learner-profile.json` (vazio, `revision` 0, summary em `unknown`);
  - `state.json` ganhou `diagnostics: []` e `retrieval_attempts: []` (revision permaneceu **119**; nenhuma sessão, evidência, tópico ou lição foi criada/alterada/reclassificada);
  - `study-config.json` ganhou `spacing_policy: { mode: "fixed", target_horizon_days: null }` (compatível com a escada 1/3/7/16/35/60 já em uso).
- **Skill instalada sincronizada** com o conteúdo de `ai-tutor-base` (payload `SKILL.md`, `references/`, `assets/`, `scripts/`, `agents/`, `tests/`, `README.md`), preservando os três `locales/*.json` do MiMo Desktop.
- Verificação de hoje (2026-09-22):
  - `python -m scripts.validate_study "<study_root>"` → **STUDY VALIDATION: PASS** (com a skill nova, que exige `learner-profile.json`);
  - `python -m scripts.validate_skill "<skill_root>"` sobre `ai-tutor-base` e sobre a instalação → **VALIDATION: PASS** nos dois;
  - os seis JSONs canônicos em `schema_version: 2` e `study_id` coerente.
- **Conclusão:** o estudo opera sobre a onda adaptativa. Nenhum domínio, evidência, lição ou sessão foi alterado. Restam itens de prática da conferência anterior (cards de `lesson_03-testes-git` vencidos desde 13/09; 12 lições sem arquivo em `lessons/`), não de migração.
- **Operação (mesma data):** `AGENTS.md` ganhou o § *Operação com a skill `/ai-tutor` (onda adaptativa)* — retomar sessão, uma pergunta por vez, protocolo de `programming.md`, `retrieval_first`, observação de perfil no fechamento, interleaving só com gate do `practice_strategy`, validação após cada virada, `spacing_policy` fixa. Espelhos `.cursor/rules/ai-tutor-only.mdc` e `pedagogia-progressiva.mdc` sincronizados (arquivos canônicos completos; regra 10: diagnóstico e perfil não são nota).
- Hashes registrados (SHA-256, skill instalada em `~/.config/mimocode/skills/ai-tutor/`, espelho de `ai-tutor-base`):

| Arquivo da skill | SHA-256 |
|---|---|
| `SKILL.md` | `97c690e46f31dd1b8001fe9cc38b05ca1702c459ff2998810fac3b34da9efe5d` |
| `references/architecture.md` | `ae74bfa4a7951f1e80c318769b57330c60b32809e4c8a9b88150fc66bcad97d6` |
| `references/learning-contract.md` | `e3c6e689db1d4ba7ede5ff61e9728d0932ab57e1ac6c5c38a11eb67680c691f2` |
| `references/state-contract.md` | `a74e0312256960584a554411cea8e34c4043926b8fcc018658bcbeefd510b3f6` |
| `references/delegation-contract.md` | `cdaaf4390e0965fac3d3a6d86e104bbc9572e30307e9f885b92eb2ee38cadd58` |
| `references/output-contract.md` | `becc886c1602beefe89eac58ebc8c57e10b31073b2d60b24cd53a6fd4f3bb42d` |
| `references/diagnostic-contract.md` | `8d17f429041d3e8c6c186dbc2b269c5ed5e658113eef284ea3d85ed1fe4b241b` |
| `references/learner-profile-contract.md` | `76a9555fb1b5d2c481d33d73d03fb5b73e3be49a110fc48313d56a4b1b5f350e` |
| `references/learning-strategies.md` | `bdb34fe3127a7eb5dbb64a63786e89526a540c12b97059a0d31ddc5f0ac853d3` |
| `references/programming.md` | `0d5010b626a4d9a49b10adeb8cbcb700e420e1bebabb8a630851d1bc8a33087b` |
| `references/workflows/session.md` | `328f97d2ec5dd431441bd3ba598ee81420646c3550c5d2eefaea007e45c875a4` |
| `references/workflows/diagnostic.md` | `d992d9d82a529d3a5808393a46243508693b7cc13314d148ed066177d399c52c` |
| `references/workflows/profile.md` | `1c3d4027e94f2a5187a3e163d4438531edd6452834231c5e7dc4aac552390468` |
| `scripts/validate_study.py` | `0f9fe13868fddda311f73a94ed455d2d76ebaadc6cb7c85d6906b9b83c65c420` |
| `scripts/migrate_state.py` | `b93f50c60743a46b04de079281a85d9bca8c1117f4ed660fa8dda72731cc305f` |
| `scripts/learner_profile.py` | `80dedf07ca190e69abb0a50390f1f7ffa9fe85f3b190fd731fd44ea60caab99b` |
| `scripts/practice_strategy.py` | `fedc302b01d66a3efd233019173e669c7844d5fd626ca66c678f85d29a65c12d` |
| `scripts/retrieval.py` | `f372cd0b801a1f1301fcb1b226b9207bfe57a868b1e40edd959df7e53456f557` |
| `scripts/spaced_repetition.py` | `f1ad87ac518397c740232e3f9fd54891cfd7ad4f64ea84de12be57ad629e8dcc` |
| `scripts/representation.py` | `cc44bc8b38b2cb7e9ace5df6aede1706b83ce01a2a3b8358d16427bfcc27f481` |

## Mídia — NotebookLM no Cursor, 2026-09-18

- Não é sessão de aprendizagem. A sessão `session_2026-09-18-arquivos-modulo-01` permanece concluída.
- Pacote `media_eefbf673-6430-4d3c-a314-7f66db7b70f8` (`lesson_02-arquivos-erros`) passou de `prepared` para `generated`.
- Notebook observado: [Guia de Referência: Módulos, Listas e Manipulação de CSV](https://notebook.google.com/notebook/9971b3fb-74e1-43a2-9bae-47f62803b788). Fontes inseridas por texto copiado: `source-pack.md` e `prompts.md`. Estúdio observado: `Python Flashcards`, `Python Quiz`, `Python Mapa` e o guia de estudo. Áudio pedido e ainda em geração no painel (`Volte em alguns minutos`). Conteúdo **não verificado** contra as fontes (`verified: false`).
- Decisão: Xiaomi Mi Modem Desktop continua sem NotebookLM; a conexão externa fica neste Cursor. Gravada em `AGENTS.md` e `.cursor/rules/sem-geracao-externa.mdc`.
- Nada disto é evidência. A tarefa da lição 2 segue aberta.

## Revisão do contrato AI Tutor — onda de 12/09 (v2 endurecido), confirmada em 2026-09-20

- Motivo da conferência: o aluno informou que a skill `ai-tutor` recebeu uma versão nova e pediu que o estudo fosse atualizado ao funcionamento novo.
- O registro anterior de alinhamento era de **03/09** ("Revisão do contrato AI Tutor (`revision` 14)"), que guardava o hash do `learning-contract.md` como `80f51c29431d603f61f43d7afad5b5865819c7cb42b79966ad3e288cb1f40218`.
- O que mudou na skill: onda de **11–12/09/2026**. Em 11/09, `architecture.md` (novo) e `output-contract.md`. Em 12/09, `learning-contract.md`, `state-contract.md` e todos os scripts (`init_study`, `projections`, `validate_study`, `create_learning_pack`, `migrate_state`, `state_io`, `validate_skill`). O hash atual do `learning-contract.md` é `9f69322f119eafe686e60b3d4278d8c9b88f074b90face80753c642e18d66c0e`, ou seja, o registro de 03/09 ficou para trás.
- **Como o estudo absorveu a onda:** pela migração de endurecimento de 12/09 — `docs/compose/spec/ai-tutor-hardening-migration.md` com `status: delivered`, commits `7e4a891..c460270` na branch `migrate/ai-tutor-hardening`, backup pré-migração em `.ai-tutor/migrations/pre-hardening/`, revisão independente sem achado crítico e 82 testes da skill passando na época.
- Verificação de hoje (2026-09-20):
  - `python -m scripts.validate_study "<study_root>"` → **PASS**, com o estado em `revision` 113.
  - `python -m scripts.validate_skill "<skill_root>"` sobre o pacote instalado → **PASS**.
  - Os cinco JSONs canônicos (`state`, `study-config`, `cards`, `sources`, `media-index`) em `schema_version: 2`.
- **Conclusão: nenhuma migração de dados era necessária.** O estudo já opera sobre o contrato endurecido desde 12/09. Nenhum domínio, evidência, lição ou sessão foi criado, alterado ou reclassificado por esta conferência.
- Itens remanescentes da onda, registrados para não se perderem:
  - **Fontes com tópico desatualizado** (apontado no journey log da migração): corrigido nesta conferência. `source_fastapi-tutorial` e `source_fastapi-testing` saíram de `topic_apis-backend` (que hoje é SQL relacional) e foram para `topic_agentes-ferramentas` + `lesson_07-fastapi-dados` (ciclo 7). `source_openai-agents-quickstart` e `-tools` ficaram sem competência corrente (`topic_ids` e `lesson_ids` vazios): agentes e LLMs estão no backlog pós-transição, `project_agente-operacional`. `sources.json` avançou para `revision` 3.
  - **Lições sem arquivo de material:** 12 de 14 lições do estado não têm arquivo em `lessons/`. Item deliberadamente fora de escopo da migração de 12/09 (trabalho de conteúdo, não de formato). Entra lição por lição, quando cada uma abrir.
  - **Repetição espaçada pendente:** os 8 cards canônicos de `lesson_03-testes-git` vencem desde 13/09 e nenhuma revisão rodou. Prática pendente, não migração.
  - Divergência pré-existente "session-log em andamento × state completed" — corrigida em 12/09, confirmada hoje.
- Hashes registrados para detectar a próxima deriva (SHA-256, skill instalada em `~/.config/mimocode/skills/ai-tutor/`):

| Arquivo da skill | SHA-256 |
|---|---|
| `SKILL.md` | `b9da8b358df2bd01bce828185e5c6c8247f133df6673af8eebc5511c6e1ae931` |
| `references/architecture.md` | `6781ef9fbe0fd20ab4afb6cdc0343bed298f028d50907cebaae6cf9d2e404724` |
| `references/learning-contract.md` | `9f69322f119eafe686e60b3d4278d8c9b88f074b90face80753c642e18d66c0e` |
| `references/state-contract.md` | `cccab4723fd83cce4e0c56b2662311fdcbc4f4029958ae600e7bb9d18ede90c5` |
| `references/delegation-contract.md` | `cdaaf4390e0965fac3d3a6d86e104bbc9572e30307e9f885b92eb2ee38cadd58` |
| `references/output-contract.md` | `5cb50ec37f9682f024786daf4f2926d9f87944fdff15b32a03a4a52a5e43ae45` |
| `references/workflows/session.md` | `77e09b6f858460737e62a78edefb374b1d627c4b60b815e203f93604bd5e0b79` |
| `references/media-providers.md` | `da026dff7509a7bbbc847973f40ddf192acb5cd936caedabc252dea48ee227b2` |
| `scripts/validate_study.py` | `63196802ca9327aee6e13d16e502d16bdd1ebeb3db6084cb7e1f9c8fecf85662` |
| `scripts/migrate_state.py` | `b817c7601b5af5619405d827d571faa14aeb0964accca255ef7bd83ec5726546` |
| `scripts/init_study.py` | `2bf04d0bd4120118df2af4d58f60807d44572ecab354981f7568a3e14acf786d` |
| `scripts/projections.py` | `2d402b9e2d277b4210a51a7bca0a1982da094b323a8b026ff23af98bc578410a` |
| `scripts/state_io.py` | `8f87d4134bf1687406fff3132f22f032e6aee1fc56776aeb0336187c678a0d7b` |
| `scripts/create_learning_pack.py` | `51a2be49c77804c52601137f2e158fabbc5bde2ed5ce517d758aa084ca3c0e56` |
| `scripts/validate_skill.py` | `17f8f06abeafe0fb72d54d9668a42c932a954786ff18047fb7d4fb8cc87dc241` |

## `session_2026-09-21-csv-contrato-01` — fechamento em 2026-09-21

- Status: concluída, encerrada a pedido do aluno, **sem iniciar a tarefa 2**. Acima do orçamento: 79 minutos de 60 planejados (19:38 às 20:57), o excedente consumido pela discussão de avaliação e pela correção da regra 9.
- Duração planejada: 60 minutos (sessão aberta às 19:38).
- Lição: `lesson_02-arquivos-erros` — Ciclo 4. Permanece **em andamento**.
- Objetivo: reconstruir com as próprias palavras a justificativa do contrato de retorno das duas vias, com os valores literais de cada desfecho, e tratar entrada inválida com verificação por execução.
- Modo: `assessment`; núcleo cognitivo: justificar autonomamente o contrato de retorno e decidir o tratamento de entrada inválida a partir do próprio experimento da sessão anterior.
- Cenário: `E:/Lucas/Documents/formação_python/src/exercicios/exercicios_03.py` e `src/dados.csv` — o arquivo ficou com quatro títulos no cabeçalho e três valores por linha, estado do experimento de 20/09 que nunca foi restaurado.
- Evidência: `evidence_csv-justificativa-01` — Feynman **autônoma parcial**. Mecanismo de chave correto, mas afirmou que o `DictReader` "não desloca o conteúdo" quando o cabeçalho ganha coluna sem valor correspondente, contradito pelo próprio print colado (a chave `sobrenome` recebeu o e-mail e `telefone` saiu `None`). A razão de segurança não foi formulada.
- Evidência: `evidence_csv-justificativa-02` — Feynman **autônoma correta**: a metade posicional que ficou sem resposta em 20/09. `csv.reader` devolve listas cruas, a coluna extra aparece no cabeçalho, as linhas de dados permanecem iguais e na ordem do arquivo, e nada quebra na tela — confirmado por execução própria, `exited with code=0`. **Esta evidência cumpre a metade Feynman do requisito de domínio 60 do tópico.**
- Evidência: `evidence_csv-justificativa-03` — Feynman **autônoma parcial**: executou três desfechos e colou as saídas reais, mas respondeu em texto descritivo e unificou "só cabeçalho" com "arquivo vazio". Forma branda do padrão do `weak_python-test-literal-lista`.
- Devolutiva: o erro material foi explicado começando simples (regra 8), com o print do próprio aluno como exemplo e a analogia da ficha com quatro campos impressos para três informações ditadas — as informações entram na ordem dos campos, tudo depois do campo vago cai na casa errada e o programa não reclama.
- Evidência: `evidence_csv-justificativa-04` — Feynman **correta e guiada** (degrau 3 da escada). Razão de segurança formulada: a posição é endereço, a chave é rótulo; sem a chave não dá para saber se `linha[2]` ainda representa o dado procurado; e "chamar pelo nome amarra o programa ao significado da coluna, não só ao lugar dela na linha".
- Evidência: `evidence_csv-justificativa-05` — Feynman **correta e guiada** (degrau 4). Os quatro desfechos com execução real dos quatro, incluindo o arquivo de 0 byte (`None []`), com a causa correta: sem primeira linha, `fieldnames` devolve `None`. O erro material da rodada anterior (tratar os dois casos como equivalentes) está resolvido.
- **Objeção do aluno (2026-09-21) — aceita em parte.** O aluno contestou o desfecho da tarefa 1 pedindo avanço do domínio de 40 para 60, argumentando que parte da tarefa foi autônoma e que as partes guiadas não invalidam o conjunto. O tutor reconheceu a imprecisão: a evidência `-02` já havia cumprido a metade Feynman do 60 e a devolutiva **não declarou isso**, dando a entender que nada tinha contado.
- O número não subiu porque o 60 exige **as duas** metades — explicação Feynman autônoma **e** aplicação autônoma independente. A segunda não existe: as aplicações do tópico são todas parciais, e entrada inválida, módulos separados e JSON seguem sem execução. Rigidez sobre os itens guiados não foi o motivo; eles não são o obstáculo.
- **Regra 9 gravada em `AGENTS.md`**: prestação de contas do domínio — declarar qual elemento do nível está cumprido e qual falta, em vez de tratar o tópico como zerado; a calibragem legítima está na forma, nunca em contar conteúdo fornecido pelo tutor como trabalho autônomo. O espelho `.cursor/rules/pedagogia-progressiva.mdc` estava parado em 12/09 (sem as regras 6, 7 e 8) e foi sincronizado com as regras 6 a 9.
- Nota de progresso gravada no `topic_automacao-confiavel` no estado canônico, dizendo explicitamente qual metade do 60 está cumprida.
- Domínio de `topic_automacao-confiavel`: **mantido em 40**.
- `next_focus`: `lesson_02-arquivos-erros`. Próximo passo: a tarefa 2 (entrada inválida tratada), candidata direta à aplicação autônoma independente que falta para o 60.
- Checkpoint: encerrada sem iniciar a tarefa 2. Sem toque nesta sessão: `weak_csv-return-flow` (segue com 1 de 2 evidências autônomas), `weak_git-formas-exatas-comandos` e `weak_error-model-tempo-deteccao` (1 de 2 explicações). Os 8 cards de `lesson_03-testes-git` seguem vencidos desde 2026-09-13 — sugerida a abertura da próxima sessão por `/review`.

## `session_2026-09-20-arquivos-duas-vias-01` — fechamento em 2026-09-20

- Status: concluída, encerrada a pedido do aluno, **sem fechar a lição**.
- Lição: `lesson_02-arquivos-erros` — Ciclo 4. Domingo, dia de projeto e revisão. Permanece **em andamento**.
- Objetivo: fechar o módulo de leitura de CSV nas duas vias — separar o cabeçalho dos registros na via posicional, escrever a via por nome com `DictReader` e justificar o trade-off.
- Modo: `assessment`; núcleo cognitivo: decidir o contrato de retorno e resolver o mesmo problema com duas ferramentas, justificando o que cada uma resolve sozinha e o que custa.
- Achado de partida: a guarda `__main__` havia sido implementada pelo aluno em **18/09 às 20:42**, durante a sessão anterior e depois da última conferência do tutor. O critério 1 (importar sem efeito) estava cumprido — a regressão de quinta, consertada sem o tutor dizer como.
- Evidência: `evidence_csv-duas-vias-01` — aplicação **autônoma parcial**, via posicional. Cabeçalho separado com `result[0]` e `result[1:]`, e a checagem de vazio colocada **antes** de indexar, o que evita `IndexError` em cima do `except FileNotFoundError`. Contrato frágil: quatro desfechos em quatro formatos de três tipos.
- Evidência: `evidence_csv-duas-vias-02` — aplicação **autônoma parcial**, via por nome. `leitor.fieldnames` lido **dentro** do `with`, evitando o `ValueError` de arquivo fechado, e detecção de vazio por `fieldnames is None`, que é a distinção documentada. Contrato paralelo ao da outra via, com os mesmos dois problemas — o que torna a comparação entre as vias válida.
- Achado do tutor, verificado por execução: o sintoma do desempacotamento **depende do dado**, não do código — com 3 colunas levanta `ValueError: too many values to unpack`, com 2 colunas não levanta nada e devolve `titulo='nome'`, `corpo='email'`. O tutor corrigiu a própria demonstração anterior, que usara um arquivo de 2 colunas, e registrou a correção.
- Evidência: `evidence_csv-duas-vias-03` — aplicação **autônoma parcial**, terceira iteração. O retorno passou a ser sempre uma tupla de dois itens e o desempacotamento funciona nos quatro desfechos; o defeito material demonstrado antes está resolvido. Verificações que ficaram: os três ramos devolvem exatamente o mesmo valor (saídas idênticas com os ramos removidos) e a frase "Arquivo vazio" desapareceu de todas as saídas, deixando o contrato implícito.
- Evidência: `evidence_csv-explicacao-01` — Feynman **autônoma parcial**. Acertos: mecanismo das duas vias, escolha do `DictReader`, e um **experimento real** na terceira pergunta — editou o `dados.csv`, inseriu a coluna `sobrenome` e executou, em vez de especular. Erros: atribuiu a segurança a "não modificar a lista original" (razão de outra pergunta, e verdadeira para as duas vias), não percebeu que a falha foi **silenciosa** (`exited with code=0`) e testou uma via só.
- **Correção de material (regra 8).** A devolutiva entregue com tabela e nome de conceito **não foi entendida**, e o aluno pediu reexplicação pela técnica de Feynman, dizendo que impactava diretamente o entendimento dele. O tutor refez a explicação com frase curta e analogia: a chamada de turma (posição × nome), o funcionário preenchendo a ficha na ordem, e o termômetro que mostra 39° quando a medida é 41° — dado errado e silencioso é pior que programa quebrado. Gravado em `AGENTS.md` item 8: **explicar o erro do aluno começando simples**. Efeito no registro: a razão de segurança e a metade posicional passaram a ser conteúdo ensinado, portanto **guiadas**, e precisam de reconstrução própria.
- O experimento do aluno é também a prova de que o critério "**entrada inválida tratada**" segue aberto: a coluna inserida só no cabeçalho deslocou o conteúdo uma posição — o e-mail caiu em `sobrenome`, o telefone caiu em `email` — e a última coluna virou `None`, sem nenhum erro.
- `weak_csv-return-flow`: **1 de 2** evidências autônomas. O fluxo de acumulação e retorno está correto e autônomo; falta a segunda, em outra sessão.
- Domínio de `topic_automacao-confiavel` mantido em **40**. Nenhum requisito de 60 foi fechado: as aplicações são parciais e a explicação tem erro material.
- `next_focus`: `lesson_02-arquivos-erros`. Próximo passo: reescrever a justificativa com as próprias palavras e depois fechar entrada inválida, módulos separados e README.
- Checkpoint: encerrada. Sem toque nesta sessão: `weak_python-test-literal-lista` (reapareceu no pedido dos valores literais) e `weak_git-formas-exatas-comandos`.

## `session_2026-09-18-arquivos-modulo-01` — fechamento em 2026-09-18

- Status: concluída, encerrada **sem concluir a tarefa**, a pedido do aluno.
- Lição: `lesson_02-arquivos-erros` — Ciclo 4. Permanece **em andamento**.
- Objetivo: deixar o leitor de CSV pronto para ser importado por outro programa — sem efeito no import, com os registros separados do cabeçalho e com erro explícito que quem chama consiga distinguir.
- Modo: `assessment`; núcleo cognitivo: decidir o que a função devolve (registros, e não o cabeçalho) e onde o programa começa a rodar.
- Cenário: `E:/Lucas/Documents/formação_python/src/exercicios/exercicios_03.py`.
- **Auditoria de pré-requisitos, pedida pelo aluno.** Já ensinados: a guarda `__name__ == "__main__"` (`lesson_01`, 07/09, evidências `python-core-structure-06/07`), `import`/`from`, `for`/`if`, listas e `append`, `csv.reader`, `try/except` e flag booleana. **Nunca ensinados:** `next()`, fatiar `[1:]`, `pop(0)` e o `csv.DictReader`. A aula veio antes de qualquer avaliação, com execução real e mais de um exemplo por mecanismo.
- Aula entregue, tudo executado: os dois leitores na mesma planilha (listas por posição × dicionários por nome); `fieldnames`; o cabeçalho omitido dos resultados e por que isso resolve o defeito de 17/09; `next()` avançando uma linha por chamada e o custo de chamá-lo duas vezes; a armadilha do `StopIteration` em arquivo vazio e a saída `next(leitor, None)`; fatiar criando lista nova contra `pop(0)` modificando a lista; linhas irregulares (`restval` → `None` na célula faltante, excedente → chave literalmente chamada `None`); e o leitor preso ao arquivo aberto (`ValueError: I/O operation on closed file`, descoberto por erro do próprio tutor ao montar a demonstração).
- **Decisão do aluno (2026-09-18), gravada em `AGENTS.md` item 7:** ensinar um pré-requisito que a regra 1 obriga a ensinar **não** rebaixa a tentativa seguinte a prática guiada. A escada de ajuda mede ajuda sobre o núcleo cognitivo, não conhecimento de documentação convencional. Fundamento no contrato de aprendizagem ("documentação convencional não invalida a autonomia automaticamente") e no degrau 2 da escada (recuperar pré-requisito não aplica teto). Limites registrados: continua guiada quando o tutor entrega o núcleo — critérios, análise, conclusão ou implementação essencial —, e comportamento que a ferramenta ensinada executa sozinha, como o `DictReader` pulando o cabeçalho, não ganha crédito independente naquela tentativa.
- Nada foi implementado nesta sessão: o aluno encerrou antes de escrever o código. **Sem evidência nova**, e a tarefa segue aberta.
- Pacote de mídia local criado para `lesson_02-arquivos-erros` (`media/lesson_02-arquivos-erros/notebooklm/`), artefato `media_eefbf673-6430-4d3c-a314-7f66db7b70f8`, status `prepared`: `source-pack.md`, `prompts.md`, `manifest.json`, `local/cards.json` (10 rascunhos com fonte citada), `local/quiz.json` (8 perguntas, chave de resposta separada, um distrator por confusão registrada), `local/concept-map.mmd`, `local/didactic-image.svg` com alt text em `local/image-brief.md`, `local/audio-script.md` (transcript em 5 blocos) e `local/study_guide.md`.
- Fontes novas em `.ai-tutor/sources.json` (revision 2): `source_python-csv-module`, `source_python-modules`, `source_python-datastructures`, `source_python-builtins` — documentação oficial, consultada em 2026-09-18. Cada trecho do source pack declara explicitamente o que **não** cobre, para nenhuma afirmação ficar sem lastro.
- **Nenhum artefato externo existe.** Nenhuma automação de navegador foi tentada nesta sessão; a decisão de não usar NotebookLM nem Gemini neste desktop segue valendo.
- `next_focus`: `lesson_02-arquivos-erros`. Próximo passo: implementar a leitura **dos dois jeitos** — leitor posicional e leitor por nome — com a guarda `__main__`, os três desfechos distinguíveis (dados, ausente, só cabeçalho) e a justificativa de projeto. O aluno declarou que fará os dois caminhos.
- Checkpoint: encerrada sem conclusão. Sem toque nesta sessão: `weak_python-test-literal-lista`, `weak_error-model-tempo-deteccao` (1 de 2 explicações) e `weak_git-formas-exatas-comandos`.

## `session_2026-09-17-arquivos-csv-01` — fechamento em 2026-09-17

- Status: concluída, encerrada acima do orçamento (72 min de 45 planejados)
- Lição: `lesson_02-arquivos-erros` — Ciclo 4, Arquivos, CSV e JSON. Permanece **em andamento**.
- Objetivo: ler um CSV real com mais de uma linha e devolver todos os registros, provando a leitura pelo retorno completo.
- Modo: `assessment` seguido de prática guiada; núcleo cognitivo: separar leitura de acumulação e devolver a coleção inteira depois da iteração, em vez de devolver o último item lido.
- Cenário: `E:/Lucas/Documents/formação_python/src` — `exercicios/exercicios_03.py` (código de 2026-09-08) e `dados.csv`, que tinha cabeçalho e **um** registro.
- Por que o item ficou pendente desde 08/09: com um registro só, "devolver o último" e "devolver todos" dão o mesmo resultado. A verificação era impossível de observar naquele arquivo.
- Evidência: `evidence_csv-ciclo4-01` — aplicação **autônoma parcial**. Ampliou o CSV para cinco registros, previu a forma do retorno e executou a leitura: `exited with code=0`, seis listas na saída (cabeçalho + 5 registros). O retorno completo ficou provado. Falhas materiais: afirmou que a função devolve `FileNotFoundError` quando ela imprime uma mensagem e devolve `None` implicitamente; justificou a adequação pelo mecanismo (`usar try-except`) e não pela consequência para quem chama. Refinamento: descreveu a estrutura em vez de escrever os valores literais pedidos, repetindo o padrão do `weak_python-test-literal-lista` agora na verificação.
- Aula entregue com execução real: `print` não é retorno (canais diferentes — a mensagem vai para a tela, o valor sai para quem chama); `.strip()` para os espaços que o `csv.reader` não limpa; e `csv.reader` já entrega uma lista nova por linha, o que torna o `.copy()` do código redundante (ensinado assim em sessão anterior — lacuna do material, não do aluno).
- Evidência: `evidence_csv-ciclo4-02` — aplicação **correta e guiada** (a forma do reprojeto veio do tutor no ciclo de erro). O ponto central foi cumprido: a função passou a **devolver** em vez de imprimir, com três execuções reais (arquivo com dados, arquivo ausente, arquivo vazio). Quatro lacunas verificadas por execução: a justificativa sobre como quem chama distingue os casos não foi escrita; a limpeza dos espaços foi feita reescrevendo o próprio `dados.csv` em vez de tratar na leitura (resolve arquivo próprio, não arquivo de terceiro); a detecção de vazio **conta o cabeçalho como dado**, então um CSV só com cabeçalho devolve `[['nome','email','telefone']]` como se tivesse conteúdo, com zero registros reais; e o `print` solto no fim do arquivo dispara no import, impedindo usá-lo como módulo — regressão da guarda `__main__` de `lesson_01`, e o critério "módulos separados" desta lição continua aberto.
- Observação de ambiente: no terminal do aluno a mensagem com acento saiu como `Arquivo n?o encontrado` — é a página de código do console, não o código. As demonstrações da aula usaram texto sem acento por isso.
- Domínio de `topic_automacao-confiavel`: 0 → **20** na primeira tentativa (tentativa autônoma parcial) e → **40** no fechamento (aplicação parcial com ajuda direcional). `status: in_progress`.
- Ponto fraco `weak_csv-return-flow` segue **ativo**, com progresso registrado: a verificação com arquivo real de várias linhas, pendente desde 08/09, foi feita. Falta a **produção autônoma** da acumulação para satisfazer a saída do ponto.
- `next_focus`: `lesson_02-arquivos-erros`, aberto com "entrada inválida tratada", "módulos separados" e "README" pendentes.
- Checkpoint: encerrada. Sem toque nesta sessão: `weak_python-test-literal-lista` (reapareceu em forma de descrição), `weak_error-model-tempo-deteccao` (1 de 2 explicações) e `weak_git-formas-exatas-comandos`.

## `session_2026-09-17-git-preflight` — fechamento em 2026-09-17

- Status: concluída
- Duração planejada: 60 minutos. A janela real de relógio passou disso (aberta 13:20, encerrada no fim do dia), mas o trabalho da sessão foram dois turnos: a reconstrução e a correção.
- Lição: `lesson_04-descoberta-processo` — Ciclo 3, Git e GitHub. **Concluída** nesta sessão.
- Objetivo: reconstruir, sem comandos fornecidos, o preflight completo de um repositório Git real e a configuração exata de `origin` antes de publicar.
- Modo: `assessment`; núcleo cognitivo: decidir a ordem e a função de cada verificação antes de publicar, distinguindo repositório local, histórico e remoto.
- Cenário: `C:/Users/lucka/Documents/projects/sandbox-historico`, remoto `https://github.com/14lucas-mendes/sandbox-testelab`.
- Evidência: `evidence_git-preflight-01` — aplicação **autônoma parcial**. Ordem correta (raiz → branch → working tree → remoto → referências remotas), `git ls-remote origin` colocado **depois** de garantir o remoto configurado, `-u` explicado como upstream, publicação verificada sem sobrescrever nada. Duas falhas materiais de forma exata: `git remote edit origin <URL>` (subcomando inexistente — `error: unknown subcommand`) e `git log -1 --one-line` (flag inexistente — `fatal: unrecognized argument`). O item de histórico foi escrito e não executado.
- Aula do ciclo de erro, com execução real e não descrição: a família `git remote` (`add` cria, `set-url` corrige a URL de um remoto existente, `remove` apaga, `-v` lê) e a flag `--oneline`; diagrama das quatro camadas mostrando que `git status` é a única verificação que atravessa área de trabalho, índice e remoto.
- Evidência: `evidence_git-preflight-02` — aplicação **correta e guiada** (a forma exata veio do tutor, então confirma o mecanismo e não conta como autônoma). `git remote add origin <URL>` escrito corretamente de primeira; **previsão própria**, feita antes de executar, de que o `git status` deixaria de mostrar o vínculo com o upstream — e a saída real confirmou a ausência da linha `Your branch is up to date with 'origin/master'`, que voltou depois do `push -u` como `## master...origin/master`. Autocorreção em linha do erro de digitação `git remote - v`.
- Refinamento registrado, sem rebaixar: o plano prometia `git log --oneline origin/master..HEAD` ("o que ainda não subiu") e a execução usou `git log --oneline origin/master` (histórico do lado remoto). O `..` foi explicado nesta sessão como conteúdo novo, portanto fora de avaliação.
- O `git log` final imprimiu o critério da lição ao vivo: `4d7357f alteracoes` ao lado de `d41cc1f Adiciona media() com guarda...` e `699de67 ... para desconsiderar o arquivo debug.log dos meus commits`.
- Ponto fraco aberto: `weak_git-formas-exatas-comandos` (`precision`) — a forma exata falhou duas vezes (2026-09-14 e 2026-09-17) e só ficou correta com o comando fornecido.
- **Regra nova do aluno (2026-09-17), gravada em `AGENTS.md`:** não exigir contexto novo sintético — repositório ou pasta criada só para a avaliação — como condição de fechamento de lição; o uso real em repositórios que já existem é contexto de transferência válido e preferível. Contexto sintético segue permitido como prática, nunca como exigência. Se o que falta é apenas a forma exata de um comando, o tutor ensina, registra `precision` e segue. O ponto fraco foi reescopado para ser observado no uso real.
- Motivo do fechamento: a entrega estava cumprida (repositório organizado, histórico legível, push para GitHub verificado) e os tipos exigidos de evidência já existiam no tópico com trabalho real — `feynman` autônomo correto (`evidence_git-historico-04`), aplicação autônoma correta (`evidence_git-historico-03`, `-05`) e **transferência autônoma real** (`evidence_diagnostico-transfer-01`, `evidence_git-transfer-real-01`). A exigência de um repositório novo era aplicação redundante da matriz de domínio pelo tutor, não requisito do contrato — a objeção do aluno está correta.
- Mantido com honestidade: o que falhou nesta sessão **não** era transferência, era forma exata de comando. A lição fecha; o ponto fraco permanece ativo, porque uma forma que falhou duas vezes não vira domínio por decisão de fechamento.
- Domínio de `topic_workflow-profissional` mantido em **80**; `retention` em `medium` (tentativa parcial não avança nem recua a retenção).
- `next_focus`: `lesson_02-arquivos-erros` — Ciclo 4, Arquivos, CSV e JSON.
- Checkpoint: encerrada. Sem toque nesta sessão: `weak_python-test-literal-lista`, `weak_error-model-tempo-deteccao` (1 de 2 explicações) e `weak_csv-return-flow`, cuja execução com CSV real é justamente o material do Ciclo 4.

## `session_2026-09-14-git-transferencia-01` — fechamento em 2026-09-15

- Status: concluída
- Duração planejada: 90 minutos
- Lição: `lesson_04-descoberta-processo` — Git e GitHub para trabalho profissional. A lição permanece **em andamento** porque a reconstrução autônoma do preflight ainda precisa incluir todas as verificações e a forma exata de `git remote add`.
- Objetivo: transferir o fluxo Git para um repositório real, verificando o estado local, o histórico legível e o remoto sem sobrescrever mudanças alheias.
- Modo: `assessment`; núcleo cognitivo: escolher uma sequência segura de verificação e publicação, distinguindo estado local, histórico e remoto.
- Cenário real: `C:/Users/lucka/Documents/projects/sandbox-historico`, branch `master`, working tree limpa, último commit `699de67` (`git log -1 --oneline`), nenhum remoto inicialmente.
- Execução: foi criado o remoto vazio `https://github.com/14lucas-mendes/sandbox-testelab.git`; `origin` foi configurado; `git ls-remote origin` não retornou refs; `git push -u origin master` publicou a branch; `git status -sb` terminou em `## master...origin/master`, sem `[ahead]` ou `[behind]`.
- Evidência: `evidence_git-transfer-real-01` — aplicação autônoma **correta com transferência**: executou `git rev-parse --show-toplevel`, `git branch`, `git status`, `git remote -v`, `git log -1 --oneline` e `git ls-remote origin` para inspecionar o repositório real antes do envio.
- Evidência: `evidence_git-transfer-real-02` — aplicação **correta guiada**: corrigiu o remoto, publicou `master` com `git push -u origin master` e verificou o upstream com `git status -sb`; os comandos de correção/publicação foram fornecidos após a dificuldade com a sintaxe de link.
- Evidência: `evidence_git-transfer-real-03` — Feynman autônomo **parcial**: explicou branch rastreada, remoto e push, mas omitiu branch/histórico/working tree na sequência final e não escreveu o formato completo `git remote add origin <URL>`.
- Feedback: a saída capturada pelo estudante mostrou o remoto correto e o push bem-sucedido; uma tentativa de verificação pelo ambiente do Codex foi bloqueada por `detected dubious ownership`, sem alteração global de segurança.
- Próximo passo: reconstruir em uma nova sessão, sem comandos fornecidos, o preflight completo (raiz, branch, working tree, histórico, remoto e refs) e a configuração exata de `origin` antes de publicar.

## `session_2026-09-13-git-historico`

- Status: concluída
- Duração planejada: 45 minutos
- Lição: `lesson_04-descoberta-processo` — Ciclo 3, Git e GitHub. Permanece **em andamento**.
- Objetivo: montar um histórico Git legível — ler o estado do repositório antes de commitar, decidir o que entra em cada commit e escrever a mensagem que explica o porquê.
- Modo: `learning` seguido de aplicação autônoma. Pela regra nova do `AGENTS.md`, `git status`, `git diff`, staging seletivo e mensagem de commit nunca haviam sido ensinados nesta formação, então a aula explicativa veio antes de qualquer avaliação.
- Cenário: `C:/Users/lucka/Documents/projects/sandbox-historico`, fora do estudo — commit inicial `4d7357f` com mensagem pobre (`alteracoes`), `registros.py` modificado e `debug.log` não rastreado.
- Aula entregue: analogia da foto e do álbum, diagrama das três áreas e dois exemplos executados de verdade (`log`/`status`/`diff`, e a diferença entre `diff` e `diff --staged`). Também ensinado o *pager* do Git, que apareceu na colagem do estudante (`q` para sair, `git --no-pager` para evitar).
- Evidência: `evidence_git-historico-01` — explicação autônoma **parcial**: leu as duas seções do `status` corretamente (modificado fora do preparo × não rastreado), mas descreveu o `git diff` pelo formato da saída, sem nomear a comparação.
- Evidência: `evidence_git-historico-02` — explicação **correta e guiada**: após pergunta direcional, afirmou que o `git diff` compara árvore de trabalho × índice, e tirou a consequência prática. Refinamento aplicado: o índice não é um commit.
- Evidência: `evidence_git-historico-03` — aplicação autônoma **correta**: preparou só `registros.py` (sem `git add .`), verificou com `git diff --staged`, commitou com a mensagem de porquê `d41cc1f` e justificou recusar o `debug.log`.
- Evidência: `evidence_git-historico-04` — explicação autônoma **correta** do `.gitignore` como registro da decisão; o refinamento de que o próprio `.gitignore` precisa ser commitado foi apresentado depois.
- Evidência: `evidence_git-historico-05` — aplicação autônoma **correta**: criou o `.gitignore`, confirmou que o `debug.log` saiu do `status`, commitou em commit separado (`699de67`) e terminou com *working tree clean*. Verificado fora: o arquivo continua no disco e `git check-ignore` confirma a regra.
- O `git log` final mostra o contraste que é o critério da lição: `alteracoes` ao lado de duas mensagens de porquê.
- Refinamentos opcionais, sem rebaixar a classificação: o prefixo `fix:` é convenção de correção de bug e não foi ensinado nesta formação (para esta mudança seria manutenção), o estilo diverge entre os dois commits e há erros de digitação em texto lido por humanos.
- Domínio de `topic_workflow-profissional` mantido em **80**. Subir para 100 exigiria detecção de limite ou autocorreção demonstrada, que não ocorreu.
- Próximo passo: transferir o fluxo para um repositório real (por exemplo o do próprio estudo) e, quando aplicável, remoto no GitHub. Fechar `lesson_04` exige evidência de **transferência**.

## `session_2026-09-12-debugging-02`

- Status: concluída. A linha dizia "em andamento" por desatualização do diário; `.ai-tutor/state.json` já registrava `completed` com `ended_at`.
- Duração planejada: 60 minutos (inicialmente 90; ajustada a pedido do estudante antes do início da tarefa)
- Lição: `lesson_03-testes-git` — Ciclo 2, debugging sistemático.
- Objetivo: diagnosticar autonomamente uma falha nova, separando sintoma, hipótese e verificação, e explicar sem apoio a diferença entre `NameError` e `TypeError` causado por `None`.
- Modo: `assessment`; núcleo cognitivo: separar sintoma, hipótese e teste de verificação sem pular para a correção, e classificar o defeito entre nome inexistente, valor ausente (`None`) e tipo incompatível na operação.
- Herdado da sessão anterior: `evidence_debugging-diagnosis-11` (Feynman parcial), `diagnosis-12` (prática guiada) e `diagnosis-13` (transferência parcial — chamou `None + 1` de concatenação).
- Material de estudo: `lessons/03-testes-git.md`; fontes registradas `source_python-errors-exceptions` e `source_python-traceback`.
- Evidência: `evidence_debugging-diagnosis-14` — explicação autônoma **parcial**: ordem de leitura do traceback e identificação dos frames de chamada corretas; executou os dois casos no terminal (`TypeError` no código original, `SyntaxError` na substituição que ele próprio propôs). Não nomeou o tipo da exceção na primeira resposta e tratou o `TypeError` como "sintaxe errada".
- Correção pedagógica (a pedido do estudante): a sessão abriu com pergunta gerativa sobre o modelo de dois tempos do Python (análise do código vs execução), que **nunca foi ensinado** nesta formação. A pergunta "por que `SyntaxError` não tem traceback" foi **retirada da avaliação** e a lacuna virou ponto fraco conceitual.
- Regras duráveis gravadas: `AGENTS.md` na raiz do estudo e espelho em `.cursor/rules/pedagogia-progressiva.mdc` — aula explicativa antes de avaliar, nunca assumir termo não estudado, conteúdo não ensinado não vira nota baixa, mais de um exemplo por conceito, concretizar antes de abstrair.
- Ponto fraco aberto: `weak_error-model-tempo-deteccao` (conceitual) — momento de detecção de cada tipo de erro.
- Evidência: `evidence_debugging-diagnosis-15` — explicação autônoma **correta com transferência**: previu que, num arquivo com `SyntaxError` e `TypeError` ao mesmo tempo, só a mensagem de `SyntaxError` aparece; verificou por conta própria trocando a ordem dos `prints` e reexecutando.
- Evidência: `evidence_debugging-diagnosis-16` — aplicação autônoma **parcial** em contexto novo (programa de manutenção com retorno implícito `None`): achou a causa real fora da linha apontada pelo traceback e propôs correção adequada, mas descreveu o valor recebido como `str + float` quando a mensagem indicava `NoneType`, e não apresentou a etapa de verificação.
- Evidência: `evidence_debugging-diagnosis-17` — explicação autônoma **correta**: `media` vale `None` no programa com defeito, confirmado pela própria mensagem de erro e pela linha apontada. Refinamento de redação: `None` é um valor, não ausência de inicialização.
- Evidência: `evidence_debugging-diagnosis-18` — aplicação autônoma **correta com transferência**: `return media` em `tempo_medio` + f-string em `relatorio`; execução real no VS Code com `Tempo medio: 60.0 min` e `exited with code=0`. Saída `60.0` em vez de `60` é refinamento opcional.
- Evidência: `evidence_debugging-diagnosis-19` — explicação Feynman autônoma **correta** do alvo da lição: função que termina sem `return` devolve `None` ao chamador, a variável do outro escopo recebe esse `None`, e a operação incompatível (concatenação ou soma) gera `TypeError`.
- Lição `lesson_03-testes-git`: **concluída** — hipótese registrada, debugging registrado e correção verificada por execução. `next_focus` passa a `lesson_04-descoberta-processo` (Ciclo 3, Git e GitHub).
- Diário gravado no vault Obsidian: `20 - Áreas/Sistema de Estudos/AI Tutor - Python automações - lesson-03-testes-git.md`, com o link adicionado ao `MOC - Sistema de Estudos`.
- Ponto fraco `weak_error-model-tempo-deteccao` segue **ativo**: tem 1 das 2 explicações autônomas exigidas, e a segunda precisa ocorrer em sessão diferente.
- Checkpoint: sessão encerrada. Ficaram sem toque nesta sessão `weak_csv-return-flow` (execução com CSV real ainda pendente) e `weak_python-test-literal-lista`.

## `session_2026-09-10-debugging-01`

- Status: concluída (encerrada ao atingir o limite de 60 minutos). A linha de status anterior dizia "em andamento" por desatualização do diário; `.ai-tutor/state.json` já registrava `completed` com `ended_at`.
- Duração planejada: 60 minutos
- Lição: `lesson_03-testes-git` — Ciclo 2, debugging sistemático.
- Objetivo: diagnosticar uma falha Python por observação, hipótese e verificação da correção.
- Modo: `assessment`; núcleo cognitivo: separar sintoma, hipótese e teste de verificação sem pular diretamente para uma alteração de código.
- Checkpoint: diagnóstico inicial parcial. Identificou o uso de variável sem atribuição, mas confundiu o tipo `NameError` com a variável `quantidade` indicada pela mensagem.
- Evidência: `evidence_debugging-diagnosis-01` — explicação autônoma parcial do sintoma; falta usar a linha indicada para localizar o uso da variável.
- Evidência: `evidence_debugging-diagnosis-02` — diagnóstico autônomo parcial. Identificou corretamente a divergência entre `quantidade` e `qtd`; foi corrigida a ideia de que um nome inexistente vira `None`.
- Evidência: `evidence_debugging-diagnosis-03` — aplicação autônoma correta: alterou `qtd` para `quantidade` e previu corretamente o resultado `30`.
- Evidência: `evidence_debugging-diagnosis-04` — aplicação autônoma correta: identificou que `desconto` recebe o retorno implícito `None` quando `preco` é menor que 100, causando o `TypeError` na subtração.
- Evidência: `evidence_debugging-diagnosis-05` — aplicação autônoma correta: garantiu retorno numérico e calculou `45` para a regra escolhida. Refinamento: retornar `5` abaixo de 100 cria uma nova regra de negócio; uma correção proporcional deve preservá-la ou mudá-la explicitamente.
- Evidência: `evidence_debugging-diagnosis-06` — aplicação autônoma parcial. A intenção de não conceder desconto abaixo de 100 está correta, mas retornar o próprio preço produz `50 - 50 = 0`; falta retornar o valor que representa ausência de desconto.
- Evidência: `evidence_debugging-diagnosis-07` — prática guiada correta: identificou `0` como ausência de desconto após uma pista algébrica.
- Evidência: `evidence_debugging-diagnosis-08` — prática guiada correta: implementou os retornos `10` e `0`, prevendo corretamente `90` para 100 e `50` para 50.
- Evidência: `evidence_debugging-diagnosis-09` — aplicação autônoma parcial: identificou o retorno implícito `None`, sua causa e a necessidade de outro caminho em `classificar_falhas`; falta definir a string retornada nesse caminho.
- Evidência: `evidence_debugging-diagnosis-10` — prática guiada correta: garantiu retorno de string em todos os caminhos e produziu `Status: sem falhas registradas`.
- Evidência: `evidence_debugging-diagnosis-11` — explicação Feynman autônoma parcial: distinguiu nome inexistente de operação inválida, mas falta explicitar que, no `TypeError`, a variável existe e contém `None`, incompatível com a subtração.
- Evidência: `evidence_debugging-diagnosis-12` — prática guiada correta: explicitou que `desconto` existe, mas contém `None`; a distinção ainda precisa ser reexplicada sem estrutura fornecida.
- Evidência: `evidence_debugging-diagnosis-13` — aplicação autônoma parcial em novo contexto: identificou `None` e a necessidade de retorno padrão, mas chamou `None + 1` de concatenação; trata-se de soma entre tipos incompatíveis.
- Ajuste pedagógico: o exemplo anterior mostrou somente a mensagem de erro e ficou abstrato. A partir deste ponto, os exercícios trarão código completo, resultado observado e uma pergunta objetiva.
- Próximo passo: revisar a diferença entre concatenação de strings e soma numérica ao diagnosticar `None + 1`.

## Migração curricular — 2026-09-09

- Formação reposicionada como transição de carreira de 9 meses, em 13 ciclos de 21 dias, para Automação e Integração de Sistemas com Python.
- Preservado: todas as 48 evidências, 8 sessões, competências com domínio 80, diário, pontos fracos e IDs canônicos existentes.
- Reposicionado: `lesson_02-arquivos-erros` passa ao Ciclo 4; suas tentativas anteriores permanecem válidas, sem conclusão fictícia.
- Preservado e reposicionado: `project_api-llm-servico` agora representa o Cliente de API pelo terminal no Ciclo 6.
- Projeto principal: `project_automacao-processo-real` passa a representar o Sistema de Automação de Manutenção — Demo, com dados fictícios ou anonimizados.
- Fora do núcleo: agentes, LLMs, FastAPI, Docker, cloud, MCP, RAG, n8n, frontend e stacks correlatas foram movidos para backlog pós-transição.
- Próximo foco: `lesson_03-testes-git`, Ciclo 2 — debugging sistemático. Nenhuma aula foi iniciada nesta migração.

## `session_2026-09-08-arquivos-erros-02`

- Status: concluída
- Lição: `lesson_02-arquivos-erros`
- Objetivo: executar a função corrigida com um CSV real e verificar que devolve todas as linhas.
- Modo: `assessment`; núcleo cognitivo: verificar a acumulação de linhas por meio de uma entrada real e distinguir código correto de resultado comprovado.
- Checkpoint: sessão encerrada a pedido do estudante. A acumulação foi corrigida como prática guiada; a execução com CSV real permanece pendente.
- Evidência: `evidence_python-core-csv-read-errors-07` — prática guiada correta; `result` é iniciado antes do laço, cada linha é adicionada e o retorno ocorre após a iteração.
- Próximo passo: na próxima sessão, criar um CSV com mais de uma linha, chamar `ler_clientes` e mostrar o retorno completo.
- Encerramento: transição `in_progress` → `completed` registrada em 2026-09-08.

## `session_2026-09-08-arquivos-erros-01`

- Status: concluída
- Duração planejada: 40 minutos
- Lição: `lesson_02-arquivos-erros`
- Objetivo: distinguir CSV e JSON e escolher o formato adequado para um caso simples de automação.
- Modo: `assessment`; núcleo cognitivo: reconhecer a estrutura dos formatos, relacioná-la ao tipo de dado e justificar uma escolha.
- Checkpoint: sessão encerrada. `return` foi movido para depois do `for`, mas `result = linha.copy()` sobrescreve o resultado a cada ciclo e devolve apenas a última linha. Acumulação real de todas as linhas permanece pendente.
- Evidência: `evidence_python-core-csv-json-01` — Feynman autônomo correto.
- Evidência: `evidence_python-core-csv-json-02` — aplicação autônoma parcial: JSON preservou a lista de telefones, mas o CSV foi escrito como pares campo/valor em vez de tabela consistente.
- Evidência: `evidence_python-core-csv-json-03` — correção autônoma correta para uma tabela CSV com cabeçalho fixo e três colunas; dois telefones ficaram em uma célula, válido para a representação pedida.
- Evidência: `evidence_python-core-csv-read-errors-01` — Feynman correto: identificou o módulo `csv` e `FileNotFoundError` para arquivo inexistente.
- Evidência: `evidence_python-core-csv-read-errors-02` — aplicação autônoma parcial. `try`/`with open`/`except FileNotFoundError` estão adequados, mas `csv.load` não existe e o caminho de sucesso não processa nem retorna dados.
- Evidência: `evidence_python-core-csv-read-errors-03` — aplicação autônoma parcial. `csv.reader` e a iteração estão corretos; falta retornar os dados em vez de imprimi-los dentro da função.
- Evidência: `evidence_python-core-csv-read-errors-04` — aplicação autônoma parcial. `return linha` dentro do `for` encerraria a função na primeira linha; ainda falta acumular todas as linhas e retornar após a iteração.
- Ponto fraco aberto: `weak_csv-return-flow` (procedural). A ordem entre iteração, acumulação e retorno precisa de duas aplicações autônomas corretas em sessões diferentes.
- Evidência: `evidence_python-core-csv-read-errors-05` — Feynman autônomo correto: `return` no primeiro ciclo encerra a função; o retorno da coleção completa deve acontecer após o `for`.
- Evidência: `evidence_python-core-csv-read-errors-06` — aplicação autônoma parcial. O `return` saiu do `for`, mas `result = linha.copy()` sobrescreve o valor a cada ciclo e mantém somente a última linha.
- Próximo passo: iniciar uma coleção antes do `for`, adicionar cada linha sem sobrescrever e retorná-la após a iteração; depois executar com CSV real.
- Encerramento: transição `in_progress` → `completed` registrada em 2026-09-08.

## `session_2026-09-07-python-core-tests`

- Status: concluída
- Lição: `lesson_01-python-core` (concluída)
- Objetivo: escrever e executar testes pytest da regra central de `maior_igual`.
- Modo: `assessment`; núcleo cognitivo: escolher casos que provam a regra de filtragem, inclusive o limite, e deixar a função importável sem disparar o CLI.
- Checkpoint: sessão encerrada. `py -m pytest test_tarefas_01.py` — 2 passed em `E:/Lucas/Documents/formação_python/src/tarefas`.
- Evidência: `evidence_python-core-import-01` — Feynman autônomo incorreto. `from tarefas_01 import maior_igual` ainda executa o módulo inteiro; só escolhe o nome ligado no destino.
- Evidência: `evidence_python-core-import-02` — Feynman correto após pista parcial (ajuda nível 4): `input()` solto roda no import porque o Python percorre o arquivo de cima a baixo. Prática guiada, não evidência autônoma plena.
- Evidência: `evidence_python-core-structure-01` — Feynman autônomo parcial. Evitar `input()` solto está certo; colocá-lo dentro de `maior_igual` faz o teste esperar digitação ao chamar a função. A posição da `def` no topo não é o requisito.
- Evidência: `evidence_python-core-structure-02` — Feynman correto após pergunta direcional (ajuda nível 3): ao chamar `maior_igual`, o `input()` interno também executa. Prática guiada.
- Evidência: `evidence_python-core-structure-03` — Feynman autônomo correto: a função recebe uma lista de inteiros; o `input()` fica na chamada do CLI. O limite do import ficou para a pergunta seguinte.
- Evidência: `evidence_python-core-structure-04` — Feynman autônomo correto: se a chamada com `input()` ficar solta no arquivo, ela também executa no import.
- Evidência: `evidence_python-core-structure-05` — Feynman autônomo parcial: os dois usos (executar vs reutilizar) estão certos, mas o import também executa o arquivo. Falta um critério observável para o CLI.
- Evidência: `evidence_python-core-structure-06` — Feynman correto após pista (ajuda nível 4): a chamada com `input()` deve rodar quando `name` for `main`. A notação exata é `__name__ == "__main__"`; a omissão dos underscores não rebaixa a ideia.
- Evidência: `evidence_python-core-structure-07` — aplicação da guarda correta (notação guiada). `split`/`int` no corpo de `maior_igual` é o próximo ajuste para o teste com lista.
- Evidência: `evidence_python-core-structure-08` — Feynman autônomo correto: a função atual quebra com lista de inteiros porque ainda converte a entrada. Refinamento: `.split()` é método de string, não de lista de strings.
- Evidência: `evidence_python-core-structure-09` — aplicação autônoma parcial. A função agora aceitaria `[5, 10, 20]`. No CLI, `split` não é chamado, então o programa quebra ao iterar.
- Evidência: `evidence_python-core-structure-10` — aplicação correta após pergunta direcional: `numeros.split()` no CLI; módulo importável e filtragem em lista. `int()` no corpo não bloqueia o teste com inteiros.
- Evidência: `evidence_python-core-tests-01` — aplicação autônoma parcial. O import e o `assert` estão no caminho; `def test_maior_igual(lista)` e `maior_igual() == int(...)` não testam a regra com um exemplo fechado.
- Evidência: `evidence_python-core-tests-02` — aplicação autônoma parcial. A `def` sem parâmetro está correta; `str([])` e `int([])` não são listas de números.
- Evidência: `evidence_python-core-tests-07` — aplicação correta após pista (ajuda nível 4): `assert maior_igual([10, 20, 30]) == [10, 20, 30]`.
- Evidência: `evidence_python-core-tests-08` — aplicação autônoma correta: `maior_igual([10, 6, 8, 20]) == [10, 20]`. Exclui `< 10`, mantém o limite `10` e o valor acima, preserva a ordem.
- Evidência: `evidence_python-core-pytest-01` — aplicação autônoma correta: `py -m pytest test_tarefas_01.py`, 2 passed. Arquivos `tarefas_01.py` e `test_tarefas_01.py` no projeto do estudante.
- Encerramento: transição `in_progress` → `completed`. Lição `lesson_01-python-core` concluída (CLI, função, testes).
- Próximo passo: `lesson_02-arquivos-erros` (CSV/JSON, erros explícitos e módulos).

## `session_2026-09-03-python-core-01`

- Status: concluída
- Lição: `lesson_01-python-core`
- Objetivo: resolver problemas decompondo entradas, regras e saídas com tipos, fluxo, coleções e funções.
- Modo: `assessment`; núcleo cognitivo: decompor um problema em entrada, regras e saída e escolher estruturas Python proporcionais.
- Checkpoint: sessão encerrada. Aplicação, transferência e implementação do CLI corretas; `tarefas-01.py` executou e produziu `[10, 20, 65]`. Testes pytest ainda pendentes.
- Evidência: `evidence_python-core-pares-01` — aplicação autônoma correta ao filtrar números pares de uma lista.
- Feedback: a ideia central, o contexto e a justificativa observável estão adequados. `filtra_pares` seria nome mais preciso que `conta_par`, mas isso é melhoria opcional.
- Evidência: `evidence_python-core-modulo-01` — explicação Feynman autônoma parcial. A ideia de resto zero está correta, mas o exemplo confundiu divisão comum (`7 / 2 = 3,5`) com o resto usado pelo operador `%`.
- Evidência: `evidence_python-core-modulo-02` — autocorreção Feynman autônoma ainda parcial. O resto `1` e o múltiplo `6` foram identificados, mas o quociente foi informado como `1`.
- Evidência: `evidence_python-core-modulo-03` — autocorreção correta após pista direcional: `2` cabe 3 vezes em `6` e sobra `1`. Conta como prática guiada, não como evidência autônoma plena.
- Evidência: `evidence_python-core-lista-01` — identificação autônoma correta de `numeros` como lista de valores inteiros. “Não ordenados” foi uma observação desnecessária; listas mantêm ordem, mas isso não era requisito da pergunta.
- Evidência: `evidence_python-core-item-01` — identificação autônoma correta de `num` como item corrente da lista em cada iteração.
- Evidência: `evidence_python-core-funcao-01` — explicação Feynman autônoma correta do papel da função, iteração, `append` e `return`.
- Evidência: `evidence_python-core-transfer-01` — aplicação autônoma correta com transferência para filtrar valores maiores ou iguais a 10 em uma lista diferente.
- Evidência: `evidence_python-core-cli-choice-01` — escolha autônoma correta de entrada digitada, com justificativa de proximidade a uma CLI real e escopo proporcional ao nível atual.
- Evidência: `evidence_python-core-cli-implementation-01` — aplicação autônoma correta: `tarefas-01.py` leu seis inteiros, converteu, filtrou valores `>= 10` e foi executado com `python tarefas-01.py`, produzindo `[10, 20, 65]`.
- Domínio de `topic_python-fundamentos`: 60 → 80. Os requisitos de Feynman, aplicação e transferência autônomos foram atendidos.
- Lição `lesson_01-python-core`: permanece em andamento porque ainda faltam programa CLI e testes exigidos pela entrega.
- Próximo passo: escrever testes pytest para a regra central de `maior_igual` e executá-los.
- Encerramento: transição `in_progress` → `completed` registrada em 2026-09-03.

## Revisão do contrato AI Tutor (`revision` 14)

- Data: 2026-09-03.
- Motivo: alinhar a formação às regras atuais de `cognitive core`, modos `learning`/`assessment`/`performance`, escada de ajuda, capacidade residual e prontidão para delegação.
- Alterações: o contrato pedagógico foi incorporado ao currículo; o capstone passou a exigir plano/registro de delegação e verificação; a revisão canônica avançou de 13 para 14.
- Preservado: configuração, sessões concluídas, evidências, domínio 80 de `topic_workflow-profissional`, ponto fraco resolvido e `next_focus: lesson_01-python-core`.
- Nenhuma evidência ou domínio foi criado, removido ou reclassificado.

## `session_2026-09-02-transfer`

- Status: concluída
- Lição: `lesson_00-diagnostico`
- Objetivo: transferir o fluxo profissional para outro diretório (pasta, venv, programa, pytest, Git local e remoto), com menos ajuda.
- Entrega: `C:\Users\lucka\Documents\projects\sandbox-transferencia`; `informacoes_aluno.py` + `test_informacoes_aluno.py`; `pytest` 1 passed; commit `54320a2`; remoto vazio [sandbox-transferencia](https://github.com/14lucas-mendes/sandbox-transferencia); `git push origin master`; `deactivate`.
- Evidência: `evidence_diagnostico-transfer-01` — aplicação **autônoma com transferência**, correta. `git log -l` foi autocorreção; `-u` omitido é refinamento, não erro.
- Domínio de `topic_workflow-profissional`: 60 → **80**. Lição `lesson_00-diagnostico` concluída.
- Ponto fraco `weak_workflow-pasta-repositorio` resolvido (remoto autônomo em sessão anterior + transferência com `mkdir`/`cd` e `deactivate` nesta).
- Próximo passo: `lesson_01-python-core`.

## Revisão do contrato de avaliação (`revision` 9)

- Fonte: `learning-contract.md` da skill `ai-tutor` (hash `80f51c29431d603f61f43d7afad5b5865819c7cb42b79966ad3e288cb1f40218`, fonte = instalação).
- Matriz de domínio 60/80/100 inalterada. Respostas passam a ser classificadas por ideia central, contexto e justificativa; omissão opcional e redação não rebaixam sozinhas.
- `evidence_diagnostico-workflow-04`: **parcial → correta** (Feynman autônomo). “Sincronizar” não foi lido como afirmação de que o remoto já existia.
- `evidence_diagnostico-workflow-03` e `evidence_diagnostico-pytest-01`: **parcial → correta**, ainda **guiadas** (`autonomous: false`). pytest/remoto fora de escopo e mensagem de commit genérica deixaram de contar como erro.
- `evidence_diagnostico-workflow-01` e `02` permanecem parciais (confusão material `mkdir` vs repositório / `commit add`).
- Ponto fraco `weak_workflow-pasta-repositorio` segue ativo, agora apoiado só em 01–03.

## `session_2026-09-02-remoto`

- Status: concluída
- Lição: `lesson_00-diagnostico`
- Objetivo: conectar o repositório local do sandbox a um remoto vazio no GitHub com `git remote add` e `git push`.
- Entrega: repositório vazio em https://github.com/14lucas-mendes/sandbox-diagnostico ; `git remote add origin`; `git push -u origin master`; `master` rastreia `origin/master`; commit `e1df64b`.
- Evidência: `evidence_diagnostico-remoto-01` — aplicação **autônoma correta** (comandos construídos pelo estudante; `-u` foi escolha extra, não requisito).
- Domínio de `topic_workflow-profissional`: 40 → **60** (Feynman autônomo `workflow-04` + esta aplicação independente). Transferência ainda não houve; 80 e fechamento da lição continuam abertos.
- Ponto fraco `weak_workflow-pasta-repositorio` segue ativo (falta segunda aplicação autônoma noutra sessão, incluindo encerramento do venv).
- Próximo passo: repetir o fluxo noutro diretório, com menos ajuda.

## `session_2026-09-01-pytest`

- Status: concluída
- Lição: `lesson_00-diagnostico`
- Objetivo: instalar pytest no venv do sandbox, escrever um teste mínimo e vê-lo passar.
- Entrega: `pytest 9.1.1` no `.venv`; `hello.py` com `saudacao()`; `test_hello.py` com `from hello import saudacao` e `assert saudacao() == "hello"`; `1 passed`; `.gitignore` com `__pycache__/`; commit do estudante `e1df64b`.
- Evidência: `evidence_diagnostico-pytest-01` — aplicação **correta e guiada** (`autonomous: false`). O `assert` foi corrigido após feedback; o import foi fornecido. A mensagem de commit genérica é refinamento, não erro.
- Domínio de `topic_workflow-profissional` era 40 nesta sessão; subiu para 60 após o remoto autônomo da sessão seguinte.
- Lição permanece em andamento: falta remoto e transferência.
- Próximo passo: criar repositório vazio no GitHub, `git remote add` e `push`.

## `session_2026-08-31-diagnostico`

- Status: concluída
- Lição: `lesson_00-diagnostico`
- Objetivo: medir autonomia para criar, executar, testar e versionar um projeto Python mínimo.
- Tentativa registrada: o estudante explicou corretamente a ideia de `git add`, `git commit` e `git push`, mas confundiu `mkdir` com `git init` e não lembrou o fluxo de criação/ativação do ambiente virtual.
- Evidência: `evidence_diagnostico-workflow-01` — explicação autônoma parcial; não eleva domínio além de 20.
- Segunda tentativa: sequência quase completa, mas ainda com confusão entre pasta e repositório e `commit add` no lugar de `git add`. `deactivate` e remoto foram omissoes opcionais nessa reescrita.
- Evidência: `evidence_diagnostico-workflow-02` — tentativa guiada; não é evidência autônoma.
- Execução em `C:/Users/lucka/Documents/projects/sandbox-diagnostico`: pasta, `.venv`, `hello.py` executado, `git init`, `.gitignore` excluindo `.venv`, commit do estudante `2d4864a`, `deactivate` conferido.
- Evidência: `evidence_diagnostico-workflow-03` — aplicação **correta e guiada** (venv/ativação fornecidos; `cd` após `mkdir` com pista). pytest e remoto estavam fora do objetivo da tentativa.
- Evidência: `evidence_diagnostico-workflow-04` — Feynman **autônomo correto** da distinção pasta / Git local / remoto, após reavaliação literal.
- Domínio de `topic_workflow-profissional`: 20 → 40. Lição permanece em andamento (falta remoto executado e transferência).
- Ponto fraco aberto: `weak_workflow-pasta-repositorio` (precisão).
- Próximo passo: pytest mínimo no sandbox e, se houver repositório no GitHub, `git remote add` + `push`.
