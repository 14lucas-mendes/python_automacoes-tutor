# Flashcards

<!-- Generated from .ai-tutor/cards.json. Edit the canonical JSON, then sync. -->

## card_tempos-01

**Frente:** Quais sao os dois tipos de erro que o Python distingue?

**Verso:** Erros de sintaxe, detectados na analise do codigo antes de executar, e excecoes, levantadas durante a execucao.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `review`
- Próxima revisão: `2026-10-15`
- Intervalo: `7 dias`

## card_tempos-02

**Frente:** A mensagem de erro nao traz o cabecalho "Traceback (most recent call last)". O que isso prova?

**Verso:** Que o codigo foi reprovado na analise. Nenhuma linha executou, por isso nao existe rastro de chamadas.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`, `source_python-traceback`
- Status: `review`
- Próxima revisão: `2026-10-15`
- Intervalo: `7 dias`

## card_tempos-03

**Frente:** O que a ultima linha de uma mensagem de erro informa, e o que informa o bloco acima dela?

**Verso:** A ultima linha informa o tipo da excecao e o detalhe. O bloco acima e o stack traceback: arquivo, linha e a cadeia de chamadas, lida de cima para baixo.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`, `source_python-traceback`
- Status: `review`
- Próxima revisão: `2026-10-24`
- Intervalo: `7 dias`

## card_tempos-04

**Frente:** NameError significa o que?

**Verso:** O nome usado nao existe ou nao foi definido naquele ponto. Exemplo da documentacao: 4 + spam*3 levanta NameError: name 'spam' is not defined.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `review`
- Próxima revisão: `2026-10-22`
- Intervalo: `3 dias`

## card_tempos-05

**Frente:** TypeError significa o que?

**Verso:** O nome existe, mas o valor tem tipo incompativel com a operacao. Exemplo da documentacao: '2' + 2 levanta TypeError: can only concatenate str (not "int") to str.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `review`
- Próxima revisão: `2026-10-01`
- Intervalo: `3 dias`

## card_tempos-06

**Frente:** O que uma funcao Python devolve quando termina sem `return`?

**Verso:** None, automaticamente. O calculo pode ter acontecido, mas nao sai da funcao, e o chamador recebe None sem nenhum aviso.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `review`
- Próxima revisão: `2026-10-01`
- Intervalo: `3 dias`

## card_tempos-07

**Frente:** Uma variavel recebeu None de uma funcao. O que acontece ao concatena-la com um texto?

**Verso:** TypeError: can only concatenate str (not "NoneType") to str. None e um valor, do tipo NoneType, nao a ausencia de uma atribuicao.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `review`
- Próxima revisão: `2026-10-01`
- Intervalo: `3 dias`

## card_tempos-08

**Frente:** A linha apontada pelo traceback e sempre a linha do defeito?

**Verso:** Nao. A linha apontada e onde a operacao falhou; a causa pode estar em outra funcao. No caso praticado, o erro apareceu em relatorio e o defeito era o return ausente em tempo_medio.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `review`
- Próxima revisão: `2026-10-06`
- Intervalo: `7 dias`

## card_cond-01

**Frente:** Duas situacoes podem acontecer juntas (tem cafe, tem pao). Uso if separados ou if/elif? E se for uma OU outra?

**Verso:** Se podem acontecer juntas: if separados (o Python testa todos). Se sao exclusivas: if/elif/else ou match (para no primeiro verdadeiro).

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_01-python-core`
- Fontes: `source_python-controlflow`
- Status: `learning`
- Próxima revisão: `2026-10-22`
- Intervalo: `3 dias`

## card_cond-02

**Frente:** Em `if nota >= 5: ... elif nota >= 9: ...`, por que 'louvor' nunca aparece? Qual a regra de ordem?

**Verso:** Toda nota >= 9 tambem e >= 5, entao a primeira condicao sempre ganha. Com condicoes sobrepostas, a mais especifica vem primeiro.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_01-python-core`
- Fontes: `source_python-controlflow`
- Status: `learning`
- Próxima revisão: `2026-10-16`
- Intervalo: `7 dias`

## card_cond-03

