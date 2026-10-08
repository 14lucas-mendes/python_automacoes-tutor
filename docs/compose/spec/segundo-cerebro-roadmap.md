---
feature: segundo-cerebro-roadmap
status: approved
updated: 2026-10-05
state_revision_base: 171
applied_revision: 172
---

# Proposta de roteiro: o Segundo Cérebro como projeto da formação

> [!warning] Substituído por [`formacao-fechada.md`](formacao-fechada.md) em 2026-10-08
> Este roteiro fica só como histórico. O projeto passou a ser o app da própria formação, o MVP foi reduzido, a lição de manutenção foi arquivada e entraram Python intermediário, Docker/VPS e IA aplicada.

> **Status: aprovada pelo aluno em 2026-10-05 e aplicada** (`state.json` revisão 172, `curriculum.md`, `AGENTS.md`).
>
> Em 2026-10-08 os IDs herdados do roteiro antigo foram renomeados neste documento e no estado (revisão 188), por exemplo `lesson_08-llm-estruturado` → `lesson_08-selenium-captura`. A tabela completa está no `session-log.md`, e cada item renomeado guarda o ID antigo em `former_id`.

## 1. A decisão, em uma frase

O projeto de portfólio da formação passa a ser o **MVP do Segundo Cérebro**: uma memória pessoal
escrita em Python, com API própria (FastAPI) e interface web em React com TypeScript (Vite), desenvolvida
num repositório próprio com fluxo Git profissional de dev solo (branches `main`/`develop`, PRs, CI e
releases). Ele guarda como o aluno
pensa, como escreve e estrutura código, como lida com dúvidas e tudo o que faz no curso. A demo de
manutenção vira um **módulo** dele.

Decisões do aluno em 2026-10-05: um cofre só ("Segundo Cérebro"); a demo de manutenção vira módulo;
interface web local; frontend em React (o aluno já usou React e Next na Mate Academy).
Acréscimos do aluno no mesmo dia: **TypeScript**, para se alinhar ao mercado, e **Git/GitHub profissional**,
com PRs e branches separadas de produção e desenvolvimento, como dev solo.

