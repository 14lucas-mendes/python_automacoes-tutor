# Registro de sessões

<!-- Projeção legível mantida à mão. NÃO execute `python -m scripts.projections` neste
     estudo: o gerador reescreve session-log.md sem condição e substituiria toda esta
     narrativa por um resumo mecânico de 6 linhas por sessão. -->

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
