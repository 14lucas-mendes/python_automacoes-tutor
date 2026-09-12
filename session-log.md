# Registro de sessões

## `session_2026-09-10-debugging-01`

- Status: em andamento
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
