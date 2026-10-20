# Pedido de mudança: unificar a formação de Engenharia de IA nesta formação

Status: **registrado em 2026-10-15, aguardando avaliação no fecho da `lesson_15-logica-decomposicao`.**

Este documento segue a regra de formação fechada ([`formacao-fechada.md`](formacao-fechada.md), seção 6, e `AGENTS.md`): o pedido é registrado agora, **não é aplicado nesta conversa** e só é avaliado no fecho da lição atual, com justificativa escrita.

## 1. O pedido

O aluno tem três formações em aberto: Python (este repositório), Engenharia de IA (`14lucas-mendes/fundamentos-engenharia-ia`) e Claude Code. Ele quer **uma formação só**, em paralelo com a faculdade de ADS, estudada em etapas e sem prazo.

- **Python + Engenharia de IA:** unificar neste repositório.
- **Claude Code:** fica de fora por enquanto (decisão do aluno, 2026-10-15).
- **Product engineer:** ficou para outro momento. O alvo continua sendo Python, automação e IA aplicada.

## 2. Situação dos dois repositórios em 2026-10-15

| | `python_automacoes-tutor` | `fundamentos-engenharia-ia` |
|---|---|---|
| Estado | revisão 248 (a sessão de 13/10 ainda não foi commitada); 3 tópicos com domínio 80 | M01 em 20; demais tópicos em 0 |
| Última sessão | 2026-10-13 (`lesson_15`, interrompida e retomável) | 2026-10-03 (M01, interrompida) |
| Ritmo real recente | cerca de 6,4 h na semana de 09 a 13/10 | nenhuma sessão desde 03/10 |
| Carga planejada | 10 h/semana | 3 h/semana |
| API de LLM | Claude API (stack congelada) | OpenAI |
| Projeto | app `segundo-cerebro` | exercícios por módulo + capstone |
| Pendências locais | — | 4 arquivos não commitados (estado, perfil, lição M01, log de 03/10) |

**Sobreposição.** O currículo da formação de IA diz que esta formação "deixa IA, agentes e MCP fora do núcleo". Isso ficou desatualizado em 2026-10-08: desde o fechamento, as lições 20, 21 e 22 cobrem saída estruturada, avaliação, injeção de prompt, RAG e agente com ferramentas. Cerca de metade dos módulos da formação de IA duplica essas lições.

## 3. Proposta

### 3.1 Repositório único

Este repositório passa a ser o único programa de estudo. `fundamentos-engenharia-ia` é **arquivado** (README de arquivamento + repositório marcado como arquivado no GitHub). Nada é apagado.

### 3.2 Mapeamento módulo → lição

Os módulos entram como **aprofundamento dentro das lições existentes**. Não há lição nova, troca de ordem, mudança de stack nem mudança no escopo do MVP.

**Limite de escopo:** cada módulo entra só como a **capacidade observável** que o app usa — um checkpoint com Feynman dentro da lição —, não como módulo inteiro. A formação de IA previa cerca de 70 h (22 a 26 semanas a 3 h); as lições 20 a 22 têm cerca de 45 h para aula e prática fora do código do app. O que não couber vai para o backlog.

