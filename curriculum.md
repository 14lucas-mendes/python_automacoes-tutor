# Formação fechada: especialista em Python, automação e IA

> **Formação fechada em 2026-10-08.** Plano único: `docs/compose/spec/formacao-fechada.md`. Tópicos, lições, ordem, escopo do MVP, stack e carga estão congelados até a `lesson_13-portfolio` ser concluída. As regras de pedido de mudança estão no `AGENTS.md`.

## Objetivo profissional

Tornar-se **especialista em Python, automação e IA aplicada**: LLMs, RAG e agentes integrados a sistemas. Front-end (React + TypeScript), DevOps (Docker, deploy) e segurança entram no nível suficiente para construir e publicar um sistema completo.

A amplitude full stack vem da faculdade de ADS. Esta formação dá a profundidade, com autonomia real de programação e uso de IA sem dependência de vibe coding.

**Carga:** 10 h por semana, sem dias fixos. A meta é semanal e aparece no painel.

## Sem prazo definido

Início: **2026-08-31**, a primeira sessão (canônico em `study-config.json`: `program_start_date`).

**Decisão do aluno (2026-10-15):** a formação não tem prazo para terminar. O antigo fim de referência (24/10/2027) e as janelas de 21 dias de cada ciclo foram retirados. O número do ciclo na tabela abaixo indica só a **ordem** das lições. O avanço depende de evidência, e a carga de 10 h por semana continua congelada.

## Regra de avanço e uso de IA

Uma competência só avança com evidência demonstrada: explicação autônoma, implementação de uma variação e diagnóstico de um erro relacionado. A IA atua primeiro como tutora: pergunta, oferece pistas, explica, conduz debugging e revisa código. Implementação central fornecida antes da tentativa é prática guiada, não evidência autônoma.

## Ciclos e lições

| Fase | Ciclo | Lição canônica | Marco observável (entrega no app) |
|---|---|---|---|
| Fundamentos | 1 | `lesson_00-diagnostico`, `lesson_01-python-core` | Ambiente profissional e Python core com testes. Concluídos. |
| | 2 | `lesson_03-testes-git` | Debugging sistemático. Concluído em 2026-09-12. |
| | 3 | `lesson_04-descoberta-processo` | Git e GitHub com preflight reconstruído sem comandos. Concluído em 2026-09-17. |
| | 4 | `lesson_02-arquivos-erros` | Arquivos, CSV, JSON e exceções. Concluído em 2026-10-06 (`evidence_lesson02-readme-01`). |
| Lógica | 5 | `lesson_15-logica-decomposicao` | **Cria o repositório `segundo-cerebro`.** Perguntas sobre o estudo fictício (cards vencidos, evidências por tópico), com plano escrito, saída esperada à mão e `assert`. |
| | 6 | `lesson_16-estruturas-dados` | Índices do estudo: tópico → evidências, lição → sessões; estrutura justificada; casos-limite tratados. |
| | 7 | `lesson_17-algoritmos-debugging` | Ordenar e buscar sessões e datas; busca binária e ordenação testadas; defeitos diagnosticados com hipótese. |
| Python intermediário | 8 | `lesson_19-python-intermediario` | Modelos da formação como dataclasses tipadas, pacote com `pyproject`, logging e exceções próprias. |
| Sistema base | 9 | `lesson_14-git-fluxo-profissional` + `lesson_05-sql-memorias` | `main` protegida, `develop`, PR, CI mínimo e `v0.1`. PostgreSQL num container (1º Docker) e importador do estudo. |
| | 10 | `lesson_06-http-apis` | PRs e commits do GitHub importados e ligados às sessões; timeout, erros e paginação tratados. |
| | 11 | `lesson_07-fastapi-dados` | API da formação com modelos Pydantic; a única escrita é a revisão de card, pelas funções da skill. |
| | 12 | `lesson_18-docker-vps-deploy` | Compose completo (db, api, web), `.env`, deploy na VPS por túnel SSH; daí em diante toda fatia é publicada. |
| Automação | 13 | `lesson_08-selenium-captura` | Tarefa diária de cards vencidos e captura de fonte com Selenium, com falha diagnosticada. |
| IA aplicada | 14 | `lesson_20-llm-estruturado` | Claude API com saída estruturada, custo e tokens medidos, avaliação com casos esperados, injeção de prompt tratada. |
| | 15 | `lesson_21-rag-segundo-cerebro` | Busca full-text no PostgreSQL e resposta com citação verificável. |
| | 16 | `lesson_22-agente-tutor-mcp` | Agente tutor com ferramentas na revisão de card e confirmação humana (MCP como extra opcional). |
| Interface suficiente | 17 | `lesson_10-react-typescript-1` | Diagnóstico de React antes; painel e revisão em React + TS. |
| | 18 | `lesson_11-react-typescript-2` | Aba Segundo Cérebro e revisão com o agente, ponta a ponta. |
| Qualidade e entrega | 19 | `lesson_12-qualidade-ci` | Testes, CI com lint, tipos e build do front; segurança do app. |
| | 20 | `lesson_13-portfolio` | README, demo de 3 a 5 min, release do MVP e simulações de teste técnico. |

Notas:
- A partir da `lesson_14`, toda fatia entra por feature branch e PR para `develop`. No fim de cada ciclo, um PR de `develop` para `main` publica uma release com tag.
- `lesson_09-manutencao-sonhar` foi **arquivada** em 2026-10-08. Ela nunca teve sessão.
- `lesson_15-logica-decomposicao` foi **concluída** em 2026-10-23, com `topic_logica-algoritmos` em 80. A próxima é a `lesson_16-estruturas-dados`.