Inspiração: vídeo [Super memória vs. Segundo Cérebro](https://youtu.be/3CBIhTVAGCE) (Vini Lana).
Destas ideias, o MVP implementa quatro:

| Ideia do vídeo | Como aparece no MVP |
|---|---|
| Memória **fora** do agente, sem ficar preso a uma ferramenta | Os dados ficam em Markdown, JSON e SQLite, formatos abertos. Qualquer agente ou interface lê pela API. |
| **Memória versionada no tempo** | Cada memória tem tema e histórico. Uma mudança cria uma versão nova, sem apagar a anterior. |
| **Busca que traz só o trecho certo** | Busca por texto completo no SQLite (FTS5), que devolve o trecho e aponta para a nota inteira. |
| **Dreaming (sonhar)** | Um script periódico lê os registros e escreve um relatório de padrões: erros que se repetem, temas que voltam, reincidências de manutenção. |

## 2. O que **não** muda

- **Histórico.** As lições concluídas (`lesson_00`, `01`, `03`, `04`), as evidências, o domínio de cada tópico e os pontos fracos ficam como estão.
- **Regra de avanço.** O avanço continua dependendo só de evidência, pela matriz normativa (20/40/60/80/100). Escrever código do projeto não é evidência por si só.
- **Calendário.** Continuam 13 ciclos de 21 dias, com fim em 2027-05-30. O trabalho real está cerca de um ciclo à frente do calendário, e essa folga absorve o React.
- **IDs.** Os `lesson_id` antigos são mantidos, como na reorganização anterior do roteiro: o título muda e o ID fica estável.
- **`lesson_02-arquivos-erros`.** Os critérios dela não mudam. Ela só ganha uma ligação explícita com o projeto.
- **Regras pedagógicas do `AGENTS.md`.** Valem como antes. Em especial, a regra 1 (explicar antes de avaliar) e a regra 2 (nunca assumir conhecimento) se aplicam ao React.

## 3. Como o MVP fica montado

```text
 FONTES (dados reais do aluno)           NÚCLEO PYTHON                         INTERFACE
 ─────────────────────────────           ─────────────                         ─────────
 Cofre Obsidian (Markdown)   ─┐
 Registros do tutor (.ai-tutor)├─► importadores ─► SQLite ─► "sonhar" ─┐
 Commits / GitHub (API)       ─┤   (Ciclos 4–7)    memórias    relatório│
 Módulo manutenção (fictício) ─┘                   versionadas  padrões │
                                                   + busca FTS          ▼
                                                        └──► API FastAPI ──► React + TypeScript
                                                             (Ciclo 7)        (Vite, Ciclos 10–11)

 REPOSITÓRIO segundo-cerebro (GitHub):  feature/* ──PR──► develop ──PR + tag──► main (produção)
                                         CI (GitHub Actions) roda os testes em todo PR
```

**Fora do MVP, no backlog depois da transição:** busca por significado (embeddings ou RAG),
LLM no "sonhar", servidor MCP para agentes lerem a memória, deploy e cloud. Como o MVP já tem
API e formatos abertos, essas peças entram depois sem reescrever nada.

### O que é "pronto" para o MVP

1. Importa notas do cofre, registros do tutor, commits e registros de manutenção.
2. Guarda memórias com histórico de versões e permite consultar "como este tema estava em tal data".
3. Faz busca por texto que devolve o trecho e o link da nota.
4. Gera o relatório do "sonhar" sob demanda ou agendado.
5. Tem uma interface React em TypeScript com captura, busca, linha do tempo de um tema e leitura do relatório.
6. Tem testes pytest nas regras centrais e na API, CI verde em `main` e um README.
7. Tem um repositório GitHub legível, com histórico de PRs e releases por ciclo, uma demo de 3 a 5 minutos e dados de exemplo fictícios. Os dados pessoais reais não vão para o repositório.

## 4. Os ciclos

Cada linha registra o que `references/programming.md` exige de um item de programação: a âncora no
projeto, a capacidade anterior revisitada, a nova restrição e a transferência esperada.

| Ciclo | Lição (ID mantido) | Novo foco | Peça do MVP / critérios de entrega | Revisita → nova restrição | Transferência esperada |
|---|---|---|---|---|---|
| 1–3 | `00`, `01`, `03`, `04` | concluídos | — | — | — |
| 4 | `lesson_02-arquivos-erros` | Arquivos, CSV, JSON e exceções (**sem mudança nos critérios**) | Fecha com o README já previsto. Ponte opcional, que não é critério de fechamento: um script que lê as notas do cofre e gera `indice.json` (título, tipo, data, tags). | CSV/JSON → **Markdown com cabeçalho de metadados (frontmatter)** | Ler um formato novo sem receita pronta. Pode virar a evidência de 100 do tópico (outro contexto). |
| 5 (início) | **`lesson_14-git-fluxo-profissional`** (nova, 1–2 sessões) | Git profissional de dev solo | Cria o repositório `segundo-cerebro` no GitHub com `main` protegida e `develop`; primeira fatia por `feature/...` → PR → merge; CI mínimo (GitHub Actions rodando pytest); primeira tag `v0.1`. **Critérios:** branches criadas pelo aluno, PR com descrição e autorrevisão, CI executado, tag publicada. | commits e push no `main` → **branches, PR, merge e release** | Toda fatia seguinte entra por PR sem roteiro de comandos: o fluxo vira hábito observável. |
| 5 | `lesson_05-sql-memorias` | SQL relacional: memórias versionadas | Banco SQLite com tabelas `memoria`, `versao`, `tema` e `fonte`; consulta "estado do tema na data X"; busca FTS5; tabelas do módulo de manutenção (falha, equipamento, atividade). **Critérios:** tabelas relacionadas, consultas com join e por data, resultado explicado. | `indice.json` → **banco relacional com histórico** | Modelar um domínio novo (manutenção) sozinho. |
| 6 | `lesson_06-http-apis` | HTTP e APIs REST: importador do GitHub | Cliente que lê os seus commits e repositórios pela API do GitHub e grava no banco ("como eu escrevo código"). **Critérios:** cliente HTTP, timeout e erros de rede tratados, paginação, testes com mock. | Ler arquivo → **ler da rede, que pode falhar** | Consumir uma segunda API com outro contrato. |
| 7 | `lesson_07-fastapi-dados` | Integração de sistemas + **API própria (FastAPI)** | Endpoints de captura, busca, linha do tempo e relatório; integra cofre, tutor, GitHub e manutenção num fluxo com falhas registradas. Os formatos de dados viram modelos Pydantic com type hints, a ponte para o TypeScript. **Critérios:** mapeamento de entradas e saídas, endpoints documentados, modelos tipados, falhas tratadas, registro de execução. | Consumir API → **servir uma API** | Explicar o contrato da própria API e diagnosticar uma falha de integração. |
| 8 | `lesson_08-selenium-captura` | Automação web (Selenium): captura de páginas | Captura automatizada de páginas públicas, artigos ou documentação, para dentro do cérebro, com esperas explícitas. **Critérios:** navegação automatizada, esperas explícitas, falha diagnosticada. | API pronta → **site sem API** | Automatizar um segundo site sozinho. |
| 9 | `lesson_09-manutencao-sonhar` | Módulo de manutenção + **"sonhar"** | Importa registros fictícios de manutenção, aplica as regras de reincidência e gera o relatório de padrões: reincidências, e também erros e dúvidas que se repetem no próprio estudo. **Critérios:** dados fictícios, regras testadas, relatório verificável, README de domínio. | Consultas soltas → **síntese periódica** | Aplicar o mesmo "sonhar" a uma fonte diferente. |
| 10 | `lesson_10-react-typescript-1` | **Frontend React + TypeScript I** (Vite, modelo `react-ts`) | Projeto React em TypeScript consumindo a API: busca e linha do tempo de um tema; estados de carregamento e erro; tipos que espelham os modelos da API. **Começa por diagnóstico de React e TypeScript** (seção 6). **Critérios:** componentes tipados, estado, chamada à API tipada, erro da API mostrado na tela, `tsc` sem erros. | Testar API pelo terminal → **consumir no navegador** (inclui CORS) | Criar uma tela nova sem modelo. |
| 11 | `lesson_11-react-typescript-2` | **Frontend React + TypeScript II** + ponta a ponta | Captura pela interface, leitura do relatório do "sonhar", navegação; o fluxo completo funcionando. **Critérios:** fluxo ponta a ponta, falhas tratadas na tela, limites conhecidos documentados. | Tela de leitura → **tela que escreve dados** | Diagnosticar uma falha que atravessa frontend, API e banco. |
| 12 | `lesson_12-qualidade-ci` | Qualidade: pytest, debugging, refatoração e CI completo | Testes das regras, da API (TestClient) e dos importadores; refatoração sem mudar o comportamento; o CI passa a rodar também lint, checagem de tipos (Python e `tsc`) e o build do frontend. **Critérios:** testes relevantes, debugging registrado, refatoração verificada, CI cobrindo backend e frontend. | CI mínimo do Ciclo 5 → **CI que barra PR quebrado** | Diagnosticar um PR com o CI vermelho sozinho. |
| 13 | `lesson_13-portfolio` | GitHub, testes técnicos e portfólio | README, repositório público com dados de exemplo, demo de 3 a 5 minutos, simulações de teste técnico. | — | — |

## 5. Mudanças exatas no estado canônico (depois da aprovação)

Todas as escritas usam `scripts/state_io.atomic_update_json` com `expected_revision`, e o
`validate_study` roda ao final.

**`state.json`**
- `lessons`: novos `title`, `objective` e `delivery_criteria` de `lesson_05` a `lesson_13`, conforme a tabela; `lesson_10` e `lesson_11` passam para `topic_id: topic_frontend-react`. A `lesson_02` recebe só uma `progress_note` com a ligação ao projeto.
- `lessons`: nova `lesson_14-git-fluxo-profissional` (`status: planned`, `topic_id: topic_workflow-profissional`, pré-requisito `lesson_02-arquivos-erros`); `lesson_05` passa a ter `lesson_14` como pré-requisito.
- `topics`: novo `topic_frontend-react` ("React e TypeScript consumindo API"), com `mastery: 0` e `status: not_started`. O conhecimento prévio **não** vira domínio. `topic_workflow-profissional` mantém domínio 80 e evidências; o objetivo ganha "branches, PRs, CI e releases". Os demais tópicos mantêm nome, domínio e evidências; só `topic_integracao-fastapi` ganha a menção à API própria no objetivo.
- `projects`:
  - novo `project_segundo-cerebro`, com `status: planned` (passa a `in_progress` na primeira fatia), `lesson_ids` de `lesson_02` e de `lesson_05` a `lesson_13`, objetivo e critérios da seção 3;
  - `project_automacao-processo-real` → `status: archived`, com nota "absorvido como módulo de manutenção de `project_segundo-cerebro` em 2026-10-05";
  - `project_api-llm-servico` → `status: archived`, com nota "absorvido como importador do GitHub (Ciclo 6)";
  - `project_agente-operacional` (backlog): o objetivo passa a citar o servidor MCP do Segundo Cérebro e a busca por embeddings.
- `next_focus` continua `lesson_02-arquivos-erros`.

**Projeções e regras**
- `curriculum.md`: tabela de ciclos, seção "Projeto principal" e o parágrafo do núcleo. FastAPI, React, TypeScript e CI com GitHub Actions passam a fazer parte do núcleo; Docker, n8n, deploy, cloud, MCP, agentes, RAG e frameworks de IA continuam fora.
- `AGENTS.md`: nova seção "Projeto Segundo Cérebro" (âncora dos exercícios) e a regra de captura contínua (seção 7), se aprovada.
- `session-log.md`: entrada escrita à mão registrando a decisão. **Sem `scripts.projections`.**
- Cofre: a nota `10 - Projetos/Segundo Cérebro.md` deixa de ter "atualizar o roteiro" como pendência.

## 6. React e TypeScript: como entram sem quebrar as regras

- Antes do Ciclo 10, um `/diagnostic` curto mede o que restou da Mate Academy: componentes, props, estado, efeitos, `fetch` e tipos básicos de TypeScript. O diagnóstico só escolhe por onde começar e quanto explicar. Ele **não** gera domínio nem evidência.
- O TypeScript entra desde o primeiro arquivo do frontend (modelo `react-ts` do Vite), e não como migração posterior. A ponte começa no Python: type hints aparecem nos Ciclos 5 a 7 e viram modelos Pydantic no FastAPI, então a ideia de "declarar o formato do dado" chega ao TypeScript já conhecida.
- Escopo do TypeScript no MVP: tipos e interfaces dos dados da API, props tipadas, tipagem de `fetch` e de estado, `tsc` sem erros. Genéricos avançados e tipos utilitários complexos ficam para depois, salvo necessidade real.
- O Next fica de fora porque teria servidor e rotas de API próprios, duplicando o FastAPI. Essa separação (Python no backend, React só na tela) é a que mostra integração de sistemas.

## 6a. Fluxo Git profissional de dev solo

Vale do primeiro commit do repositório `segundo-cerebro` até o fim da formação.

| Peça | Regra |
|---|---|
| `main` | Produção. Protegida no GitHub: só recebe PR vindo de `develop`, com CI verde. |
| `develop` | Desenvolvimento. Recebe os PRs das fatias. |
| `feature/<fatia>` | Uma branch por fatia de trabalho, criada a partir de `develop`. Correções urgentes usam `fix/<assunto>`. |
| Pull request | Título claro, descrição (o que muda, por quê, como testar), autorrevisão do diff e CI verde antes do merge. |
| Release | No fim de cada ciclo, PR `develop` → `main` e tag (`v0.1`, `v0.2`…), com notas curtas da versão. |
| Commits | Mensagens no padrão Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`), que este repositório já usa. |

- O aluno executa os comandos e cria os PRs. O tutor explica antes (regra 1), revisa e nunca faz commit pelo aluno.
- Configurar a proteção da `main` é uma configuração da conta do GitHub, feita pelo próprio aluno com orientação.
- É uma revisita em espiral de `topic_workflow-profissional` (hoje 80) com restrições novas. O uso real repetido ao longo dos ciclos é o contexto natural para chegar a 100 (matriz: repetição em duas sessões e dois contextos com detecção de limite ou autocorreção). O ponto fraco `weak_git-formas-exatas-comandos` passa a ser observado nesse uso real.

## 7. Captura contínua desde já (para aprovar à parte)

Os dados do Segundo Cérebro começam a ser registrados **hoje**, antes de existir a ferramenta.

- **Ao fechar cada sessão de estudo**, o tutor grava uma nota em `70 - Sessões Claude/` no cofre, usando o template "Sessão Claude", com o que aconteceu: como você raciocinou, dúvidas que surgiram, erros e como foram resolvidos, decisões de estrutura de código e links para o diário da lição e os arquivos.
- A nota é **projeção, não evidência**, como o diário. Ela não muda domínio nem a escada de ajuda.
- O diário de lição (`20 - Áreas/Sistema de Estudos/`) continua como está, gravado ao concluir cada lição.
- Você pode acrescentar as suas próprias notas na mesma pasta ou em `50 - Notas Permanentes`.
- Esse material é a primeira fonte que o importador do Ciclo 4 ou 5 vai ler.

## 8. Riscos e decisões em aberto

| Risco ou decisão | Proposta |
|---|---|
| React e TypeScript tomam tempo do Python | Ficam restritos aos Ciclos 10 e 11, com o diagnóstico antes e a ponte dos type hints nos Ciclos 5 a 7. Se faltar tempo, o Ciclo 8 (Selenium) é o candidato a encolher. |
| Fluxo Git atrasa as fatias | A lição 14 é curta (1–2 sessões); depois o fluxo é hábito e cada PR leva minutos. |
| Dados pessoais no portfólio | O repositório público usa só dados de exemplo fictícios; o cofre real e os registros do tutor ficam fora dele (`.gitignore` e caminho configurável). |
| Onde vive o código | **Decidido pelo fluxo de PR:** repositório separado `segundo-cerebro` no GitHub do aluno. Este repositório continua só para o estado do tutor. |
| Selenium continua? | Recomendo manter, como captura de páginas: é pedido em vagas de automação. Alternativa: trocar por folga para o React. |
| Escopo cresce durante a formação | Tudo o que não está em "pronto para o MVP" (seção 3) vai para o backlog. |