| Módulo da formação de IA | Entra em | Como |
|---|---|---|
| M01 · Modelos, tokens, contexto e reasoning | `lesson_20-llm-estruturado` | abertura da lição: chamada stateless, histórico reenviado, janela de contexto, custo em tokens (a lição já mede tokens e custo) |
| M02 · Arquitetura de aplicações com IA | `lesson_20-llm-estruturado` | onde a chave mora (`.env`, só no backend) e o que é do modelo × do código, aplicado à API FastAPI do app |
| M03 · Prompts como interface de engenharia | `lesson_20-llm-estruturado` | prompt como contrato de saída, validado com Pydantic, com fallback no código |
| M11 · Avaliação de soluções com IA | `lesson_20-llm-estruturado` e `lesson_12-qualidade-ci` | casos esperados e comparação de versões na 20; eval rodando no CI na 12 |
| M05 · Memória, contexto e estado (inclui RAG) | `lesson_21-rag-segundo-cerebro` | comparação histórico × resumo × recuperação antes da busca full-text com citação |
| M04 · Tools e function calling | `lesson_22-agente-tutor-mcp` | ciclo `tool_use → aplicação executa → tool_result` no agente da revisão de card |
| M07 · Assistentes, automações e workflows | `lesson_22-agente-tutor-mcp` | critério "o caminho é conhecido de antemão?" para justificar agente × workflow; a tarefa diária da `lesson_08` serve de contraexemplo |
| M08 · Agentes e subagentes | `lesson_22-agente-tutor-mcp` | agent loop com condição de parada; subagentes só como explicação (fora do MVP) |
| M06 · MCP, skills, plugins e integrações | `lesson_22-agente-tutor-mcp` | conceito (host, client, server; MCP × skill × plugin). Construir o servidor continua **extra opcional**, como já está na regra 9 do MVP |
| M10 · Segurança no harness e prompt injection | `lesson_20` e `lesson_12-qualidade-ci` | injeção tratada no sistema, não no prompt (a 20 já pede isso); confirmação humana na 22; segurança do app na 12 |
| M09 · IDEs, CLIs, modelos locais | backlog | extra depois do MVP (comparar um modelo local com a Claude API) |

O ponto fraco da formação de IA `weak_01ebbe5b…` (fronteira modelo × sistema) **não é importado** para o estado deste estudo. Ele vira um critério escrito no plano das lições 20 a 22 — em cada entrega, o aluno classifica o que é do modelo e o que é do código — e só vira ponto fraco aqui se reaparecer em evidência.

### 3.3 Evidências e domínio

- As 4 evidências do M01 (guiadas ou parciais, domínio 20) ficam **como histórico** no repositório arquivado.
- **Não migram** como domínio nem como evidência deste estudo, para não contar a mesma coisa duas vezes.
- O script `conversa.py` e as notas da `lesson_m01` podem ser reaproveitados como **material** da abertura da `lesson_20`.
- Das fontes de `.ai-tutor/sources.json` da formação de IA, copiar para este estudo, ao abrir a `lesson_20`, só as da Anthropic ou independentes de provedor (contexto, tools, MCP, evals, OWASP LLM). A `source_openai_structured` fica de fora.

### 3.4 Carga

A soma planejada era 10 h + 3 h por semana. Com a unificação, fica uma meta só, as 10 h já congeladas. Desde 2026-10-15 a formação não tem prazo definido (decisão do aluno, aplicada à parte, porque o prazo não era item congelado). O avanço continua dependendo de evidência.

## 4. Avaliação no fecho da `lesson_15` (para o tutor)

A regra lista três bloqueios reais. Este pedido não é exatamente nenhum deles; a justificativa é outra e precisa ser pesada no fecho:

1. **O que muda nesta formação:** só o conteúdo dentro das lições 20, 21, 22 e 12, que a regra já deixa livre ("adaptar a aula dentro de cada lição"). Tópicos, ordem, MVP, stack e carga ficam iguais.
2. **O que muda de verdade:** uma formação paralela deixa de existir. Isso reduz duplicação e carga, que o próprio plano aponta como o maior risco ("o risco é a carga, não o escopo").
3. **Autoridade:** a decisão final é do aluno, que pediu o fechamento e agora pede a unificação.

**Parecer prévio do tutor (2026-10-15):** recomendar **aceitar**, com o limite de escopo da seção 3.2.
- A favor: na prática, a formação de IA já está parada; a sobreposição é real; a stack fica com uma API só; nada congelado muda.
- Riscos: excesso de conteúdo nas lições 20 a 22 (tratado pelo limite de escopo) e perder o histórico do repositório de IA se ele for arquivado com mudanças não commitadas.
- Esperar o fecho custa zero: a `lesson_20` é o ciclo 14, ainda distante.

Se aceito, aplicar nesta ordem:

