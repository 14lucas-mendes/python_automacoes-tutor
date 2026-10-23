# Formação fechada: especialista em Python, automação e IA

Status: **aprovada pelo aluno em 2026-10-08** e gravada no estado canônico (`state` revisão 208; `study-config.json` com 20 ciclos e 10 h por semana).

**Este é o documento único do plano da formação.** Ele substitui, para decisões futuras:
- [`segundo-cerebro-roadmap.md`](segundo-cerebro-roadmap.md), de 05/10;
- [`bloco-logica-roadmap.md`](bloco-logica-roadmap.md), de 06/10.

Os dois continuam como histórico.

## 1. Objetivo

Tornar-se **especialista em Python, automação e IA aplicada**: LLMs, RAG e agentes integrados a sistemas. Front-end (React + TypeScript), DevOps (Docker, deploy) e segurança entram no nível **suficiente** para construir e publicar um sistema completo.

A amplitude full stack vem da faculdade de Análise e Desenvolvimento de Sistemas, que cobre front, back, DevOps, segurança, engenharia de software e IA. Esta formação dá a **profundidade**. É o formato em T: profundo numa área, largo o bastante para entregar o sistema inteiro.

## 2. Por que este formato (levantamento de vagas de 08/10/2026)

Foram lidas 10 descrições completas de vagas no LinkedIn público, mais os títulos das buscas "full stack júnior" (25) e "Python júnior" (20). A amostra é pequena: serve como tendência, não como estatística.

| Sinal | Achado |
|---|---|
| Git, code review, PR | quase todas |
| Banco relacional (PostgreSQL o mais citado) | maioria |
| Criar e consumir APIs, integrar sistemas | maioria |
| React + TypeScript | front mais comum nas vagas full stack |
| Docker, CI/CD, cloud | 4 de 10; obrigatório em 1 |
| IA aplicada (LLM, RAG, agentes) | 3 de 10 |
| Lógica de programação | explícita nas vagas de entrada |

- O back-end do full stack júnior é, na maioria, Node, Java ou .NET. Nenhum dos 25 títulos cita Python.
- **Python aparece forte em automação, integração, IA e dados.** É essa a ponta da especialização.
- Uma das vagas (MRM) pede para "entender e validar o código produzido" pela IA. É o diferencial que esta formação treina.

