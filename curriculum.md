# Formação oficial: Automação e Integração de Sistemas com Python

## Objetivo profissional

Formação de transição de carreira de cerca de onze meses (estendida em 2026-10-06; antes, nove meses) para atuar em Automação e Integração de Sistemas com Python. O foco é transformar experiência em manutenção, sistemas críticos, diagnóstico de falhas, processos operacionais e documentação em autonomia técnica demonstrável.

O programa tem 16 ciclos de 21 dias (eram 13 até 2026-10-06, quando entrou o bloco de lógica). Dias protegidos: segunda, terça, quinta, sexta e domingo. Em dia de trabalho, a sessão dura até 1h30; em dia de folga, até 2h. A distribuição semanal é: segunda (conceito e prática guiada), terça (recriação independente), quinta (aplicação no projeto), sexta (lógica, debugging ou teste técnico) e domingo (projeto e revisão).

## Calendário de referência

Data oficial de início: **2026-08-31**, a primeira sessão (escolhida pelo aluno em 2026-09-29; canônico em `study-config.json`, campos `program_start_date` e `cycle_calendar`). O calendário é informativo: o avanço continua dependendo de evidência, não de data.

| Ciclo | Janela | Ciclo | Janela |
|---|---|---|---|
| 1 | 31/08 – 20/09/2026 | 9 | 15/02 – 07/03/2027 |
| 2 | 21/09 – 11/10/2026 | 10 | 08/03 – 28/03/2027 |
| 3 | 12/10 – 01/11/2026 | 11 | 29/03 – 18/04/2027 |
| 4 | 02/11 – 22/11/2026 | 12 | 19/04 – 09/05/2027 |
| 5 | 23/11 – 13/12/2026 | 13 | 10/05 – 30/05/2027 |
| 6 | 14/12/2026 – 03/01/2027 | 14 | 31/05 – 20/06/2027 |
| 7 | 04/01 – 24/01/2027 | 15 | 21/06 – 11/07/2027 |
| 8 | 25/01 – 14/02/2027 | 16 | 12/07 – 01/08/2027 |

Em 2026-09-29, pelo calendário, o estudo estaria no Ciclo 2 (dia 9); o trabalho real está no Ciclo 4, cuja janela de calendário começa em 02/11/2026.

## Regra de avanço e uso de IA

Uma competência só avança com evidência demonstrada: explicação autônoma, implementação de uma variação e diagnóstico de um erro relacionado. A IA atua primeiro como tutora: pergunta, oferece pistas, explica, conduz debugging e revisa código. Implementação central fornecida antes da tentativa é prática guiada, não evidência autônoma.

Desde a revisão de roadmap de 2026-10-05, aprovada pelo aluno, o núcleo inclui FastAPI, React com TypeScript (Vite), CI com GitHub Actions e o fluxo Git profissional de dev solo. Esses temas entram porque compõem o projeto de portfólio (Segundo Cérebro). O núcleo continua sem Docker, n8n, deploy, cloud, MCP, agentes, RAG e frameworks de IA. Esses temas permanecem no backlog pós-transição e não alteram o percurso sem mudança explícita de roadmap ou oportunidade profissional concreta.

## Ciclos de 21 dias

| Ciclo | Foco | Lição canônica | Marco observável |
|---|---|---|---|
| 1 | Lógica, decomposição e Python core | `lesson_01-python-core` | Resolver entradas, regras e saídas com funções e testes simples. Concluído por evidência prévia válida. |
| 2 | Debugging sistemático | `lesson_03-testes-git` | Formular hipóteses, isolar uma falha e verificar a correção. Concluído em 2026-09-12, com correção verificada por execução. |
| 3 | Git e GitHub | `lesson_04-descoberta-processo` | Histórico legível e remoto quando aplicável. Concluído em 2026-09-17, com preflight reconstruído sem comandos fornecidos. |
| 4 | Arquivos, CSV e JSON | `lesson_02-arquivos-erros` | Ler arquivos completos, tratar erros e modularizar. Concluído em 2026-10-06: entrada inválida tratada, módulos separados e README do módulo 02 (`evidence_lesson02-readme-01`). |
| 5 | Lógica: decompor, planejar e rastrear | `lesson_15-logica-decomposicao` | Antes do código: entrada, regra, saída, exemplos com saída esperada à mão e plano dividido em subproblemas; tabela de rastreio conferida por execução. |
| 6 | Estruturas de dados | `lesson_16-estruturas-dados` | Lista, dicionário, tupla e conjunto escolhidos e justificados; acumular, contar, agrupar, filtrar, buscar e dados aninhados no índice das notas. |
| 7 | Algoritmos e debugging por hipótese | `lesson_17-algoritmos-debugging` | Busca binária e ordenação testadas com valor esperado, custo em passos explicado, defeitos diagnosticados com hipótese escrita. |
| 8 (início) | Git profissional de dev solo | `lesson_14-git-fluxo-profissional` | Repositório `segundo-cerebro` com `main` protegida e `develop`, fatia entregue por feature branch e PR com CI, primeira tag `v0.1`. |
| 8 | SQL relacional: memórias versionadas | `lesson_05-automacao-confiavel` | SQLite com memórias versionadas, consulta por data, busca FTS5 e tabelas de manutenção. |
| 9 | HTTP e APIs REST: importador do GitHub | `lesson_06-http-apis` | Importar commits e repositórios pela API do GitHub com timeout, erros e paginação tratados. |
| 10 | Integração e API própria (FastAPI) | `lesson_07-fastapi-dados` | API do Segundo Cérebro com modelos tipados, integrando todas as fontes com falhas rastreáveis. |
| 11 | Selenium: captura de páginas | `lesson_08-llm-estruturado` | Capturar páginas públicas para o cérebro com esperas explícitas e falha diagnosticada. |
| 12 | Módulo de manutenção e "sonhar" | `lesson_09-seguranca-custo` | Regras de reincidência com dados fictícios e relatório periódico de padrões. |
| 13 | React e TypeScript I | `lesson_10-agente-ferramentas` | Diagnóstico prévio; interface tipada consumindo a API (busca e linha do tempo). |
| 14 | React e TypeScript II | `lesson_11-agente-controle` | Captura pela interface, relatório na tela e fluxo ponta a ponta com falhas tratadas. |
| 15 | Qualidade e CI completo | `lesson_12-docker-ci` | pytest, debugging, refatoração e CI com lint, tipos e build do frontend. |
| 16 | Portfólio e processos seletivos | `lesson_13-deploy-portfolio` | Repositório legível com PRs e releases, demo de 3 a 5 minutos e testes de entrada. |