## IA aplicada: conteúdo unificado e lente agêntica (decisão do aluno, 2026-10-23)

Depois do pedido de unificação aceito no fecho da `lesson_15` (`docs/compose/spec/pedido-unificacao-engenharia-ia.md`), a antiga formação de Engenharia de IA deixou de existir em paralelo. O conteúdo dela entra **dentro das lições existentes**.

**O que não muda:** os IDs, a ordem, o MVP, a stack (só Claude API) e a carga. Esta seção só adapta a aula dentro de cada lição.

**Limite de escopo:** cada módulo entra como a **capacidade observável** que o app usa, com checkpoint e Feynman dentro da lição. O que não couber vai para o backlog. Evidências e domínio da formação de IA **não migram**.

| Lição | Módulos da antiga formação de IA | Como entram |
|---|---|---|
| `lesson_20-llm-estruturado` | M01, M02, M03, M10, M11 | Chamada sem estado e histórico reenviado; janela de contexto e custo em tokens; a chave só no backend (`.env`); prompt como contrato de saída validado com Pydantic e fallback no código; casos esperados e comparação de versões; injeção de prompt tratada no sistema. |
| `lesson_21-rag-segundo-cerebro` | M05 | Comparar histórico, resumo e recuperação antes da busca full-text com citação. Contexto e memória como peças do harness. |
| `lesson_22-agente-tutor-mcp` | M04, M06, M07, M08 | **Núcleo agêntico** (detalhado abaixo). |
| `lesson_12-qualidade-ci` | M10, M11 | Eval do LLM rodando no CI e segurança do app. |
| backlog | M09 | IDEs, CLIs e modelos locais, depois do MVP. |

**Núcleo agêntico da `lesson_22`:**
- o *agent loop* com condição de parada;
- o desenho de ferramentas e o ciclo `tool_use → aplicação executa → tool_result`;
- permissões e confirmação humana;
- "workflow ou agente?": o caminho é conhecido de antemão?
- a arquitetura e a avaliação do agente da revisão de card;
- conceitos de MCP (host, client e server; MCP × skill × plugin);
- orquestração e subagentes **só como explicação**, porque a regra 9 do MVP os deixa fora.

**Lente das três lições:** o modelo recebe tokens e devolve tokens; o resto é harness. Em cada entrega, o aluno classifica o que é do modelo e o que é do código.

**Depois da `lesson_13`:** uma trilha de especialização em agentes, registrada como continuação prevista na seção 8 do `formacao-fechada.md`. A pasta `harnnes-engeniring` é o material de referência dela.

## Projeto principal: o app da formação

`project_segundo-cerebro` é o **app da própria formação**, construído sobre a skill `ai-tutor`. O aluno estuda dentro do app (painel e revisão de cards com um agente tutor), e a aba **Segundo Cérebro** responde perguntas sobre o que a formação registrou, citando a origem.

- **Stack:** Python, FastAPI, PostgreSQL, Claude API, React + TypeScript, Docker e VPS.
- **Regras de negócio do MVP:**
  - os JSON do estudo são a verdade, e o banco é uma cópia de leitura;
  - uma pessoa e um estudo;
  - o app só escreve o resultado da revisão de card, pelas funções da skill, e nunca evidência ou domínio;
  - busca full-text com resposta citada;
  - sem notificação externa;
  - VPS por túnel SSH;
  - três telas.
- **Dados:** o repositório público usa só um estudo fictício. O estudo real só é lido localmente, e enviá-lo à Claude API exige consentimento.

Detalhes, backlog e o levantamento de vagas que embasou o formato estão em `docs/compose/spec/formacao-fechada.md`.

Projetos anteriores arquivados, sem perda de histórico:
- `project_automacao-processo-real` e `project_api-llm-servico`, absorvidos em 2026-10-05;
- `project_agente-operacional` e `project_capstone-producao`, absorvidos em 2026-10-08: agentes, Docker e deploy agora fazem parte do núcleo.

## Estado no fechamento (2026-10-08)

- **Domínio 80:**
  - `topic_python-fundamentos`;
  - `topic_workflow-profissional`;
  - `topic_automacao-confiavel`.
- **Domínio 0:** todos os demais, incluindo os novos `topic_python-intermediario`, `topic_devops-deploy` e `topic_ia-aplicada`.
- **Diagnóstico de lógica:** concluído em 2026-10-08 (`partial`, confiança `medium`). A `lesson_15` começa por:
  - saída esperada em números e `assert`;
  - tabela de rastreio montada pelo aluno;
  - dicionário com chave nova.
- **Pontos fracos ativos (6):**
  - lista literal em testes;
  - modelo de dois tempos dos erros;
  - forma exata de comandos Git;
  - caminho relativo;
  - ordem e guarda de condicionais;
  - verificação com valor esperado.

  Os três primeiros de lógica estão ligados às tarefas da `lesson_15`.
- **Próxima lição:** `lesson_15-logica-decomposicao`.
- **Histórico de revisões de roteiro:**
  - 2026-10-05: Segundo Cérebro como projeto (`segundo-cerebro-roadmap.md`);
  - 2026-10-06: bloco de lógica (`bloco-logica-roadmap.md`);
  - 2026-10-08: formação fechada (`formacao-fechada.md`);
  - 2026-10-23: Engenharia de IA unificada dentro das lições 20, 21, 22 e 12, com lente agêntica (`pedido-unificacao-engenharia-ia.md`).

<!-- IDs, evidências, sessões e critérios canônicos estão em .ai-tutor/state.json. -->