1. Escrever aqui a justificativa da decisão e mudar o status.
2. Atualizar `curriculum.md` e `formacao-fechada.md` com o mapeamento da seção 3.2 (sem tocar nos IDs das lições, na ordem ou no MVP).
3. Registrar a decisão no `session-log.md` e no `AGENTS.md`.
4. No repositório de IA:
   1. commitar as 4 mudanças pendentes;
   2. rodar o `validate_study` lá e anotar o resultado;
   3. commitar o README de arquivamento;
   4. marcar o repositório como arquivado no GitHub (pelo aluno, ou pelo tutor com `gh repo archive` só com confirmação explícita).
5. Rodar `validate_study` neste estudo.

## 4.1 Complemento do aluno (2026-10-19): foco em agentes

Nas palavras do aluno: "quero que a minha formação de engenharia de IA foque em agentes, engenharia de loop, programação agêntica e harness engineering, orquestração de agentes, arquitetura de agentes de IA e coisas relacionadas."

**Achado relacionado:** existe uma quarta formação, parada, em `E:\Lucas\Documents\Faculdade AI\harnnes-engeniring`, chamada "Harness Engineering para agentes de IA".
- Ela foi criada em 21 e 22/09, tem 4 fases e meta de até 2 h por semana.
- Não tem nenhuma sessão nem evidência, e a pasta não é repositório Git.
- O currículo dela cobre exatamente esse foco: anatomia do harness, modelo × harness, desenho, primeira versão própria, avaliação e melhoria.

**Avaliação do tutor (prévia, para o fecho da `lesson_15`).** O foco cabe em duas camadas, sem mexer no que está congelado.

1. **Dentro da formação fechada (lições 20 a 22), como lente das aulas.** Adaptar a aula dentro da lição é livre.
   - **`lesson_20`:** o modelo recebe tokens e devolve tokens; todo o resto é harness. A fronteira entre modelo e sistema é o critério transversal, junto com saída estruturada, avaliação e injeção de prompt tratadas no sistema.
   - **`lesson_21`:** contexto e memória como peças do harness, com recuperação e citação.
   - **`lesson_22`:** o núcleo agêntico.
     - o *agent loop* com condição de parada;
     - o desenho de ferramentas e o ciclo `tool_use → aplicação executa → tool_result`;
     - permissões e confirmação humana;
     - a pergunta "workflow ou agente?";
     - a arquitetura do agente da revisão de card;
     - avaliação do agente;
     - orquestração e subagentes **só como explicação**, porque a regra 9 do MVP deixa isso fora.
   - A primeira versão do **próprio harness**, a fase 3 do currículo de harness, é o agente da `lesson_22`.
2. **Depois da `lesson_13`, quando o congelamento acaba: uma trilha de especialização em agentes.**
   - Ela reúne o que não cabe no MVP: orquestração de vários agentes e subagentes, arquiteturas de agentes, engenharia do loop em profundidade, MCP com servidor próprio, avaliação e melhoria do harness em execução (a fase 4 do currículo de harness) e programação agêntica com ferramentas de código.
   - Abrir essa trilha antes do fim exigiria lição nova, o que é mudança estrutural. Pela regra, isso não se justifica sem um bloqueio real.

**Por que não antecipar:** um agente é um programa que chama APIs, guarda estado, usa ferramentas e precisa ser testado e publicado. Sem a base dos ciclos 8 a 12 (Python intermediário, SQL, HTTP, FastAPI e deploy), o harness vira só teoria. A ordem atual prepara o terreno para esse foco.

**Se aceito no fecho da `lesson_15`, somar ao roteiro da seção 4:**
1. escrever a lente agêntica nas lições 20 a 22 do `curriculum.md` e do `formacao-fechada.md`;
2. registrar a trilha pós-MVP de agentes como continuação prevista, e não como lição nova antes da `lesson_13`;
3. tratar a pasta `harnnes-engeniring` como **material de referência** da trilha, sem domínio nem evidência a migrar, e arquivá-la junto com `fundamentos-engenharia-ia`.

## 5. Estágio no TI da CPTM

O estágio ainda não começou e a stack não é conhecida (o aluno acredita que seja JavaScript). Se for confirmada, é um bloqueio real previsto pela regra ("o estágio exigir outra stack"). O caminho natural seria antecipar o bloco de React + TypeScript (`lesson_10` e `lesson_11`). Isso é um **pedido separado**, a ser aberto só depois que a stack for confirmada.