**Frente:** Antes de usar lista[0], o que e preciso garantir? Escreva a condicao que protege.

**Verso:** Que a lista nao esta vazia. Ex.: if len(lista) > 0 and lista[0] == esperado: - o and para no primeiro False e nunca acessa lista[0] (curto-circuito).

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_01-python-core`
- Fontes: `source_python-boolean-ops`
- Status: `learning`
- Próxima revisão: `2026-10-16`
- Intervalo: `7 dias`

## card_cond-04

**Frente:** Por que gravar o arquivo antes de verificar o resultado e um problema? Qual a ordem certa?

**Verso:** Se a verificacao falhar, o arquivo errado ja substituiu o bom. Ordem: tratar falhas -> transformar -> verificar -> so entao gravar (acao irreversivel por ultimo).

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_01-python-core`
- Fontes: `source_python-controlflow`
- Status: `learning`
- Próxima revisão: `2026-10-16`
- Intervalo: `7 dias`

## card_cond-05

**Frente:** Comparar o JSON lido de volta com a mesma lista prova que a transformacao esta certa? O que prova?

**Verso:** Nao: so prova que o arquivo guardou o que recebeu. Prova a transformacao comparar com um valor esperado escrito a mao a partir da fonte (ex.: OS-101 com 3 pecas) - o troco calculado de cabeca.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-csv-module`
- Status: `learning`
- Próxima revisão: `2026-10-18`
- Intervalo: `7 dias`

## card_dictreader-chaves-01

**Frente:** No csv.DictReader, o que vira as CHAVES de cada linha?

**Verso:** Os nomes das colunas, tirados da primeira linha do arquivo quando fieldnames nao e passado. Essa primeira linha e omitida dos resultados.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-csv-module`
- Status: `new`
- Próxima revisão: `2026-10-08`
- Intervalo: `1 dias`

## card_dictreader-fieldnames-01

**Frente:** Se voce passa fieldnames explicitamente para o DictReader, o que acontece com a primeira linha do arquivo?

**Verso:** Ela deixa de ser omitida: entra nos resultados como um registro, porque os nomes ja foram dados por voce.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-csv-module`
- Status: `new`
- Próxima revisão: `2026-10-08`
- Intervalo: `1 dias`

## card_dictreader-restval-01

**Frente:** Uma linha tem MENOS celulas que o cabecalho. O que o DictReader coloca na chave que ficou sem valor?

**Verso:** None, que e o valor padrao de restval.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-csv-module`
- Status: `new`
- Próxima revisão: `2026-10-08`
- Intervalo: `1 dias`

## card_dictreader-restkey-01

**Frente:** Uma linha tem MAIS celulas que o cabecalho. Onde o excedente aparece no dicionario?

**Verso:** Numa chave literalmente chamada None, que e o restkey padrao, guardando a lista de excedentes.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-csv-module`
- Status: `new`
- Próxima revisão: `2026-10-09`
- Intervalo: `1 dias`

## card_reader-tipos-01

**Frente:** O leitor de CSV converte '4.5' em numero automaticamente?

**Verso:** Nao. Toda celula chega como str, nos dois leitores; a conversao com int() ou float() e sua.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-csv-module`
- Status: `new`
- Próxima revisão: `2026-10-09`
- Intervalo: `1 dias`

## card_dictreader-fieldnames-02

**Frente:** Como obter a lista de nomes das colunas de um DictReader, e o que ela vale num arquivo vazio?

**Verso:** Pelo atributo fieldnames do leitor. Num arquivo vazio, fieldnames e None; num arquivo so com cabecalho, e a lista dos nomes.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-csv-module`
- Status: `new`
- Próxima revisão: `2026-10-09`
- Intervalo: `1 dias`

## card_next-default-01

**Frente:** O que acontece ao chamar next(leitor) num arquivo vazio, e como evitar?

**Verso:** Levanta StopIteration, que nao e FileNotFoundError. Passando um valor padrao, next(leitor, None), o retorno e None em vez de erro.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-builtins`, `source_python-csv-module`
- Status: `new`
- Próxima revisão: `2026-10-10`
- Intervalo: `1 dias`