Fontes:
- [LinkedIn: full stack júnior](https://br.linkedin.com/jobs/desenvolvedor-full-stack-junior-vagas)
- [LinkedIn: Python júnior](https://br.linkedin.com/jobs/desenvolvedor-python-junior-vagas)
- [AutoU](https://br.linkedin.com/jobs/view/desenvolvedor-fullstack-trainee-j%C3%BAnior-at-autou-4476935830)
- [SPL Engenharia](https://br.linkedin.com/jobs/view/desenvolvedor-fullstack-i-at-spl-engenharia-4470549817)
- [Jobbol/On Smart](https://br.linkedin.com/jobs/view/analista-full-stack-j%C3%BAnior-at-jobbol-4470605646)
- [Smartspace](https://br.linkedin.com/jobs/view/pessoa-desenvolvedora-software-j%C3%BAnior-at-smartspace-4472917380)
- [Eletropoll](https://br.linkedin.com/jobs/view/desenvolvedor-full-stack-jr-at-grupo-eletropoll-4469995466)
- [ISA Saúde](https://br.linkedin.com/jobs/view/desenvolvedor-junior-at-isa-sa%C3%BAde-4462557267)
- [MRM](https://br.linkedin.com/jobs/view/desenvolvedor-fullstack-jr-at-mrm-brasil-4456519685)
- [Grupo SFA](https://br.linkedin.com/jobs/view/desenvolvedor-full-stack-junior-bh-at-grupo-sfa-4471208825)
- [Itaú](https://br.linkedin.com/jobs/view/engenharia-de-software-j%C3%BAnior-python-aws-comunidade-finan%C3%A7as-at-ita%C3%BA-unibanco-4474374423)
- [Accenture](https://br.linkedin.com/jobs/view/assistente-de-desenvolvimento-python-e-angular-exclusiva-pcd-h%C3%ADbrido-at-accenture-brasil-4444910132)

## 3. O projeto: o app da formação

O repositório `segundo-cerebro` passa a ser **o app da própria formação**, construído sobre a skill `ai-tutor`. O aluno estuda dentro do app, e uma aba **Segundo Cérebro** responde perguntas sobre tudo o que a formação registrou. A base de dados é o próprio estudo. Não há Obsidian nem outra ferramenta externa como fonte.

### Regras de negócio do MVP

1. **Os JSON canônicos do estudo são a fonte da verdade.** O PostgreSQL é uma cópia de leitura, recarregada inteira pelo importador, sem sincronização incremental.
2. **Uma pessoa e um estudo.** O `study_root` vem da configuração. O repositório público usa um **estudo fictício** gerado com `scripts/init_study.py`; o estudo real só é lido localmente.
3. **O app escreve em um só lugar: o resultado da revisão de card.** São `retrieval_attempts` e o passo do card, gravados pelas funções da skill (`state_io` com `expected_revision` + `validate_study`). O app nunca cria evidência nem altera domínio.
4. **O agente tutor conduz uma atividade: a revisão de card** (`retrieval_first`). Ele só grava depois da confirmação do aluno.
5. **A busca é full-text do PostgreSQL.** A Claude API responde citando o trecho e a origem (sessão, lição ou card). A Anthropic não oferece embeddings próprios, e embeddings exigiriam um segundo provedor; por isso ficam no backlog.
6. **Sem notificação externa.** A tarefa diária gera a lista de cards vencidos, que o app mostra.
7. **A VPS é acessada por túnel SSH**, sem porta pública e sem domínio. Domínio com HTTPS público é extra.
8. **Três telas**, com respostas sem streaming:
   - painel;
   - revisão de cards com o agente;
   - Segundo Cérebro, com busca e pergunta.
9. **Servidor MCP** é extra opcional da `lesson_22`.
10. **Envio externo:** mandar conteúdo do estudo real à Claude API exige consentimento explícito no app. No desenvolvimento, só o estudo fictício.

### MVP pronto

1. Importa o estudo (`.ai-tutor/*.json` + Markdown das lições e do log) para o PostgreSQL.
2. API FastAPI: progresso, lições, sessões, evidências, pontos fracos e cards devidos.
3. Revisão de cards com a escada 1/3/7/16/35/60, gravando pelas funções da skill.
4. Importa PRs e commits do repositório pela API do GitHub e os liga às sessões.
5. Automação:
   - tarefa diária de cards vencidos;
   - captura com Selenium de uma página de documentação, registrada como fonte.
6. IA:
   - saída estruturada com Pydantic;
   - Segundo Cérebro com citação;
   - agente tutor com ferramentas e confirmação humana.
7. React + TS: painel, revisão com o agente e Segundo Cérebro.
8. Entrega:
   - pytest, CI e PR em toda fatia;
   - Docker Compose (db, api, web);
   - deploy na VPS do aluno por túnel SSH;
   - segredos em `.env`.
9. README, demo de 3 a 5 min e só dados fictícios no repositório.

**Backlog depois do MVP:**
- aula completa dentro do app;
- embeddings/pgvector;
- MCP, se não entrar como extra;
- notificação externa;
- domínio e HTTPS público;
- streaming;
- vários alunos;
- mobile.

## 4. Roteiro fechado

20 ciclos, **sem prazo definido** (decisão do aluno, 2026-10-15). O número do ciclo indica só a ordem das lições. O avanço depende só de evidência. Os IDs das lições são estáveis.

Até 2026-10-15 havia ciclos de 21 dias com fim de referência em 24/10/2027. O prazo não estava entre os itens congelados (seção 6) e era só uma referência; por isso foi retirado sem pedido de mudança.

| Fase | Ciclo | Lição | Entrega no app |
|---|---|---|---|
| Fundamentos | 1–4 | `00`, `01`, `03`, `04`, `02` | concluídas |
| Lógica | 5 | `lesson_15-logica-decomposicao` | **cria o repositório**; perguntas sobre o estudo fictício, com plano e `assert` |
| | 6 | `lesson_16-estruturas-dados` | índices: tópico → evidências, lição → sessões |
| | 7 | `lesson_17-algoritmos-debugging` | ordenar e buscar sessões e datas; defeitos plantados |
| Python intermediário | 8 | `lesson_19-python-intermediario` | modelos da formação como dataclasses tipadas, pacote, `pyproject`, logging, exceções próprias |
| Sistema base | 9 | `lesson_14-git-fluxo-profissional` + `lesson_05-sql-memorias` | `main` protegida, `develop`, PR, CI e `v0.1`; PostgreSQL em container (1º Docker) e importador |
| | 10 | `lesson_06-http-apis` | PRs e commits do GitHub |
| | 11 | `lesson_07-fastapi-dados` | API da formação |
| | 12 | `lesson_18-docker-vps-deploy` | compose completo e deploy na VPS; dali em diante, toda fatia é publicada |
| Automação | 13 | `lesson_08-selenium-captura` | tarefa diária e captura de fonte |
| IA aplicada | 14 | `lesson_20-llm-estruturado` | Claude API, saída estruturada, custo, avaliação, injeção de prompt |
| | 15 | `lesson_21-rag-segundo-cerebro` | busca full-text + resposta com citação |
| | 16 | `lesson_22-agente-tutor-mcp` | agente na revisão de card, confirmação humana (MCP extra) |
| Interface suficiente | 17 | `lesson_10-react-typescript-1` | painel e revisão (diagnóstico de React antes) |
| | 18 | `lesson_11-react-typescript-2` | Segundo Cérebro e agente ponta a ponta |
| Qualidade e entrega | 19 | `lesson_12-qualidade-ci` | testes, CI completo, segurança do app |
| | 20 | `lesson_13-portfolio` | README, demo, release, testes técnicos |

- `lesson_09-manutencao-sonhar` foi **arquivada**: nunca teve sessão, e manutenção e "sonhar" saíram do MVP.
- **Tópicos novos**, com domínio 0 e sem herança:
  - `topic_python-intermediario`;
  - `topic_devops-deploy`;
  - `topic_ia-aplicada`.
- **Método do bloco de lógica** (vale em toda a formação):
  - decompor antes de codar: entrada, regra, saída e exemplos com a saída esperada calculada à mão;
  - prever, rodar, investigar, modificar e criar;
  - tabela de rastreio;
  - depois do bloco, um exercício curto de lógica por semana.

- **IA aplicada unificada** (decisão do aluno, 2026-10-23, no fecho da `lesson_15`; ver [`pedido-unificacao-engenharia-ia.md`](pedido-unificacao-engenharia-ia.md), seções 6 e 7):
  - a antiga formação de Engenharia de IA entra **dentro** das lições 20, 21, 22 e 12, sem mudar IDs, ordem, MVP, stack ou carga;
  - `lesson_20`: M01, M02, M03, M10 e M11 (contexto e tokens, chave no backend, prompt como contrato validado, avaliação, injeção tratada no sistema);
  - `lesson_21`: M05 (histórico × resumo × recuperação);
  - `lesson_22`: M04, M06, M07 e M08, com o **núcleo agêntico**: *agent loop* com parada, ferramentas, permissões e confirmação humana, "workflow ou agente?" e avaliação. Orquestração e subagentes entram só como explicação;
  - `lesson_12`: M10 e M11 (eval no CI, segurança);
  - M09 vai para o backlog;
  - limite de escopo: cada módulo entra como capacidade observável que o app usa; evidências e domínio da formação de IA não migram;
  - detalhes no `curriculum.md`, seção "IA aplicada: conteúdo unificado e lente agêntica".

## 5. Carga e orçamento

- **10 h por semana, sem dias fixos.** A meta é semanal e aparece no painel contra o realizado.
- Um ciclo dá cerca de 30 h. Cerca de metade vai para o código do projeto; o resto, para aula, prática, Feynman e cards.
- O MVP enxuto cabe nesse orçamento. **O risco é a carga, não o escopo:** no ritmo de 21/09 a 08/10 (cerca de 2,5 h por semana), nem o MVP enxuto caberia.

## 6. Regra de formação fechada

**Congelado até a `lesson_13-portfolio` ser concluída:**
- tópicos e lições;
- ordem das lições;
- escopo do MVP e regras de negócio;
- stack: Python, FastAPI, PostgreSQL, React + TypeScript, Docker, Claude API;
- carga de 10 h por semana.

**Continua livre:**
- adaptar a aula dentro de cada lição (protocolo adaptativo);
- distribuir as sessões na semana;
- correções que não mudam a estrutura, como erros de registro.

**Pedido de mudança:**
1. O tutor cita esta regra e registra o pedido no `session-log.md`.
2. O pedido não é aplicado na mesma conversa.
3. Só é avaliado no fecho da lição atual, com justificativa escrita.
4. Só é aceito diante de um **bloqueio real**: o estágio exigir outra stack, uma tecnologia ser descontinuada, ou a evidência mostrar que falta um pré-requisito.

É um compromisso que o tutor aplica por padrão. A autoridade final continua sendo do aluno, que pediu este fechamento.

## 7. O que foi preservado

Sessões, evidências, domínios, pontos fracos e lições concluídas. O `topic_python-fundamentos` continua em 80, e o `next_focus` continua `lesson_15-logica-decomposicao`. Os pontos fracos ativos continuam ligados às tarefas do bloco de lógica (`programming_plan.weak_point_exits` da `lesson_15`).

## 8. Continuação prevista: trilha de especialização em agentes

Registrada em 2026-10-23 com a unificação (foco pedido pelo aluno em 19/10). **Não é uma lição nem um ID.** Ela só começa depois que a `lesson_13-portfolio` for concluída e o congelamento acabar. Então vira lições novas, pelo rito normal de currículo.

**Conteúdo previsto,** o que não cabe no MVP:
- orquestração de vários agentes e subagentes;
- arquiteturas de agentes;
- engenharia do loop em profundidade;
- programação agêntica com ferramentas de código;
- MCP com servidor próprio;
- avaliação e melhoria do harness em execução.

**Base:** o agente da `lesson_22` é a primeira versão do próprio harness. A pasta `E:\Lucas\Documents\Faculdade AI\harnnes-engeniring` é o **material de referência**, sem domínio nem evidência a migrar.

**Por que não antes:** um agente é um programa que chama APIs, guarda estado, usa ferramentas e precisa ser testado e publicado. Os ciclos 8 a 13 dão essa base.
