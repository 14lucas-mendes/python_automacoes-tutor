# Registro de sessões

<!-- Projeção legível mantida à mão. Desde a skill bd567cd, `python -m scripts.projections`
     preserva este arquivo (não tem marca de gerado) e só atualiza o flashcards.md.
     Nunca usar `--force` neste estudo: substituiria esta narrativa por um resumo mecânico. -->

## `session_2026-10-24-lesson16-teoria-01`

- Status: concluída (12:30–13:32, ~62 min de 60 informados pelo aluno). Skill `e87e2d7`, `theory_first`.
- Lição: `lesson_16-estruturas-dados`, aberta hoje (tema novo: teoria completa antes da prática).
- **Cards (retrieval_first), 5 vencidos:**
  - `reader-tipos-01`: correto ("não converte"). Volta em 27/10.
  - `dictreader-fieldnames-02`: não lembrou. Explicado `fieldnames` e `None` no arquivo vazio. Volta em 25/10.
  - `next-default-01`: parcial. Acertou `StopIteration`, mas achava que o `next` "pega tudo depois do cabeçalho" e não disse o valor padrão. Volta em 25/10.
  - `fatiar-pop-01`: parcial. Índices e remoção certos; faltou "fatia é cópia nova, `pop` muda a original e devolve o item". Volta em 25/10.
  - `print-return-01`: correto (chamou `print` de método: detalhe de precisão). Volta em 27/10.
- **Teoria escrita** em [`lessons/16-estruturas-dados.md`](lessons/16-estruturas-dados.md):
  - parte 1: lista, dicionário, tupla e conjunto (tupla e conjunto novos nesta formação), quatro perguntas para escolher, custo de achar, exemplo da biblioteca e dados aninhados de ônibus;
  - parte 2: acumular, contar, agrupar, filtrar, buscar, maior/menor e a regra de empate.
- **Checagens** (não são evidência): ver o Progresso da lição. Ponto de atenção: no `len` do conjunto, o número saiu certo por raciocínio errado; a variação mostrou o modelo correto depois da explicação.
- **Evidência:** nenhuma. Domínio inalterado (`topic_logica-algoritmos` segue 80, da `lesson_15`).
- **Learner profile:** 1 observação (`strategy_outcome`) sobre a checagem com resultado coincidente.
- **Próximo passo:** recuperação curta da teoria e o Índice 1 (tópico → evidências) só com o enunciado. O pedido de unificar Claude Code e Harness continua para o fecho da `lesson_16`.

## Mídia de revisão da `lesson_15` — 2026-10-23

- Fora de sessão, a pedido do aluno. Ele escolheu dois formatos: mapa Excalidraw e pacote NotebookLM.
- **Novo pacote:** `media/lesson_15-logica-decomposicao/notebooklm` (`media_78a0dc9f…`, `prepared`).
  - **Material principal:** `revisao-lesson15.excalidraw`, com prévia SVG escura. São 6 colunas, cada uma ligando a etapa ao conceito, à dificuldade (com data) e à solução, mais a linha do tempo do domínio e uma pergunta de recuperação.
  - **Material complementar:** `audio-script.md`, o roteiro e o texto de apoio do Resumo em áudio do NotebookLM.
  - **Fontes:** 5 páginas da documentação oficial do Python, mais o registro da lição (`study_lesson15-percurso`).
- O pacote de 11/10 foi para `notebooklm-2026-10-11`, e o `local_path` no `media-index` foi corrigido.
- **Envio ao NotebookLM,** com o consentimento do aluno dado no momento: "Consinto em enviar ao NotebookLM o source-pack.md e o prompts.md do pacote da lesson_15".
  - Feito pelo navegador próprio do app. O login foi do aluno, que passou por uma verificação de selfie em outro aparelho.
  - Notebook "lesson_15 · revisão". O `source-pack.md` foi colado como fonte do tipo texto (6270 caracteres), e o `prompts.md` foi para o campo de foco do áudio.
- **Áudio gerado e observado:** "A armadilha do código silencioso no Python", formato Deep Dive, 20 min 46 s, status `generated`.
  - O conteúdo **não foi conferido pelo tutor**: não há transcrição, e o tutor não ouve áudio. O aluno ouve e aponta o que não bater.
  - O arquivo não foi baixado.
- `media-index` 14 → 16; `validate_study`: PASS. Mídia não é evidência.

## Pedido de mudança: unificar Claude Code e Harness Engineering — 2026-10-23

- Fora de sessão. O aluno pediu: "eu quero unificar todas as formações que eu tenho numa só. Então, inclua a do Claude Code e inclua também a do Harness Engineer."
- **Regra citada:** formação fechada (`AGENTS.md` e `formacao-fechada.md`, seção 6). O pedido foi **registrado e não aplicado** nesta conversa. Ele será avaliado no fecho da `lesson_16-estruturas-dados`, com justificativa escrita.
- **Achados:**
  - `formacao-claude` tem 26 tópicos em 0, sem lições nem evidências, e 1 sessão interrompida desde 09/10;
  - `harnnes-engeniring` não tem sessões;
  - há sobreposição com as lições 12, 14, 17 e 20 a 22 e com a trilha de agentes.
- Detalhes em [`docs/compose/spec/pedido-unificacao-claude-code-harness.md`](docs/compose/spec/pedido-unificacao-claude-code-harness.md).

## Unificação aceita e aplicada — 2026-10-23

- O aluno confirmou: "Confirmo a unificação como recomendada. Pode aplicar os passos da seção 6.4 (o arquivamento no GitHub eu faço)."
- **Aplicado:**
  - pedido com status **aceito**, e a aplicação descrita na seção 7;
  - `curriculum.md` com a seção "IA aplicada: conteúdo unificado e lente agêntica";
  - `formacao-fechada.md` com o mapeamento na seção 4 e a seção 8, "trilha de especialização em agentes", prevista para depois da `lesson_13`;
  - `AGENTS.md` com a seção "Engenharia de IA unificada";
  - README de arquivamento no `fundamentos-engenharia-ia`;
  - nota de referência na pasta `harnnes-engeniring`.
- **Não mudou:** estado canônico, IDs, ordem das lições, MVP, stack e carga. Nenhuma evidência ou domínio migrou.
- **Pendente, com o aluno:** arquivar `14lucas-mendes/fundamentos-engenharia-ia` no GitHub.

## Avaliação do pedido de unificação no fecho da `lesson_15` — 2026-10-23

- Fora de sessão, a pedido do aluno, como prevê a regra de formação fechada (seção 6 do `formacao-fechada.md`). Não é sessão de aprendizagem.
- **Fatos conferidos:**
  - `fundamentos-engenharia-ia` está parado desde 08/10, limpo, com `validate_study` PASS e M01 em 20;
  - `harnnes-engeniring` não tem sessão nem Git.
- **Avaliação:** o pedido não é nenhum dos três bloqueios reais da regra. Mesmo assim, **não toca nenhum item congelado**: lições, ordem, MVP, stack e carga ficam iguais. Tudo o que muda está na parte livre ("adaptar a aula dentro de cada lição") ou fora desta formação.
- **Recomendação do tutor: aceitar, com limites.**
  - Os módulos entram como capacidade observável nas lições 20, 21, 22 e 12, sem migrar evidência.
  - A lente agêntica entra nas lições 20 a 22, com a `lesson_22` como núcleo.
  - A trilha de agentes fica registrada como continuação prevista depois da `lesson_13`, sem lição nova agora.
  - A seção 5 (estágio) continua como pedido separado.
- **Aplicação:** espera a confirmação do aluno. A justificativa completa e a ordem dos passos estão na seção 6 de [`docs/compose/spec/pedido-unificacao-engenharia-ia.md`](docs/compose/spec/pedido-unificacao-engenharia-ia.md).

## `session_2026-10-22-lesson15-transferencia-01` (retomada em 23/10) — lição concluída

- Status: **concluída**. Retomada em 23/10 das 14:15 às 15:45 (cerca de 90 min). Skill em uso: commit `e87e2d7`, com os critérios congelados até a `lesson_17`.
  - `state` 289 → 305, `cards` 55 → 60, `learner-profile` 23 → 24.
- **Cards:** `cond-01` ✅, `fieldnames-01` ❌, `main-guard-01` ✅, `restkey-01` ❌ e `git-diff-staged-01` 🟡. Os três últimos voltam em 24/10.
- **v2 guiada do `classificar_ordens.py`:** os 7 itens do checklist estão feitos e todas as previsões saíram certas. Também ficou registrado `evidence_logica-previsao-ordens-v2-01`, de apoio.
  - O aluno fez sozinho o commit `4f2e3b1` no `formacao-python` (`add .` → `status` → `commit` → `log --oneline -1`). O push está pendente.
- **Tarefa 2 da transferência, "filas do fim de turno":** tarefa diferente no mesmo contexto, pela skill `e87e2d7`. Modo avaliação, só com o enunciado (`contar_filas.py`, `b92c9bd1…`).
  - **Entrega completa:**
    - decomposição com a ordem das verificações justificada;
    - 5 exemplos, sendo 4 casos-limite;
    - `assert` dentro do `__main__`;
    - previsão certa;
    - tabela à mão conferida pelo `print` no laço.
  - **Pergunta neutra sobre ajuda,** feita porque o estilo mudou e porque `continue`, `break`, a variável de sinal e o parâmetro padrão nunca foram ensinados aqui: "fiz consultando a documentação, o continue e break foram pesquisas adicionais. Não tive ajuda". Vale o que o aluno declarou.
  - Registrado em `evidence_logica-transferencia-filas-01`: **transferência autônoma e correta**.
- **Domínio (regra 9):** `topic_logica-algoritmos` subiu de **60 para 80**.
  - ✅ Feynman autônomo (13/10).
  - ✅ Aplicação padrão (20/10).
  - ✅ Transferência (23/10).
- **`lesson_15` concluída**, com o diário gravado no cofre. `next_focus` passou a ser `lesson_16-estruturas-dados`.
- **Pontos fracos resolvidos:** `weak_condicionais-ordem-guarda` e `weak_verificacao-valor-esperado`.
- **Learner profile:** uma observação, `autonomous_attempt` correta.
- **Próximo passo:**
  1. avaliar o pedido de unificação, previsto para o fecho da `lesson_15`, com justificativa escrita;
  2. abrir a `lesson_16`, começando pela teoria completa.

## Alinhamento com a skill `e87e2d7`: conferência completa e `lesson_15` — 2026-10-22