## card_fatiar-pop-01

**Frente:** Qual a diferenca entre result[1:] e result.pop(0)?

**Verso:** Fatiar devolve uma lista nova e deixa a original inteira; pop modifica a lista e devolve o item retirado.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-datastructures`
- Status: `new`
- Próxima revisão: `2026-10-10`
- Intervalo: `1 dias`

## card_main-guard-01

**Frente:** Para que serve if __name__ == "__main__"?

**Verso:** Para o arquivo servir como script e como modulo: o bloco abaixo roda quando o arquivo e executado direto e nao roda quando ele e importado.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-modules`
- Status: `new`
- Próxima revisão: `2026-10-10`
- Intervalo: `1 dias`

## card_print-return-01

**Frente:** Por que imprimir dentro da funcao nao substitui devolver o valor?

**Verso:** Porque print so mostra a mensagem na tela: o codigo que chamou a funcao nao recebe nada, e a chamada devolve None. Para quem chamou usar o resultado, a funcao precisa de return.

- Tópico: `topic_automacao-confiavel`
- Lição: `lesson_02-arquivos-erros`
- Fontes: `source_python-datastructures`
- Status: `new`
- Próxima revisão: `2026-10-11`
- Intervalo: `1 dias`

## card_git-remote-familia-01

**Frente:** Qual subcomando cria um remoto novo e qual corrige a URL de um remoto que ja existe?

**Verso:** git remote add origin <URL> cria; git remote set-url origin <URL> corrige a URL. Nao existe git remote edit.

- Tópico: `topic_workflow-profissional`
- Lição: `lesson_04-descoberta-processo`
- Fontes: `source_git-remote`
- Status: `new`
- Próxima revisão: `2026-10-22`
- Intervalo: `3 dias`

## card_git-remote-v-01

**Frente:** Como listar os remotos do repositorio junto com as URLs?

**Verso:** git remote -v (o -v vem entre remote e o subcomando, quando houver um).

- Tópico: `topic_workflow-profissional`
- Lição: `lesson_04-descoberta-processo`
- Fontes: `source_git-remote`
- Status: `new`
- Próxima revisão: `2026-10-26`
- Intervalo: `7 dias`

## card_git-log-oneline-01

**Frente:** Qual flag do git log mostra cada commit numa linha so? Escreva a forma exata.

**Verso:** --oneline, tudo junto (atalho de --pretty=oneline --abbrev-commit). --one-line nao existe.

- Tópico: `topic_workflow-profissional`
- Lição: `lesson_04-descoberta-processo`
- Fontes: `source_git-log`
- Status: `new`
- Próxima revisão: `2026-10-12`
- Intervalo: `1 dias`

## card_git-diff-staged-01

**Frente:** O que git diff compara sem argumentos? E git diff --staged?

**Verso:** Sem argumentos: arvore de trabalho x indice (o que ainda nao foi preparado). --staged (igual a --cached): indice x ultimo commit (o que vai entrar no proximo commit).

- Tópico: `topic_workflow-profissional`
- Lição: `lesson_04-descoberta-processo`
- Fontes: `source_git-diff`
- Status: `new`
- Próxima revisão: `2026-10-12`
- Intervalo: `1 dias`

## card_git-push-u-01

**Frente:** O que o -u faz em git push -u origin master?

**Verso:** Registra origin/master como branch rastreada (upstream) da branch local; depois, git pull e git status usam esse vinculo sem precisar repetir o remoto.

- Tópico: `topic_workflow-profissional`
- Lição: `lesson_04-descoberta-processo`
- Fontes: `source_git-push`
- Status: `new`
- Próxima revisão: `2026-10-26`
- Intervalo: `7 dias`

## card_git-log-intervalo-01

**Frente:** O que mostra git log --oneline origin/master..HEAD?

**Verso:** Os commits que estao no HEAD local e ainda nao estao em origin/master, ou seja, o que ainda nao subiu.

- Tópico: `topic_workflow-profissional`
- Lição: `lesson_04-descoberta-processo`
- Fontes: `source_git-log`
- Status: `new`
- Próxima revisão: `2026-10-12`
- Intervalo: `1 dias`