A partir da `lesson_14`, toda fatia do projeto entra por feature branch e pull request para `develop`; no fim de cada ciclo, um PR de `develop` para `main` publica uma release com tag.

## Projeto principal

Desde 2026-10-05, o projeto principal é `project_segundo-cerebro`, o **MVP do Segundo Cérebro**: uma memória pessoal em Python com memórias versionadas no tempo, busca de texto, síntese periódica ("sonhar"), API própria em FastAPI e interface em React com TypeScript. Ele guarda dados reais do aluno (notas do cofre Obsidian, registros do tutor, commits) e será construído progressivamente, nunca entregue pronto pela IA, num repositório separado `segundo-cerebro` com fluxo profissional de branches, PRs, CI e releases. O repositório público usa só dados de exemplo fictícios. A proposta completa, com o raciocínio de cada ciclo, está em `docs/compose/spec/segundo-cerebro-roadmap.md`.

Os dois projetos anteriores foram absorvidos como módulos e arquivados no estado canônico, sem perda de histórico:

- `project_automacao-processo-real` (Sistema de Automação de Manutenção — Demo) virou o **módulo de manutenção**, com dados fictícios, regras de reincidência e relatório (Ciclo 9).
- `project_api-llm-servico` (cliente de API pelo terminal) virou o **importador do GitHub** (Ciclo 6).

Busca por embeddings ou RAG, LLM na síntese "sonhar", servidor MCP e deploy ficam no backlog pós-transição (`project_agente-operacional`, `project_capstone-producao`).

## Estado inicial no novo currículo

- Competência validada: Python core e programas pequenos testáveis (`topic_python-fundamentos`) — domínio 80. Até 2026-10-07 o tópico se chamava "Lógica, decomposição e Python core"; o nome mudou para não se confundir com `topic_logica-algoritmos`, que começa em 0.
- Competência validada: Git, testes básicos e fluxo profissional — domínio 80.
- Trabalho preservado e reposicionado: CSV/JSON tem tentativas e explicações válidas, mas a leitura de um CSV real com retorno completo ainda precisa ser demonstrada no Ciclo 4.
- Pontos fracos preservados: lista literal em testes, fluxo de acumulação/retorno em CSV e o modelo de dois tempos do Python (momento em que cada tipo de erro é detectado).
- Ciclo concluído: 2, debugging sistemático (`lesson_03-testes-git`), em 2026-09-12, com correção verificada por execução.
- Ciclo concluído: 3, Git e GitHub (`lesson_04-descoberta-processo`), em 2026-09-17. O preflight foi reconstruído sem comandos fornecidos e a forma exata dos comandos de remoto foi fechada no ciclo de erro; permanece aberto apenas o ponto de precisão `weak_git-formas-exatas-comandos`, agora observável no uso real.
- Regra do aluno registrada em 2026-09-17: fechamento de lição não exige contexto novo sintético quando o tópico já sustenta o domínio exigido com evidência autônoma real de transferência.
- Ciclo concluído: 4, Arquivos, CSV e JSON (`lesson_02-arquivos-erros`), em 2026-10-06. `topic_automacao-confiavel` em 80; o README do módulo 02 fechou o último critério de entrega. `weak_csv-return-flow` foi resolvido em 2026-09-22.
- Próxima lição: `lesson_15-logica-decomposicao` (Ciclo 5), depois de um `/diagnostic` curto de lógica.
- Bloco de lógica aprovado em 2026-10-06 (estado revisão 184): novo tópico `topic_logica-algoritmos` (domínio 0; não herda nem rebaixa os 80 de fundamentos), lições 15 a 17 nos ciclos 5 a 7, `lesson_14` passa a depender da `lesson_17` e o calendário vai a 16 ciclos (até 01/08/2027). Depois do bloco, toda sexta-feira tem um exercício curto de lógica. Prática sugerida: Python Lab (referência), *Entendendo Algoritmos* (Bhargava) e *Estruturas de Dados e Algoritmos com JavaScript* (Groner). Proposta: `docs/compose/spec/bloco-logica-roadmap.md`.
- Revisão de roadmap em 2026-10-05 (estado revisão 172): projeto principal passa a ser o Segundo Cérebro; nova `lesson_14-git-fluxo-profissional`; novo tópico `topic_frontend-react` (domínio 0; o conhecimento prévio de React/Next não conta como domínio e será medido por diagnóstico antes da `lesson_10`). Nenhuma evidência, domínio ou ponto fraco foi alterado.

<!-- IDs, evidências, sessões e critérios canônicos estão em .ai-tutor/state.json. -->