- Fora de sessão, a pedido do aluno ("pegue as atualizações... e atualize a formação"). Não é sessão de aprendizagem: nenhuma evidência, domínio, card ou ponto fraco mudou.
- **Skill:**
  - o `git fetch` não trouxe nada novo: `main` = `origin/main` = **`e87e2d7`** (PR [14lucas-mendes/ai-tutor-skill#5](https://github.com/14lucas-mendes/ai-tutor-skill/pull/5)), já instalada às 19:04;
  - na skill: `unittest` com 147 testes OK e `validate_skill` PASS; no estudo, `validate_study` PASS.
- **Clone `E:\Lucas\Documents\ai-tutor-plugin`, não adotado:**
  - branch `feat/mcp-plugin`, com 79 arquivos alterados sem commit, de 20/10;
  - a base é `d9605d4`, anterior à `e87e2d7`;
  - ele move `scripts/` para `src/ai_tutor_core/`, o que quebraria os comandos deste `AGENTS.md`;
  - é trabalho em andamento fora da fonte única, então nada dele entrou no estudo.
- **O que o alinhamento anterior (`47650d6`) não tinha feito, e foi feito agora:**
  - `lessons/15-logica-decomposicao.md`, "Critérios de evidência":
    - o antigo item "`transfer`" virou a regra nova: `application` com `transfer: true`, aplicação padrão autônoma e correta em contexto novo;
    - entraram a variação no mesmo contexto depois de uma tentativa parcial e as ajudas que não tiram a autonomia;
  - na seção da transferência: o resultado de 22/10 e o caminho para o 80;
  - `state` 287 → 289: `programming_plan.expected_transfer` da `lesson_15` e `updated_at`.
- **Conferido sem mudança:**
  - os três tópicos em 80 têm `application` autônoma e correta com `transfer: true`;
  - as 3 evidências antigas com `kind: "transfer"` ficam como estão e não contam para o 80;
  - a regra nova não é aplicada para trás: o domínio só cai diante de duas evidências recentes de perda (contrato de aprendizagem, *Retention*);
  - o campo `required_evidence_types` das lições e tópicos continua listando `transfer` como **requisito**, e não como tipo de evidência a gravar.
- **Congelamento dos critérios** (registrado logo antes, às 19:17): este alinhamento só aplica à `lesson_15` as regras da `e87e2d7`, que são as congeladas. O rigor não muda.

## Critérios de domínio congelados — 2026-10-22

- Fora de sessão, a pedido do aluno: "congele os critérios de domínio por algumas lições". Nenhuma evidência, domínio, sessão, card ou ponto fraco foi alterado.
- **Até quando:** até a `lesson_17-algoritmos-debugging` ser concluída, que é o fim do bloco de lógica (lições 15 a 17).
- **O que congela:** a matriz de domínio, a aplicação padrão e o `supporting`, a escada de ajuda e a ajuda que não tira a autonomia, a conferência antes da devolutiva, as regras de transferência e a regra de avanço. Tudo isso conforme a skill `e87e2d7`.
- **O que continua livre:** corrigir defeitos nas regras (contradição, texto contrariado pelo validador, registro errado), sem mudar o rigor.
- **Pedidos de mudança:** registrados aqui e avaliados no fechamento da `lesson_17`. Antes disso, só diante de um bloqueio real: transferência pendente há mais de 3 sessões ou 2 semanas.
- Detalhes em `AGENTS.md`, seção "Critérios de domínio congelados".


## Alinhamento com a skill: ajuda que não tira a autonomia e transferência — 2026-10-22

- Fora de sessão. Não é sessão de aprendizagem: nenhuma evidência, domínio, sessão, card ou ponto fraco foi alterado. Executado a pedido do aluno, depois do merge do PR [14lucas-mendes/ai-tutor-skill#5](https://github.com/14lucas-mendes/ai-tutor-skill/pull/5).
- **Skill alinhada: commit `e87e2d7`.** Na skill, `unittest` OK e `validate_skill` PASS; no estudo, `validate_study` PASS.
  - Na máquina do aluno, `git -C <skill_root> pull` feito em 2026-10-22: **skill em uso: commit `e87e2d7`**.
- **Pedido do aluno:** a transferência para o 80 costuma sair parcial, e ele propôs aceitar ajuda no 80 e exigir autonomia só no 100.
- **Decisão do aluno**, depois da avaliação do tutor:
  - **não** exigir autonomia só no 100, porque contraria o objetivo de "autonomia real, sem dependência de vibe coding";
  - **não** contar transferência feita depois do degrau 3;
  - **não** mudar agora a regra de avanço (fechar a lição com 60 e a transferência pendente). Ela só volta à mesa diante de um bloqueio real.
- **Regras novas da skill:**
  - **Ajuda que não tira a autonomia:** em qualquer nível, a tentativa continua autônoma quando a única ajuda foi:
    - reformular a tarefa (degrau 1);
    - recuperar um pré-requisito (degrau 2);
    - a conferência genérica;
    - explicar o **contexto** (domínio, significado dos campos e formatos, termos do lugar).

    Nenhuma dessas ajudas pode entregar a decisão, o plano, os critérios, a análise ou o código. A ajuda dada fica registrada na evidência. É a regra 7 deste estudo levada para a skill.
  - **Transferência:**
    - precisa ser uma **aplicação padrão** autônoma e correta, num contexto em que a capacidade do tópico ainda não foi demonstrada neste estudo;
    - se sair parcial: conferência genérica, depois devolutiva, depois uma **tarefa diferente no mesmo contexto**, que conta para o 80;
    - refazer a mesma tarefa continua guiado, e não é preciso um terceiro contexto.
  - **Transferência é a marca `transfer: true`** numa evidência `application`, e não um tipo. As 3 evidências antigas com `kind: "transfer"` (`evidence_git-transferencia-01`, `evidence_git-transferencia-02` e `evidence_ordens-transformacao-01`) ficam como estão e não contam para o 80. Os tópicos já em 80 não são afetados: todos têm aplicação autônoma correta com `transfer: true`, e o `validate_study` passa.
- **Efeito na `lesson_15`:** se a transferência "classificar ordens de serviço" sair parcial, depois da conferência e da devolutiva, uma tarefa diferente com ordens de serviço conta para o 80. Uma pergunta sobre o significado de um campo da ordem não tira a autonomia.
- **`AGENTS.md`:** acrescentado o resumo das regras na seção de operação com a skill.

## `session_2026-10-22-lesson15-transferencia-01`

- Status: **interrompida e retomável**, das 16:36 às 18:44. Interrompida a pedido do aluno: "Amanhã eu corrijo".
  - `state` 275 → 287, `cards` 50 → 55, `learner-profile` 22 → 23.
  - Skill em uso: commit `d9605d4`.
- Lição `lesson_15-logica-decomposicao`: continua `in_progress`.
- **Cards:** 4 de 5 corretos (`tempos-04`, `git-remote-familia-01`, `dictreader-restval-01` e `git-log-oneline-01`). O `dictreader-fieldnames-01` não foi lembrado e volta em 23/10.
  - O `cond-01`, que vencia hoje, foi adiado de propósito para depois da transferência, para não dar pista.
- **Pré-requisito ensinado** (regras 1 e 7): o operador `in` / `not in` em dicionário. Na checagem, que não é evidência, acertou 3 de 3.
- **Duas dúvidas sobre o enunciado**, respondidas como reformulação (degrau 1): a saída é uma palavra; a entrada é uma ordem só.
- **Transferência "classificar ordens de serviço"**, em modo avaliação, no `formacao-python` (`src/modulo-03/classificar_ordens.py`, `c2f10399…`):
  - ✅ A ordem das verificações saiu certa e sem pista: guarda antes do acesso, bloqueado antes do tipo, específica antes da geral.
  - ❌ `__name__ == "__name__"`: os `assert` nunca rodaram.
  - ❌ O esperado do caso 3 contradiz a ordem decidida pelo próprio aluno.
  - ❌ A lista vazia não é pega pela guarda.
  - ❌ Os textos estão fora do contrato.
  - ❌ Faltaram a previsão e a tabela à mão.
  - A conferência genérica foi pedida uma vez: "Acredito que esteja completa".
  - Registrado em `evidence_logica-transferencia-ordens-01`: **transferência autônoma parcial**.
  - O tutor demonstrou dois dos erros numa cópia: com `__main__`, `AssertionError` no caso 3; com `itens: []`, `StopIteration`.
- **Domínio (regra 9):** `topic_logica-algoritmos` **continua em 60**.
  - ✅ Feynman autônomo (13/10).
  - ✅ Aplicação padrão (20/10).
  - ⏳ Transferência autônoma correta.
- **Ponto fraco** `weak_condicionais-ordem-guarda`: continua ativo. A ordem saiu certa, mas a aplicação foi parcial, e a guarda da lista vazia falhou.
- **Learner profile:** uma observação, `autonomous_attempt` parcial.
- **Próximo passo:**
  1. retomar esta sessão com uns 5 cards (incluindo `cond-01` e `fieldnames-01`);
  2. fazer a v2 guiada pelo checklist de 7 itens da lição;
  3. depois, uma **tarefa diferente com ordens de serviço**, só com o enunciado. Corrigido no commit desta sessão: pela skill `e87e2d7`, alinhada às 19:04, depois do fechamento, ela conta para o 80 e não é preciso outro contexto.
- **Ajuda dada antes da entrega**, registrada na evidência: o pré-requisito `in` (degrau 2) e duas reformulações do enunciado (degrau 1). Nenhuma tira a autonomia.

## Ajuste da transferência para o 80 — 2026-10-20

- Fora de sessão, a pedido do aluno: no Python Lab, a missão 006 só abre depois que as anteriores são concluídas.
- O Lab continua **só como referência**: nada foi alterado nele, nem a ordem das missões nem o `progress.json`.
- A missão foi **adaptada** como tarefa de transferência na seção "Transferência para o 80" da `lesson_15`:
  - o contexto é ordens de serviço, no repositório real `formacao-python`;
  - o arquivo é `src/modulo-03/classificar_ordens.py`, criado pelo aluno.
- **Ajuste:** a guarda devolve `"sem_itens"`, e não `raise ValueError`, porque lançar exceções ainda não foi ensinado nesta formação (regra 1). O núcleo é o mesmo: guarda antes do acesso e ordem das condições.
- `state` 274 → 275: `next_step` da sessão de 20/10 e `programming_plan.expected_transfer` da lição. `validate_study`: PASS.

## `session_2026-10-20-lesson15-variacao-01`

- Status: **concluída**, das 18:00 às 18:43 (cerca de 43 de 90 min). Concluída a pedido do aluno.
  - `state` 267 → 274, `cards` 45 → 50, `learner-profile` 21 → 22.
  - Skill em uso: commit `d9605d4`.
- Lição `lesson_15-logica-decomposicao`: continua `in_progress`. **Os três critérios de entrega estão cumpridos.**
- **Cards:** 5 de 5 corretos (`tempos-05` a `tempos-08` e `dictreader-chaves-01`).
- **Problema 4, em modo avaliação, só com o enunciado:** quantos cards vencidos há em cada status (`exe_03.py`, `73bd869b…`).
  - **Entrega completa:** decomposição com as decisões escritas, 5 exemplos com o esperado à mão, plano, função, 5 `assert` com mensagem, previsão e tabela de rastreio.
  - O tutor conferiu: tudo passa, e a tabela bate com a execução.
  - **Pergunta neutra sobre ajuda de IA**, feita porque o formato do texto mudou: "Foi feito por mim". Vale o que o aluno declarou.
  - A conferência genérica foi pedida uma vez ("Codigo terminado", sem mudança no arquivo).
  - Registrado em `evidence_logica-problema4-aplicacao-01`: **aplicação padrão, autônoma e correta**.
  - Depois do feedback, o `print` dentro do laço confirmou a tabela linha por linha (`evidence_logica-rastreio-execucao-01`, de apoio).
- **Domínio (regra 9):** `topic_logica-algoritmos` subiu de **40 para 60**.
  - ✅ Feynman autônomo (13/10).
  - ✅ Aplicação padrão (20/10).
  - ⏳ Falta a transferência a um contexto novo para o 80.
- **Ponto fraco resolvido:** `weak_python-test-literal-lista`, por `evidence_logica-caso-limite-assert-01` (16/10) e `evidence_logica-problema4-aplicacao-01` (20/10).
- **Learner profile:** uma observação, `autonomous_attempt` correta.
- **Próximo passo:** uns 5 cards; depois a missão 006 do Python Lab como transferência para o 80, só com o enunciado. Se sair correta, a `lesson_15` fecha (com o diário no Obsidian) e o pedido de unificação é avaliado.

## Complemento ao pedido de unificação: foco em agentes — 2026-10-19

- Fora de sessão. O aluno concordou com a avaliação da unificação e com o momento dela (fecho da `lesson_15`). Ele acrescentou que a parte de engenharia de IA deve focar em "agentes, engenharia de loop, programação agêntica e harness engineering, orquestração de agentes, arquitetura de agentes de IA e coisas relacionadas".
- **Regra citada:** formação fechada. O complemento foi **registrado e não aplicado**, e será avaliado junto com o pedido no fecho da `lesson_15`.
- **Achado:** a pasta `harnnes-engeniring` é uma quarta formação, parada desde 22/09, sem sessão nem evidência, e o currículo dela cobre esse foco.
- **Avaliação prévia do tutor:**
  - dentro das lições 20 a 22, entra como lente das aulas, e a `lesson_22` vira o núcleo agêntico;
  - depois da `lesson_13`, entra como trilha de especialização em agentes, com orquestração e subagentes, harness em profundidade e MCP;
  - antecipar exigiria lição nova, o que é mudança estrutural sem bloqueio real.
- Detalhes na seção 4.1 de [`docs/compose/spec/pedido-unificacao-engenharia-ia.md`](docs/compose/spec/pedido-unificacao-engenharia-ia.md).
- O repositório `fundamentos-engenharia-ia` tinha 4 arquivos com mudanças pendentes, que registravam a sessão M01 retomada e concluída em **08/10**.
  - Por pedido do aluno, entraram no commit `6c7ac9b` e foram enviados ao GitHub, depois de um `validate_study` com PASS naquele estudo.
  - Nenhuma evidência nova; o M01 continua em 20.
  - **Correção de registro:** o pedido dizia que a última sessão de IA tinha sido em 03/10. A data certa é 08/10, e a tabela do pedido foi corrigida.

## Alinhamento com a skill: critério do 60 e conferência antes da devolutiva — 2026-10-19

- Fora de sessão. Não é sessão de aprendizagem: nenhuma evidência, domínio, sessão, card ou ponto fraco foi alterado. Responde ao pedido abaixo, depois do merge do PR [14lucas-mendes/ai-tutor-skill#4](https://github.com/14lucas-mendes/ai-tutor-skill/pull/4).
- **Skill em uso: commit `d9605d4`** (pull feito pelo aluno em 19/10). Na skill, `unittest` OK e `validate_skill` PASS; no estudo, `validate_study` PASS.
  - **Na máquina do aluno**, conferido em 2026-10-19 às 20:36:
    - até então, a pasta instalada ainda estava em `6a43e26`;
    - o `git pull --ff-only` levou a skill a **`d9605d4`**;
    - na skill, `unittest` passou (146 testes) e o `validate_skill` deu PASS;
    - o estudo avançou para a `a9d25fb`, e o `validate_study` deu PASS.
    - A partir daqui, o tutor local aplica a aplicação padrão, o `kind: "supporting"` e a conferência antes da devolutiva.
- **Decisão do aluno:** a matriz **não** foi afrouxada. Ficaram de fora o "Feynman correto + aplicação parcial = 60" e um nível 50. Entraram duas regras, só em texto:
  - **Aplicação padrão:** o 60 exige a aplicação que cumpre o objetivo da lição de ponta a ponta. Quando o objetivo tem várias partes, ela cobre todas.
    - Comportamentos menores, como prever uma saída, rastrear um laço ou escrever um `assert` isolado, são **evidência de apoio**, gravada com `kind: "supporting"`. O validador barra um 60 apoiado só nela.
    - Quando um acerto autônomo não conta, o tutor diz qual é o critério e por quê.
  - **Conferência antes da devolutiva:** diante de uma aplicação autônoma parcial ou incorreta, o tutor pede **uma vez por tarefa**, com a frase fixa "Confira sua solução contra cada regra e exemplo do enunciado.", sem apontar o que falta.
    - Esse pedido não aplica teto. Se o aluno achar e corrigir sozinho, a correção é uma nova evidência **autônoma**.
    - Apontar a categoria do erro, como "confira os casos-limite", já é degrau 3. Se a revisão continuar parcial, segue a escada de ajuda.
  - O nível 40 passa a descrever também a aplicação autônoma com um elemento material faltando.
- **Leitura das evidências existentes** (nada foi reclassificado no `state.json`):
  - `evidence_logica-previsao-return-laco-01` está gravada como `application`, mas é **evidência de apoio**, porque é uma previsão isolada. **Não conta para o 60** de `topic_logica-algoritmos`, embora o validador a aceitasse.
  - Para o 60, continua valendo: ✅ Feynman autônomo (13/10); ⏳ falta uma **aplicação padrão** autônoma e correta, ou seja, um problema da lição feito de ponta a ponta só com o enunciado.
  - Na próxima variação, se ela sair parcial, o tutor faz primeiro a conferência genérica, e uma correção do aluno sem mais ajuda conta como autônoma.
- **`AGENTS.md`:** acrescentado o resumo das duas regras na seção de operação com a skill.

## Pedido do aluno: rever o rigor do critério 40 → 60 — 2026-10-19

<!-- Título restaurado em 2026-10-19: o commit a9d25fb tinha apagado esta linha sem querer. -->

- **Pedido**, nas palavras do aluno: "essa condição do 40 para 60 não está muito rígida? Eu fiz praticamente tudo sozinho [...] o fator principal deve ser se eu entendi o que eu fiz [...] em vez de somente a prática em si."
- **Onde a regra mora:** a matriz de domínio é da skill (`references/learning-contract.md`, na fonte única `ai-tutor-skill`). Ela não pertence aos itens congelados da formação fechada. Mudar a matriz exige branch e PR na skill, com o CI verde, e não se faz por decisão do tutor no meio de uma sessão.
- **O que o tutor reviu na aplicação** (regra 9, sem inflar nem desqualificar):
  - Pela matriz, o 60 já mede o entendimento: uma das duas metades é a **explicação Feynman**, cumprida em 13/10.
  - A outra metade pede **uma** aplicação autônoma correta.
  - A v1 do `exe_02.py` foi autônoma, mas deixou de fora duas exclusões que a tarefa citava de forma explícita (sem tópico, sem id). Com id vazio, ela poria `{"": ...}` no painel, o que é um problema de confiabilidade. Pelo contrato, isso é **parcial** ("falta um elemento material que impede cumprir o objetivo com segurança ou confiabilidade").
  - A classificação ficou mantida. O tutor reconheceu que é um caso de fronteira.
- **Evidências da semana a favor de manter a aplicação no critério:** em 16 e 17/10, entendimento e código divergiram nos dois sentidos.
  - o código passava, mas a previsão do laço vazio e a da chave repetida saíram erradas;
  - em 19/10, a previsão do `return` dentro do laço saiu certa.
- **Recomendação do tutor:** não afrouxar a matriz. O caminho mais curto é uma variação nova só com o enunciado na próxima sessão, que leva uns 20 minutos. Se ela sair correta, o tópico vai a 60 na hora.
- **Se o aluno quiser mudar a regra mesmo assim:** abrir um issue ou PR em `14lucas-mendes/ai-tutor-skill`, propondo a mudança na matriz ou na leitura de "parcial", e avaliar com calma, fora da sessão. A autoridade final é dele.

## `session_2026-10-17-lesson15-problema3-01` (retomada e concluída em 2026-10-19)

- Status: **retomada** às 17:16 e **concluída** às 18:45 (cerca de 89 de 90 min). Concluída a pedido do aluno.
  - `state` 260 → 267, `cards` 40 → 45, `learner-profile` 20 → 21.
  - Skill em uso: commit `6a43e26`. O estudo avançou para a `269eac3`, que veio do GitHub.
- **Cards:**
  - ✅ `git-remote-v-01` e `git-push-u-01`, que tinham falhado em 17/10 (voltam em 26/10);
  - parciais `cond-01`, `git-remote-familia-01` e `tempos-04` (voltam em 22/10).
- **`exe_02.py` v1**, feito sozinho em cerca de 40 min: autônomo e **parcial** (`evidence_logica-problema3-codigo-01`).
  - O filtro e a saída `{id: tópico}` estão certos, com 5 `assert`.
  - O aluno declarou que os esperados foram calculados à mão antes de rodar.
  - Faltaram as exclusões de "sem tópico" e "sem id".
- **Feedback:**
  - v2 com um laço só, mas com o `return {}` para item inválido dentro do laço.
  - Na pergunta do caso misto, previu que o código devolveria `{}`, o que está certo. Registrado em `evidence_logica-previsao-return-laco-01` (autônoma).
  - Corrigiu o id e depois o tópico (`evidence_logica-problema3-codigo-02`, guiada e correta).
- **Domínio (regra 9):** `topic_logica-algoritmos` segue em **40**.
  - ✅ A metade **Feynman** do 60 foi cumprida em 13/10.
  - ⏳ Falta a **aplicação autônoma correta**.
- **Learner profile:** uma observação, `autonomous_attempt` parcial.
- **Próximo passo:**
  1. uns 5 cards;
  2. uma variação nova só com o enunciado;
  3. a tabela de rastreio do aluno.
  - Opcional: o `assert` do caso misto de tópico e um `.gitignore`.

## `session_2026-10-17-lesson15-problema3-01`

- Status: **interrompida e retomável**, das 18:34 às 20:00 (cerca de 86 de 90 min). Interrompida a pedido do aluno.
  - `state` 253 → 260, `cards` 35 → 40, `learner-profile` 19 → 20.
  - Skill em uso: commit `6a43e26`, com `theory_first`. O tema já tinha teoria escrita, então a sessão retomou a prática sem recomeçar a aula.
- Lição `lesson_15-logica-decomposicao`: continua `in_progress`.
- **Cards (5, preferência `card_review_pacing`):**
  - `cond-01`: ❌ **incorreto**. A resposta saiu invertida ("juntas: `if/elif`; uma ou outra: um `if` com `or`"). Volta em 18/10.
  - `tempos-03`: ✅ **correto**. Volta em 24/10.
  - `git-remote-familia-01`, `git-remote-v-01` e `git-push-u-01`: ❌ não lembrados. Voltam em 18/10.
  - Cada card recebeu uma explicação simples depois da tentativa.
- **Repositório do app criado pelo aluno**, antes de mandar o plano pedido: [`14lucas-mendes/second-brain-agent`](https://github.com/14lucas-mendes/second-brain-agent).
  - É público, com a branch `main` ligada a `origin/main`.
  - O primeiro commit, `ac8833d`, tem só `exercicios/` com dados fictícios. Conferido pelo tutor.
  - Registrado em `evidence_git-repo-second-brain-01`: autônomo, correto, em uso real.
  - **Não conta** para a saída de `weak_git-formas-exatas-comandos`, porque os comandos tinham sido explicados nos cards minutos antes.
  - O `project_segundo-cerebro` ganhou o campo `repository`.
- **Problema 3: decomposição só com o enunciado.** Registrada em `evidence_logica-decomposicao-problema3-01`: **guiada**, parcial.
  - **Próprio do aluno:** o status como parâmetro e a exclusão dos dados com defeito.
  - **Erros e como foram resolvidos:**
    - os exemplos tinham um item cada, e não uma lista;
    - a saída `{tópico: status}` apagava pontos fracos do mesmo tópico. Com uma pergunta direcional, ele propôs contar por tópico;
    - com a pergunta "quais × quantos", propôs `{"weak_point_id": ...}` com a chave repetida. Previu que o `print` mostraria as duas chaves; rodou e viu só `weak_02`;
    - chegou a `{id: tópico}`;
    - os esperados tinham etiquetas fora do contrato (`"sem status ativo"`, `None`, `0`) e ids e tópicos trocados. Ficaram todos certos depois do degrau 4 e da analogia da peneira.
  - Também vira evidência de apoio de `weak_verificacao-valor-esperado`.
- **Domínio (regra 9):** `topic_logica-algoritmos` segue em **40**.
  - ✅ A metade **Feynman** do 60 foi cumprida em 13/10.
  - ⏳ Falta a **aplicação autônoma**. O alvo é o código do problema 3.
- **Learner profile:** uma observação, `help_usage` de nível 4.
- **Próximo passo:** uns 5 cards; depois o código do problema 3 a partir da decomposição do aluno, com `assert` em listas literais, previsão antes de rodar e uma tabela de rastreio própria. Opcional: `.gitignore`.

## Alinhamento com a skill: teoria primeiro — 2026-10-17

- Fora de sessão. Não é sessão de aprendizagem: nenhuma evidência, domínio, sessão, card ou ponto fraco foi alterado. Executado a pedido do aluno, depois do merge do PR [14lucas-mendes/ai-tutor-skill#3](https://github.com/14lucas-mendes/ai-tutor-skill/pull/3).
- **Skill alinhada: commit `6a43e26`.** Na skill, `unittest` OK e `validate_skill` PASS; no estudo, `validate_study` PASS antes e depois da mudança.
  - Na máquina do aluno, `git -C <skill_root> pull` feito em 2026-10-18: **skill em uso: commit `6a43e26`**.
  - **Feito em 2026-10-17, na máquina do aluno:**
    - o estudo avançou da `203d57e` para a `c467df4` com `git pull --ff-only`;
    - a skill instalada avançou de `bd567cd` para **`6a43e26`**;
    - na skill, `unittest` passou (145 testes) e o `validate_skill` deu PASS;
    - no estudo, o `validate_study` deu PASS;
    - a junction `~/.claude/skills/ai-tutor` aponta para a fonte única.
    - A partir daqui, o tutor local segue `theory_first`.
- **Mudança na skill:** o aluno escolhe a abordagem de ensino, e o padrão passa a ser `theory_first`, a aula completa do zero antes da prática. Isso já era o que pediam as regras 1 e 2 deste estudo, que a skill antiga contrariava com a "exposição mínima".
- **Não é mudança estrutural** pela regra da formação fechada: tópicos, ordem, escopo, stack e carga continuam iguais. A abordagem é "adaptar a aula dentro de cada lição", que continua livre.
- **`study-config.json`:** `teaching_policy: {"approach": "theory_first"}`, gravado por `scripts.migrate_state` (`_upgrade_v2_support_files`). Nenhum outro arquivo canônico mudou.
- **`lessons/15-logica-decomposicao.md`:** reorganizado em **Teoria**, **Plano de prática** e **Progresso**, sem perder conteúdo.
  - A Teoria é um resumo dos conceitos já ensinados de 09 a 16/10 (decomposição, esperado × obtido, caso-limite, contrato da saída, `assert`, tabela de rastreio, guarda e curto-circuito, `None` × `""`, datas ISO, dicionário com chave nova, laço vazio e código morto), com erros comuns, três checagens e a ponte para o `segundo-cerebro`.
  - O tema já tem evidência, então não recomeça do zero. O problema 3 não aparece na teoria, para continuar sendo feito só com o enunciado.
  - É material do tutor e não é evidência.
- **`AGENTS.md`:** o protocolo de aula passa a descrever a teoria completa, o override por lição e a divisão da lição em sessões. O campo `teaching_policy` entrou na seção Estado.
- As lições concluídas (`lessons/00` e `lessons/03`) não foram reescritas.

## Preferência de revisão de cards — 2026-10-16

- Fora de sessão. Pedido do aluno: os cards vencidos entram aos poucos, **cerca de 5 no início de cada sessão**, como revisão (`retrieval_first`), em vez de todos de uma vez.
- Gravado em `learner-profile.json` como preferência declarada `card_review_pacing` (revisão 18 → 19). `validate_study`: PASS.
- Não muda a escada de espaçamento, que continua `fixed` em 1/3/7/16/35/60 dias. Os cards que não forem revisados continuam vencidos e entram nas sessões seguintes, começando pelos mais atrasados.

## `session_2026-10-13-lesson15-problema2-01` (retomada e concluída em 2026-10-16)

- Status: **retomada** às 18:29 e **concluída** às 19:59 (90 min, o padrão). Concluída a pedido do aluno.
  - `state` 251 → 253 (252 na retomada), `learner-profile` 17 → 18.
  - Skill em uso: commit `bd567cd`.
- Lição `lesson_15-logica-decomposicao`: continua `in_progress`. O **problema 2 está fechado** no código (`exe_01.py`, `6088b9fd…`).
- **Regra do `evidence_id` vazio:**
  - A primeira resposta misturou duas situações: "tópico sem evidência" (que aparece com `0`) e "evidência sem número".
  - Depois de uma pergunta direcional (degrau 3), classificou a linha do `javascript` como "ficha sem número", o que está certo. A analogia, porém, saiu invertida (`topic_id` = ficha).
  - Conferindo pelo próprio resultado, acertou: "as chaves são os tópicos e o valor é a quantidade de vezes que esses tópicos aparecem na minha lista".
  - Regra escrita: "conta quando ela existe". A direção está certa; o ajuste de precisão é "quando o `evidence_id` não está vazio".
- **`assert`:**
  - Primeiro, um `assert` com a lista grande e mensagem em f-string.
  - Depois, um `assert` **isolado** da ficha sem número, com listas escritas direto na chamada e no `assert`. Registrado em `evidence_logica-caso-limite-assert-01`: **autônomo e correto**. É a primeira saída de `weak_python-test-literal-lista`; falta outra, em outra sessão.
  - Não declarou a previsão antes de rodar.
- **Caso vazio, só com o enunciado:**
  - Escreveu os esperados `{"lista": 0}` e `{"topicos": 0}` e ajustou a função até eles passarem. Registrado em `evidence_logica-caso-vazio-01`: **incorreto**, porque as chaves não são tópicos e isso quebra o contrato da saída. Vira evidência de apoio de `weak_verificacao-valor-esperado`.
  - Com o degrau 3 (o painel de quem começa sem evidências e o contrato de 13/10), calculou `{"topic_python": 0, "topic_sql": 0}` e `{}`, ambos certos.
- **Rastreio do laço vazio:**
  - Disse que o `return {topico: 0}` executava, embora tenha dito também que o laço da lista vazia "nem chega a rodar". Registrado em `evidence_logica-rastreio-laco-vazio-01`: **incorreto**.
  - O tutor explicou com a imagem da fila sem ninguém e com a prova dos próprios testes.
  - O aluno apagou o código morto sem prever o resultado, os testes passaram, e ele pediu a explicação.
  - O tutor montou a tabela de rastreio dos casos 3 e 4. A explicação Feynman que veio em seguida foi correta, mas **guiada** (`evidence_logica-laco-vazio-feynman-01`).
- **Domínio (regra 9):** `topic_logica-algoritmos` segue em **40**.
  - ✅ A metade **Feynman** do 60 foi cumprida em 13/10.
  - ⏳ Falta a **aplicação autônoma**.
- **Learner profile:** uma observação, `autonomous_attempt` incorreta. Inventou os esperados do caso vazio e ajustou o código até passar; a previsão veio depois do ajuste.
- **O que falta para concluir a `lesson_15`:**
  - problema 3 com plano antes do código (hoje são 2 de 3);
  - uma tabela de rastreio montada pelo aluno e conferida por execução;
  - aplicação autônoma para o domínio 60;
  - aplicação autônoma em contexto novo para o 80;
  - criar o repositório Git `segundo-cerebro`.
- **Próximo passo:** criar o repositório e depois fazer o problema 3 só com o enunciado. Cards atrasados: `cond-01`, `tempos-03..08` e `dictreader-*`.

## `session_2026-10-13-lesson15-problema2-01` (retomada em 2026-10-15)

- Status: **retomada** às 19:25 e **interrompida de novo, retomável**, às 20:25 (cerca de 60 de 45 min, orçamento pedido pelo aluno). Interrompida a pedido do aluno, que volta amanhã.
  - `state` 248 → 250 (249 na retomada), `learner-profile` 16 → 17.
  - Skill em uso: commit `bd567cd`.
- Lição `lesson_15-logica-decomposicao`: continua `in_progress`.
- **Pergunta das gavetas** (degrau 3, retomada de 13/10): "Eu preciso de uma gaveta para cada tópico". Correto. Ele não disse quantas gavetas o código tinha (uma).
- **Pré-requisito relembrado** (regra 7): dicionário, com `=` criando a chave, `+= 1` somando e `KeyError` quando a chave não existe.
- **Código do aluno**, feito sozinho em cerca de 50 min: `exe_01.py` (`494f60e3…`).
  - Um dicionário `result` com as 4 chaves escritas à mão valendo `0`, um laço `topicos × lista` e `result[topico] += 1`.
  - Tirou o `evicence_id` e o `return 0` de dentro do laço.
  - O tutor rodou com `python -I` e conferiu a saída: `{'topic_python': 2, 'topic_sql': 2, 'topic_git': 1, 'topic_javascript': 1}`.
  - Registrado em `evidence_logica-gavetas-problema2-02` (aplicação parcial, depois do degrau 3).
- **Faltam:**
  - criar as gavetas a partir de `topicos`, porque hoje estão fixas e o exemplo 1 não passaria;
  - fazer o caso vazio devolver um dicionário, e não um texto;
  - escrever os `assert`.
  - Ficou sem resposta a pergunta de previsão `calcular_topicos(lista, ["topic_python", "topic_rust"])`.
- **Domínio (regra 9):** `topic_logica-algoritmos` segue em **40**.
  - ✅ A metade **Feynman** do 60 foi cumprida em 13/10.
  - ⏳ Falta a **aplicação autônoma**.
- **Learner profile:** uma observação, `help_usage`. Depois da pergunta das gavetas, trabalhou sozinho além do orçamento e voltou com o código rodando, pedindo verificação.
- **Revisão das 20:52** (`resumed → interrupted`, `state` 250 → 251). Depois do encerramento, o aluno trabalhou sozinho e pediu revisão.
  - Versão `def56e11…`: as gavetas são **criadas a partir de `topicos`**. Com `["topic_python", "topic_rust"]`, o tutor obteve `{python: 2, rust: 0}`, e o exemplo 1 passa.
  - Regra nova, só no código: evidência com `evidence_id` vazio não conta.
  - Registrado em `evidence_logica-gavetas-problema2-03` (parcial, depois da devolutiva que apontou as chaves fixas).
- **Próximo passo:** escrever na decomposição a regra do `evidence_id` vazio; fazer o caso vazio devolver um dicionário; escrever um `assert` por exemplo, prevendo antes de rodar. Cards atrasados: `cond-01`, `tempos-03..08` e `dictreader-*`.

## Formação sem prazo definido — 2026-10-15

- Fora de sessão de estudo. Decisão do aluno: "não vou assumir um prazo para terminar. Quero deixar sem prazo definido."
- **Por que foi aplicada agora:** o prazo não está entre os itens congelados da formação fechada (`formacao-fechada.md`, seção 6: tópicos e lições, ordem, MVP, stack e carga) e já era só referência. A **carga de 10 h por semana continua congelada**.
- `study-config.json`: `deadline` passou a `null`, o `cycle_calendar` (janelas de 21 dias até 2027-10-24) foi retirado e o `program_start_note` ganhou o registro. Gravado com `FileLock` e substituição atômica (o arquivo não tem `revision`).
- `curriculum.md`: a seção "Calendário de referência" virou "Sem prazo definido", e a coluna "Janela" saiu da tabela. O número do ciclo indica só a ordem das lições.
- `formacao-fechada.md` (seção 4), `AGENTS.md` e o pedido de unificação foram ajustados.
- `validate_study`: PASS.

## Pedido de mudança estrutural — 2026-10-15 (unificar a formação de Engenharia de IA)

- Fora de sessão de estudo. Nenhum arquivo `.ai-tutor/*.json` foi alterado.
- **Regra citada:** formação fechada (`formacao-fechada.md`, seção 6, e `AGENTS.md`). O pedido é registrado, **não é aplicado nesta conversa** e será avaliado no fecho da `lesson_15-logica-decomposicao`, com justificativa escrita.
- **Pedido do aluno:** unificar neste repositório a formação de Engenharia de IA (`14lucas-mendes/fundamentos-engenharia-ia`), que seria arquivada. Os módulos entram como aprofundamento das lições 20, 21, 22 e 12, sem lição nova, troca de ordem, mudança de stack ou mudança no MVP. A formação de Claude Code fica de fora.
- **Arquivo:** [`docs/compose/spec/pedido-unificacao-engenharia-ia.md`](docs/compose/spec/pedido-unificacao-engenharia-ia.md), com o mapeamento módulo → lição e o parecer prévio do tutor (aceitar, limitando cada módulo à capacidade que o app usa).
- Pendências para o fecho, se aceito: commitar as 4 mudanças pendentes do repositório de IA antes de arquivar e conferir o `validate_study` dele.

## `session_2026-10-13-lesson15-problema2-01`

- Status: **interrompida e retomável**, das 13:45 às 16:02 (cerca de 137 de 120 min, orçamento pedido pelo aluno). Interrompida a pedido do aluno.
  - `state` 242 → 248, `learner-profile` 15 → 16.
  - Skill em uso: commit `bd567cd`.
  - Horários lidos do relógio: 13:43, 15:04, 15:13, 15:59 e 16:02. Os outros são aproximados.
  - O **modo só-olhar** foi ligado no meio da sessão. As gravações seguintes foram feitas com a aprovação explícita do aluno ("aprovo, pode gravar"; "pode gravar").
- Lição `lesson_15-logica-decomposicao`: continua `in_progress`.
- **`and`/`or`, a pergunta combinada em vez de card** (`retrieval_first`): `pedidos = []` com `len(pedidos) > 0 and pedidos[0] == "cafe"`. Resposta **correta e sem ajuda**: roda sem erro, o `and` para no `False` e o programa vai direto ao `print("fim")`. Registrada em `evidence_curto-circuito-and-02`; a evidência de 12/10 tinha saído incorreta.
- **Feynman, só com o enunciado:** de onde vem o `1` do `assert` e por que não copiar o resultado da execução. Resposta **correta e autônoma**, registrada em `evidence_logica-esperado-feynman-02`.
  - O `1` vem da regra: "se o card pertence à data do dia avaliado, ele está vencido".
  - "O meu código precisa ser ajustado de acordo com o resultado que eu espero." A contradição de 12/10 não reapareceu.
- **Problema 2: evidências por tópico.** Decomposição **guiada** (degraus 1 a 3), registrada em `evidence_logica-decomposicao-problema2-01` (parcial).
  - Primeira versão: a entrada era **um** tópico, mas a saída era um dicionário com **todos**. Os `assert` comparavam com um inteiro, usando um dicionário solto e esperando 2, número tirado da lista grande.
  - Depois da reformulação com o painel (degrau 1), o aluno passou a receber a lista de evidências e a lista de tópicos. Decidiu sozinho que o tópico sem evidência vale `0`, e não `None`, porque é um "tópico não iniciado".
  - Os exemplos completos tinham **a mesma entrada com dois esperados diferentes**. Além disso, davam `javascript: 0` com uma evidência de `javascript` na lista. O tutor apontou a contradição com a analogia da máquina de café (degrau 3), e o aluno corrigiu os dois exemplos.
  - **Próprio do aluno:** a lista vazia no plano; o caso do `topic_id` vazio; a **detecção do descompasso entre `"python"` e `"topic_python"`** antes de rodar; a decisão de ajustar a lista de tópicos, e não a de evidências.
- **Pré-requisito ensinado** (regras 1 e 7): criar uma chave nova num dicionário (`=` cria; `+= 1` lê e soma; `KeyError` quando a chave não existe). Houve dois exemplos executados. Na previsão, o aluno respondeu "`KeyError` na linha 4" e se corrigiu sozinho antes de enviar; isso não conta como evidência.
- **Código em andamento:** `segundo-cerebro/exercicios/exe_01.py` (`a4d0cff5…`). Tem um contador só para todos os tópicos, o erro de digitação `evicence_id`, um `return 0` dentro do laço e a entrada vazia devolvendo texto. Os `assert` ainda não foram escritos.
  - O aluno pediu "ajuda só para pensar onde estou errando", sem resposta e sem código.
  - Recebeu três perguntas de localização: quantas gavetas o código tem para 4 tópicos; rodar o código e ler o traceback; o caso vazio contra a decisão do `0`.
- **Domínio (regra 9):**
  - `topic_logica-algoritmos`: **20 → 40**, porque aplicou parcialmente o procedimento com ajuda direcional;
    - ✅ a metade **Feynman** do nível 60 foi **cumprida** hoje;
    - ⏳ falta a **aplicação autônoma**, que pode vir do código do problema 2 ou do problema 3 feito sem pistas sobre o núcleo;
  - `topic_python-fundamentos`: segue em **80**;
  - `weak_verificacao-valor-esperado` ganhou uma evidência de apoio (o esperado sem conferir pela regra) e segue ativo.
- **Learner profile:** uma observação, `help_usage`. O aluno pediu ajuda só para localizar o erro, sem resposta.
- **Próximo passo:** retomar pela pergunta das gavetas, com o rastreio à mão do exemplo 1. Depois:
  1. o traceback;
  2. o `return 0` dentro do laço;
  3. o caso vazio;
  4. um `assert` por exemplo, com a previsão antes de rodar.

  Cards: `cond-01` (14/10), `tempos-03..08` e `dictreader-*` atrasados.

## `session_2026-10-12-lesson15-problema1-02`

- Status: concluída, das 18:12 às 18:47 (cerca de 35 de 45 min, orçamento pedido pelo aluno). Fechada a pedido do aluno.
  - `state` 231 → 242, `learner-profile` 14 → 15.
  - Skill em uso: commit `bd567cd`.
  - Horários lidos do relógio.
- Antes da sessão, a pedido do aluno: o `quiz.html` da lição 15 passou a ser **sempre escuro**. Antes, ele seguia o tema claro do Windows.
- Lição `lesson_15-logica-decomposicao`: continua `in_progress`.
- **Feynman, só com o enunciado e sem mídias:** "por que copiar o esperado da execução não prova a função". Resultado **parcial**, registrado em `evidence_logica-esperado-feynman-01`.
  - Certo: o esperado tem que estar pronto antes, sem tentativa e erro.
  - Faltou: a fonte (a regra) e o porquê (o teste confere o código com ele mesmo).
  - A última frase contradizia o resto: "se os testes não baterem, ajusto o valor esperado".
  - Depois de uma pergunta direcional (degrau 3), corrigiu: "não ajusto o teste, ajusto a função". É prática guiada.
- **Problema 1, fechado.** Versão final `f4898339…`:
  - um `if` só, `card["due_at"] == None or card["due_at"] <= hoje`, que é um uso correto do `or` (as duas condições levam à mesma ação);
  - o `None` vem primeiro, como guarda;
  - 6 `assert` passando, com os esperados da tabela e sem mudar nenhum;
  - o `None` substituiu o `""` no teste.
  - Previsão própria correta: "vai passar porque o `None` é verificado primeiro". O aluno declarou que antes não sabia o porquê.
- **Curto-circuito.** Foram registradas evidências de `topic_python-fundamentos`, ensinado em 02/10:
  - `evidence_condicionais-curto-circuito-01` (**incorreta**): previu que a ordem invertida "passa, o `or` verifica um ou o outro";
  - `evidence_curto-circuito-diagnostico-01` (**correta**, sozinho): rodou a versão invertida e explicou o `TypeError` pelo traceback;
  - `evidence_curto-circuito-variacao-01` (**parcial**): na fila vazia com `fila[0]` antes do `len`, acertou "dá erro" e a ordem certa, mas disse "vazia = falso, por ser falso não roda a direita" e `TypeError` em vez de `IndexError`;
  - `evidence_curto-circuito-and-01` (**incorreta**): com `and`, achou que `False` passa para a direita. O `IndexError` saiu certo desta vez.
  - O tutor explicou com execução e com a tabela `and` × `or` (convite E documento / cartão OU dinheiro).
  - O aluno disse que no `and` foi "detalhe de atenção" e **dispensou o card**. Combinado: uma pergunta rápida de `and`/`or` na abertura da próxima sessão.
- **Domínio (regra 9):**
  - `topic_logica-algoritmos`: **0 → 20**, a primeira evidência válida. Para o 60, a explicação Feynman ainda não saiu correta sozinha e a aplicação sozinha ainda não foi feita;
  - `topic_python-fundamentos`: segue em **80**. O curto-circuito não fazia parte das evidências do 80;
  - `weak_condicionais-ordem-guarda` e `weak_verificacao-valor-esperado` ganharam evidências de apoio e seguem ativos.
- **Pergunta do aluno, "falta muito?".** Hoje nada essencial ficou pendente. A lição 15 leva umas 3 ou 4 sessões. A formação está uns 2 ciclos adiantada, e o risco são as horas semanais.
- **Learner profile:** uma observação. A falha controlada (prever, inverter, rodar) deu resultado positivo no diagnóstico.
- **Próximo passo:**
  1. a pergunta de `and`/`or`;
  2. uma nova tentativa sozinho da explicação "o esperado vem da regra";
  3. o problema 2 decomposto sozinho antes do código.

## Mídias dos pontos fracos — 2026-10-11 (`/media`, `media-index` 13 → 14, `sources` 6 → 7)

- Não é sessão de aprendizagem. Nenhuma evidência, domínio ou ponto fraco foi alterado. As mídias têm `evidence_eligible: false`.
- **Pedido do aluno:** mídias para trabalhar os pontos fracos. Entre os seis ativos, escolheu os três que travam o `contar_vencidos`:
  - `weak_verificacao-valor-esperado`;
  - `weak_python-test-literal-lista`;
  - `weak_condicionais-ordem-guarda`.
- **Pacote local** `media/lesson_15-logica-decomposicao/notebooklm/` (`media_9e5caffe-…`), criado com `create_learning_pack`:
  - **principal:** quiz de 9 perguntas, 3 por ponto fraco (`local/quiz.json`, com gabarito separado, e `local/quiz.html`, interativo, em tema escuro). Cada distrator corresponde a um equívoco registrado: esperado copiado da execução, `str([])`/`int([])`, dicionário sem lista, lista grande com a data variando, `or` no lugar de `elif`, ordem trocada;
  - **complementar:** o diagrama "De onde vem o esperado?" (`esperado-vs-obtido.excalidraw`, em tema escuro, mais a prévia `.svg`), com texto alternativo em `image-brief.md`.
- **Fonte nova:** `source_python-assert` (Python Language Reference, 7.3), lida na documentação oficial em 11/10.
- **Verificação:** todo o código das perguntas foi executado em Python 3.11. As prévias foram renderizadas e conferidas. As posições das respostas certas foram embaralhadas para não formar padrão.
- **Limite pedagógico:** o pacote não mostra a correção do `contar_vencidos` ("sem data" × "venceu"). A pergunta `q15-corrigir-dupla` ensina a mesma ideia em outro contexto (pedidos).
- **NotebookLM:** ainda sem consentimento de envio (`consented: false`).
- **Próximo passo:** depois do uso, pedir uma explicação autônoma, sem as mídias, de por que o esperado vem da regra.

## `session_2026-10-11-lesson15-problema1-01`

- Status: concluída, das 17:56 às 19:37 (cerca de 101 de 90 min). Fechada a pedido do aluno.
  - `state` 221 → 231, `cards` 33 → 35, `learner-profile` 13 → 14.
  - Skill em uso: commit `bd567cd`.
  - Horários lidos do relógio: 17:56, 18:28, 18:41, 19:08, 19:10, 19:15, 19:34 e 19:36. Os horários intermediários da revisão (18:00, 18:05, 18:08) são aproximados.
- Lições:
  - `lesson_15-logica-decomposicao`: continua `in_progress`;
  - `lesson_01-python-core` e `lesson_02-arquivos-erros`: cards.
- **Revisão** (`retrieval_first`; não é evidência):
  - `cond-01` **parcial**. "Juntas → `if` separados" estava certo. No caso "uma OU outra", respondeu "um `if` só com o operador OU", o mesmo padrão de 02/10. O tutor reformulou com aprovado/reprovado (degrau 1), e o aluno escreveu `if nota >= 6` / `elif nota < 6`, que está correto. O card fica no passo 1 e volta em 14/10.
  - `cond-05` **correto** sem ajuda: ler de volta não prova a transformação; prova a comparação com o resultado esperado. Passa do passo 1 para o 2 e volta em 18/10.
- **Problema 1: `contar_vencidos.py`.** Versões do aluno, por SHA-256: `91bf4a33` → `3c6f3916` → `42ff37d2` → `99b9dbf5` → `3018a621` → `6ddabb82` (a final).
  - **Feito pelo aluno:**
    - saída como `int`;
    - `if __name__ == "__main__":` por iniciativa própria;
    - data fixa nos `assert`;
    - `return 0` para a lista vazia, corrigido sozinho depois de o teste falhar;
    - `>` trocado por `>=`;
    - a verificação do "sem data" movida para **antes** da comparação.
  - **Pré-requisito ensinado** (regra 7): a forma de "um `assert` por linha da tabela, com a sua própria lista pequena". Houve dois exemplos executados (`somar_lista` e `contar_cor`), um deles com o esperado errado de propósito, para mostrar o `AssertionError`.
    - A primeira explicação não foi entendida: o aluno manteve a lista grande e variou a data. **Falha do material.** O tutor deu o `assert` da linha 1 como modelo.
  - **Padrão central**, ligado a `weak_verificacao-valor-esperado`:
    - no caso "vence hoje", o esperado foi escrito como `0`. O aluno explicou como chegou a ele: "testando para saber qual seria o resultado esperado";
    - o tutor explicou com a analogia do troco, a mesma do `cond-05`. Depois disso, o aluno corrigiu o esperado para `1` pela regra;
    - no caso "sem data", voltou a acompanhar o código: a função passou a devolver `None`, e o `assert` esperava `None`;
    - lembrado da própria regra ("se não posso comprovar a data, ele deve ser revisado"), respondeu **1** sem rodar (degrau 3).
  - **Bloqueio aberto:** o card com `""` é contado duas vezes, porque são dois `if` separados (`== ""` e `hoje >= ""`). O tutor ligou isso ao `cond-01` de hoje (casos exclusivos → `if`/`elif`); a pergunta ficou sem resposta. O teste ainda usa `""` em vez de `None`.
  - Pré-requisito ensinado: `null` no JSON vira `None` no Python, o que é diferente de `""`.
- **Evidência: nenhuma.** Todo o trabalho no núcleo teve apontamentos de degrau 3 ou 4. Prestação de contas (regra 9): `topic_logica-algoritmos` segue em **0**. Nenhum dos dois elementos do 60 foi cumprido: nem a explicação Feynman autônoma nem a aplicação autônoma. Os pontos fracos continuam inalterados.
- **Learner profile:** uma observação. A estratégia "perguntar de onde veio o esperado + analogia do troco + lembrar a regra do próprio aluno" deu resultado positivo.
- **Próxima entrega mínima:**
  1. responder se "sem data" e "venceu" são exclusivos e escolher a estrutura;
  2. trocar `""` por `None` no teste;
  3. fazer todos os `assert` passarem com os esperados da tabela.

  Depois vêm o Feynman curto (por que o esperado vem da regra, e não do código) e o problema 2 (evidências por tópico), decomposto antes do código.
- Cards atrasados: `tempos-03..08` e `dictreader-*`.

## `session_2026-10-09-lesson15-abertura-01`

- Status: concluída, das 18:05 às 19:56 (cerca de 111 de 90 min). Fechada a pedido do aluno, que volta no domingo, 11/10.
  - `state` 209 → 221, `cards` 30 → 33, `learner-profile` 12 → 13.
  - Skill em uso: commit `bd567cd`.
- Correção de horários: 18:14, 18:17, 18:30, 18:36 e 18:38 foram estimados sem ler o relógio. A ordem dos eventos está certa; os minutos não. Os horários 18:05, 18:11, 19:01, 19:10, 19:48, 19:51 e 19:56 foram lidos do relógio.
- Lições:
  - `lesson_15-logica-decomposicao`: passa de `planned` para **`in_progress`**. Ganhou o arquivo `lessons/15-logica-decomposicao.md`.
  - `lesson_01-python-core`: cards.
- **Revisão** (`retrieval_first`; não é evidência). Os três saíram corretos, sem ajuda:
  - `cond-02` (ordem: a condição mais restrita vem primeiro);
  - `cond-03` (`if len(lista) > 0:` antes de `lista[0]`);
  - `cond-04` (gravar não tem volta; conferir antes).
  - Os três passam do passo 1 para o 2 e voltam em 16/10. Em 01/10, `cond-03` estava incorreta e `cond-04` parcial.
- **Problema 1: "quantos cards estão vencidos numa data?"** O método é decompor antes de codar.
  - **Entrada.** A primeira versão não incluía a data. Depois de uma pergunta direcional (degrau 3: "o teste daria o mesmo resultado amanhã?"), o aluno concluiu sozinho que a data deve ser parâmetro.
  - **Saída.** Primeiro misturou lista e dicionário. Depois de uma reformulação (degrau 1), ficou um inteiro.
  - **Caso-limite.** O termo não foi entendido de primeira (falha do material). O tutor reexplicou com a balança de mala (23 kg).
    - Efeito registrado: as famílias genéricas ("vazio" e "em cima da linha") foram dadas pelo tutor.
    - Achado próprio do aluno: o card **sem data**. Foi além da analogia, e o formato da skill realmente permite `due_at` nulo.
    - Regra própria, com justificativa: "se não posso comprovar a data, ele deve ser revisado".
  - **Tabela final:**

    | # | Caso | Esperado |
    |---|---|---|
    | 1 | normal | 1 |
    | 2 | vence hoje | 1 |
    | 3 | `None` | 1 |
    | 4 | `[]` | 0 |

    Na linha 4, o aluno escreveu primeiro `1` e uma mensagem ao usuário. Depois corrigiu para "zero ou `None`". O tutor explicou a diferença entre `0` e `None` e por que a mensagem pertence à tela.
  - **Pré-requisitos ensinados** (regra 7):
    - comparação de datas ISO como texto, com demonstração executada e o contraexemplo `"9/10/2026"`;
    - `date.today().isoformat()`, que fica fora da função;
    - a estrutura do arquivo (função × testes), com o exemplo `dobrar(x)`, depois de o aluno perguntar.
- **Código.** Pasta nova `E:/Lucas/Documents/segundo-cerebro/exercicios/contar_vencidos.py`, ainda sem Git. Versão atual: SHA-256 `07d6ae0a42d42b4f64101cbed1c9f929cb44d3a5cd055f44b5543e3ffe2c690f`.
  - Próprio, sem pista: laço com acumulador; guarda da lista vazia **antes** do laço; o `None` previsto.
  - Defeitos encontrados pelo tutor ao rodar:
    - comparação invertida: `hoje < card["due_at"]` conta os **não** vencidos;
    - saída em `dict` ou texto, e não em `int`;
    - `date.today()` dentro do teste;
    - a verificação de `None` depois da comparação;
    - um teste só.
  - Depois do primeiro apontamento (degrau 1), o aluno corrigiu só a chave do dicionário (`card_vencidos` × `cards_vencidos`). O teste passou **com o resultado errado**: o código e o esperado davam 2, e o certo é 4. É o padrão de `weak_verificacao-valor-esperado`.
  - Com uma tabela de contagem, card por card, montada pelo tutor (degrau 4), contou **4** na hora.
  - Ficou sem resposta a pergunta direcional da linha 18 (`"2026-10-09" < "2026-10-12"` com o `card_b`).
- **Evidência: nenhuma.** A decomposição e o código foram guiados (degraus 1 a 4). Prestação de contas (regra 9): `topic_logica-algoritmos` segue em **0**. Nenhum dos dois elementos do 60 foi cumprido: nem a explicação Feynman autônoma nem a aplicação autônoma. Os pontos fracos continuam inalterados.
- **Learner profile:** uma observação. A estratégia "teste que passa com esperado errado + tabela card a card" deu resultado positivo.
- **Próxima entrega mínima,** no domingo:
  1. corrigir o sentido da comparação da linha 18;
  2. fazer a saída ser `int`;
  3. escrever 4 `assert`, um por linha da tabela, com a data fixa `"2026-10-09"`;
  4. verificar o `None` **antes** da comparação.

  Depois vêm o Feynman curto e o problema 2 (evidências por tópico). Pendências: `git init`, o estudo fictício (`init_study`) e o remoto `segundo-cerebro`. Cards: `tempos-03..08` e `dictreader-*`.
- O aluno vai tentar corrigir no trabalho, num interpretador Python online. Pode, porque o código só tem dados fictícios. Ao voltar, deve colar a versão de lá no arquivo local, para o tutor conferir.

## Formação fechada — 2026-10-08 (`state` 207 → 209, `study-config.json`)

- Não é sessão de aprendizagem. Nenhuma evidência, domínio, ponto fraco ou sessão foi alterado.
- **Pedido do aluno.** Ele sente que estuda mas "ainda não desenvolveu nada" e quer construir o projeto desde já, usando-o para fechar a lacuna de lógica. Pediu uma avaliação sincera e um plano para seguir até o fim, sem mudanças constantes.
- **Levantamento de vagas.** Foram lidas 10 vagas completas no LinkedIn público, mais 45 títulos.
  - React + TS é o front mais comum.
  - PostgreSQL, Docker e o fluxo de PR são recorrentes.
  - IA aplicada apareceu em 3 de 10.
  - Python aparece forte em automação, integração e IA, e não como back-end de "full stack júnior".
- **Decisões do aluno:**
  - especialista em Python, automação e IA, com front e DevOps só "suficientes" (a amplitude full stack vem da faculdade de ADS);
  - o projeto passa a ser o **app da própria formação**, sobre a skill `ai-tutor`, com a aba Segundo Cérebro consultando o estudo (sem Obsidian como fonte);
  - Claude API como provedor;
  - 10 h por semana, sem dias fixos;
  - Obsidian mantido até a aba do app funcionar;
  - pediu para **fechar a formação e não permitir mudanças até o fim**.
- **Avaliação do tutor:**
  - o formato em T está alinhado ao mercado;
  - o MVP original era grande demais e foi reduzido por regras de negócio: JSON como fonte da verdade, uma única escrita (a revisão de card, pelas funções da skill), busca full-text em vez de embeddings, túnel SSH, três telas e MCP opcional;
  - faltava Python intermediário;
  - o maior risco é a carga semanal: cerca de 2,5 h por semana de 21/09 a 08/10.
- **Estado (`atomic_update_json`, 207 → 208 → 209):**
  - novos tópicos: `topic_python-intermediario`, `topic_devops-deploy` e `topic_ia-aplicada`, todos com domínio 0;
  - novas lições: `lesson_19-python-intermediario`, `lesson_18-docker-vps-deploy`, `lesson_20-llm-estruturado`, `lesson_21-rag-segundo-cerebro` e `lesson_22-agente-tutor-mcp`;
  - `lesson_09-manutencao-sonhar` → `archived`;
  - objetivos das lições `14`, `05`, `06`, `07`, `08`, `10`, `11`, `12` e `13` reancorados no app;
  - âncoras das lições `15`, `16` e `17` passam a ser o estudo fictício no repositório;
  - cadeia de pré-requisitos: 15 → 16 → 17 → 19 → 14 → 05 → 06 → 07 → 18 → 08 → 20 → 21 → 22 → 10 → 11 → 12 → 13;
  - `project_segundo-cerebro` redefinido; `project_agente-operacional` e `project_capstone-producao` arquivados (absorvidos pelo núcleo);
  - `next_focus` continua `lesson_15`.
- **`study-config.json`** (`FileLock` e substituição atômica):
  - `topic` e `goal` reescritos;
  - `weekly_hours` passou de 7 para 10;
  - `preferred_times` sem dias fixos;
  - `cycle_calendar` estendido a 20 ciclos, até 2027-10-24;
  - `deadline` reescrito.
- **Documentos:**
  - novo plano único `docs/compose/spec/formacao-fechada.md`, com MVP, regras de negócio, roteiro, regra de fechamento e o levantamento com fontes;
  - `segundo-cerebro-roadmap.md` e `bloco-logica-roadmap.md` marcados como substituídos;
  - `AGENTS.md` com a nova seção "Formação fechada", o projeto reescrito e a vigência do Obsidian até a `lesson_21`;
  - `curriculum.md` reescrito à mão.
- `validate_study`: PASS.

## Carga semanal: 8 h → 7 h — 2026-10-08 (`study-config.json`)

- Não é sessão de aprendizagem. Decisão do aluno, depois de ver a comparação com o planejamento: o conteúdo está cerca de 46 dias à frente do calendário (concluído até o ciclo 4; o calendário está no ciclo 2), mas as horas registradas caíram de 7,8–11 h por semana (31/08 a 20/09) para cerca de 2,5 h (21/09 a 08/10).
- Motivo declarado: 7 h é mais equilibrado. O estágio ainda não começou e, quando começar, fica dentro do período de trabalho, sem somar carga ao estudo.
- `weekly_hours` passou de 8 para 7, gravado com `FileLock` e substituição atômica (o arquivo não tem `revision`). `validate_study`: PASS. Calendário de ciclos, prazo e dias protegidos inalterados. A pendência "horas semanais" do `bloco-logica-roadmap.md` foi fechada.
- Projeção do tutor: os ciclos foram dimensionados para cerca de 24 h (8 h × 3 semanas); com 7 h, cada ciclo leva uns 3,4 dias a mais. Nos 12 ciclos restantes, isso consome cerca de 41 dos 46 dias de folga, desde que as 7 h sejam cumpridas.

## `session_2026-10-08-diagnostico-logica-01`

- Status: concluída (começou às 16:25 e terminou antes das 17:37, cerca de 70 de 90 min). `state` 188 → 207, `cards` 25 → 30, `learner-profile` 10 → 12. Skill em uso: commit `bd567cd`.
- Correção de horários (revisões 207/30/12): os horários intermediários gravados a partir de 16:38 foram estimados pelo tutor sem consultar o relógio e ficaram adiantados (iam até 17:52). Os registros posteriores a 17:37 foram limitados a 17:37, a hora real da correção.
- Lições: `lesson_15-logica-decomposicao` (diagnóstico; segue `planned`) e `lesson_02-arquivos-erros` (cards).
- Objetivo: retomar e concluir o `diagnostic_2026-10-06-logica-01`; depois, recuperar `cond-01` e `cond-05` (`retrieval_first`). O aluno pediu para seguir com `tempos-01..03`.
- **Diagnóstico** (não é evidência, não altera domínio). Concluído com estimativa `partial`, confiança `medium`, e `entry_topic_id: topic_logica-algoritmos`.

  | Sondagem | Observado | Estimativa |
  |---|---|---|
  | 1. Decompor a contagem de tags, sem código | Saída em dicionário `tag → contagem`, acumulador e nota vazia percebidos sem pista; lista de tags assumida como entrada pronta; laço ambíguo; valores deixados como `n` | `partial` |
  | 1b. Dicionário final com números | Mudou a forma da saída e não deu números; o aluno disse depois que não entendeu a pergunta (falha do material) | `weak`, `low` |
  | 1c–1d. Contar `python`; dicionário completo | `A, B, D`; `{"python": 3, "estudo": 2, "git": 1}` | `likely_known` |
  | 2. Prever o laço com acumulador e `if`/`else` | Descreveu a regra ("quase um caixa registrador"), sem dar o valor | `partial` |
  | 2b. Rastrear com a tabela fornecida | 12 → 11 → 41 → 40, correto | `likely_known`, `medium` |
  | 3. `contar_tags` em `formação_python/src/logica/exe_01.py` | Laço aninhado e acumuladores corretos, sem pista; tags fixas no código; chave `pyhton`; declarado concluído sem comparar com o esperado | `partial`, `high` |
  | 4–4b. Comparar a saída com o esperado | Primeiro apontou as aspas (lacuna do material, ensinada); com pista direcional, achou `pyhton`, corrigiu no `return` e rodou de novo | `weak` → `partial` |

  Ponto de entrada da `lesson_15`: laço, acumulador e `if` já servem de base. Focar em (1) exemplos com a saída esperada **em números** antes do código; (2) comparação explícita com `assert`; (3) tabela de rastreio montada pelo aluno; (4) generalizar, montando o dicionário com chave nova (ensinar antes, regra 1; ponte para a `lesson_16`).
- **Cards** (recuperação; não é evidência):
  - `cond-01`: correto, sem ajuda. Passo 0 → 1; volta em 11/10.
  - `cond-05`: correto, sem ajuda. É o primeiro acerto em quatro revisões. Na pergunta seguinte, sobre o que provaria a transformação (degrau 2), respondeu certo: "teste com o formato de saída desejado". Passo 0 → 1; volta em 11/10.
  - `tempos-01`: correto, sem ajuda (sintaxe × exceção). Passo 1 → 2; volta em 15/10.
  - `tempos-02`: respondeu sobre a **presença** do traceback. Depois da reformulação (degrau 1), ficou parcial: acertou "nem chegou a rodar", mas justificou com nome desconhecido, que é `NameError`. É a mesma confusão de `weak_error-model-tempo-deteccao`. O tutor explicou com a analogia do teatro e uma demonstração executada (`sintaxe.py` × `nome.py`). A checagem com `print(x +)` saiu correta, mas guiada (degrau 6). Fica no passo 2; volta em 15/10.
  - `tempos-03`: adiado.
- Evidências: nenhuma. Domínio inalterado. Os pontos fracos `weak_verificacao-valor-esperado`, `weak_condicionais-ordem-guarda` e `weak_error-model-tempo-deteccao` seguem ativos.
- Perfil: uma observação `strategy_outcome`. Pedir o valor concreto de forma explícita funcionou depois das respostas descritivas.
- Próximo passo: abrir a `lesson_15` com aula antes de avaliar, nos quatro focos acima. Cards vencidos: `tempos-03..08`, os três de `dictreader` (08/10) e `cond-02..04` (09/10).

## IDs herdados renomeados — 2026-10-08 (`state` 187 → 188, `sources` 5 → 6)

- Não é sessão de aprendizagem. Pedido do aluno, depois da revisão de 07/10: os IDs vinham do roteiro anterior a 05/10 e não diziam o que a lição ou o tópico cobrem. Nenhuma das lições tinha começado; nenhum dos tópicos tinha evidência.

  | Antigo | Novo |
  |---|---|
  | `topic_apis-backend` | `topic_sql-relacional` |
  | `topic_llm-aplicacoes` | `topic_http-apis` |
  | `topic_agentes-ferramentas` | `topic_integracao-fastapi` |
  | `topic_producao-empregabilidade` | `topic_selenium-qualidade` |
  | `lesson_05-automacao-confiavel` | `lesson_05-sql-memorias` |
  | `lesson_08-llm-estruturado` | `lesson_08-selenium-captura` |
  | `lesson_09-seguranca-custo` | `lesson_09-manutencao-sonhar` |
  | `lesson_10-agente-ferramentas` | `lesson_10-react-typescript-1` |
  | `lesson_11-agente-controle` | `lesson_11-react-typescript-2` |
  | `lesson_12-docker-ci` | `lesson_12-qualidade-ci` |
  | `lesson_13-deploy-portfolio` | `lesson_13-portfolio` |

- No `state.json` havia só referências exatas (35, em IDs, pré-requisitos e ligações lição → tópico), trocadas com `atomic_update_json`. Cada item renomeado ganhou `former_id` e uma nota em `progress_note`. Em `sources.json`, foram trocadas as ligações e duas menções em `authority_reason`. `validate_study`: PASS.
- `curriculum.md` e `docs/compose/spec/segundo-cerebro-roadmap.md` foram atualizados. As entradas antigas deste log ficam com os IDs da época.
- Fora deste repositório, não alterado: o Python Lab (`E:\Lucas\Documents\python-lab`, só referência por decisão de 04/10) ainda usa os IDs antigos em `data/roadmap.json` e nas missões 010 e 011.
- Também em 07/10: plano de correção do estudo "Fundamentos da Engenharia de IA" escrito no próprio projeto (`docs/plano-correcao-estado.md`), para ser executado lá.

## Manutenção da formação e da skill — 2026-10-07 (`state` 185 → 187, `cards` → 25, `sources` → 5, `learner-profile` → 10)

- Não é sessão de aprendizagem. Nenhuma evidência, domínio, sessão ou condição de saída de ponto fraco foi alterada. Executado a pedido do aluno, a partir de uma revisão da formação e da skill.
- **Skill versionada.** A onda adaptativa existia só na pasta instalada; o GitHub (`14lucas-mendes/ai-tutor-skill`) tinha parado na v2. Publicada no PR [14lucas-mendes/ai-tutor-skill#1](https://github.com/14lucas-mendes/ai-tutor-skill/pull/1), com CI verde em Windows, Linux e macOS. A pasta instalada virou um clone do repositório (backup em `C:\Users\lucka\skill-backups\installed-pre-git-20261007-224824`). A junction do Claude continua apontando para ela.
- **Correções na skill**, no PR [14lucas-mendes/ai-tutor-skill#2](https://github.com/14lucas-mendes/ai-tutor-skill/pull/2):
  - o resumo do perfil passa a usar a taxa de acerto, e não a contagem;
  - o validador rejeita observações com a chave errada;
  - o gerador de projeções preserva arquivos escritos à mão.
- **Skill em uso: commit `bd567cd`.** Na skill, 136 testes OK e `validate_skill` PASS; no estudo, `validate_study` PASS. Daqui em diante, o alinhamento registra o commit, não os hashes (histórico em `docs/compose/historico-alinhamento-skill.md`).
- **Perfil:** a migração renomeou `support_level` → `help_level` numa observação de 01/10 e recalculou o resumo: `autonomy` foi de `low` para `medium` (uma tentativa autônoma correta e uma parcial); `help_dependency` segue `medium`. O perfil não é evidência e não muda domínio.
- **Tópico renomeado:** `topic_python-fundamentos` passou de "Logica, decomposicao e Python core" para "Python core e programas pequenos testaveis", para não se confundir com `topic_logica-algoritmos`. Domínio 80 e evidências inalterados. Os IDs herdados do roteiro antigo (`topic_llm-aplicacoes` = HTTP e APIs, `lesson_08-llm-estruturado` = Selenium etc.) continuam; os nomes e as ligações lição → tópico já estavam corretos desde 05/10.
- **Cards:** foram importados para `cards.json` os 10 cards de rascunho da `lesson_02` (pacote de mídia de 18/09). O verso de `card_print-return-01` foi corrigido: a mensagem do `print` aparece na tela; quem não recebe nada é o código que chamou. Foram criados 6 cards da `lesson_04` (família `git remote`, `-v`, `--oneline`, `diff` × `diff --staged`, `push -u` e `origin/master..HEAD`), conferidos na documentação oficial e registrados como 4 fontes novas (`source_git-*`). As primeiras revisões ficam espalhadas de 08/10 a 12/10. Cards não são evidência. O `flashcards.md` foi regenerado pelo script.
- **`lesson_15`:** `programming_plan.weak_point_exits` liga `weak_verificacao-valor-esperado`, `weak_condicionais-ordem-guarda` e `weak_python-test-literal-lista` às tarefas da lição. As condições de saída não mudaram.
- **Regras:** o `AGENTS.md` passou a ser a única fonte. Os quatro arquivos de `.cursor/rules/` (que tinham divergido: nome do diário com underscore, mídia sem a ampliação de 02/10, regra 10 só no Cursor) viraram um só, que aponta para ele. A regra 10 entrou no `AGENTS.md`.
- Em aberto, para decisão do aluno: o estudo "Fundamentos da Engenharia de IA" falha no `validate_study` (diagnóstico gravado como evidência, referência `conversation`, campos do ponto fraco), e não foi alterado.

## Revisão de roadmap: bloco de lógica — 2026-10-06 (`revision` 183 → 184)

- Não é sessão de aprendizagem. Nenhuma evidência, domínio, ponto fraco ou sessão foi alterado.
- Pedido do aluno: muita dificuldade em lógica de programação, principalmente em juntar listas, dicionários, condicionais e laços, decompor um problema antes de começar, saber o que esperar de entrada e saída, e debugar. A dificuldade apareceu nas missões do Python Lab. Contexto: começou um estágio em análise e desenvolvimento de sistemas (departamento GFI, stack e carga horária ainda indefinidas). Está lendo *Entendendo Algoritmos* (Aditya Bhargava) e *Estruturas de Dados e Algoritmos com JavaScript* (Loiane Groner). Aceitou estender a formação.
- Leitura do tutor: o 80 de `topic_python-fundamentos` mede peças isoladas; compor essas peças é outra capacidade, ainda não ensinada (lacuna do material). Sinais nos registros: 4 dos 6 pontos fracos ativos são conceituais, e o `cond-05` repetiu o mesmo raciocínio três vezes.
- Aprovado pelo aluno (`docs/compose/spec/bloco-logica-roadmap.md`):
  - novo `topic_logica-algoritmos`, com domínio 0;
  - `lesson_15-logica-decomposicao`, `lesson_16-estruturas-dados` e `lesson_17-algoritmos-debugging`, uma por ciclo (ciclos 5 a 7);
  - a `lesson_14` passa a depender da `lesson_17`, e `topic_apis-backend` passa a ter o novo tópico como pré-requisito;
  - `next_focus` passa a ser a `lesson_15`.
- Prática sugerida em cada lição: missões do Python Lab (só referência, sem sincronizar, conforme a decisão de 04/10) e capítulos dos dois livros.
- `study-config.json`: 16 ciclos, até 01/08/2027 (antes, 13 ciclos até 30/05/2027). Gravado com `FileLock` mais substituição atômica, porque o arquivo não tem `revision`. `state.json` foi gravado via `atomic_update_json` com `expected_revision=183`. `validate_study`: PASS.
- `curriculum.md` foi atualizado à mão (calendário e tabela de ciclos renumerada). `scripts.projections` não foi executado.
- Em aberto: horas semanais (continuam 8 h até o estágio definir a carga) e o estágio como contexto de transferência quando a stack for conhecida. Dados da empresa nunca entram no estudo.
- Próximo passo: `/diagnostic` curto de lógica, para posicionar o início da `lesson_15`.

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
- `README.md` commitado e enviado pelo aluno depois do fechamento: `1739cc4`.
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
