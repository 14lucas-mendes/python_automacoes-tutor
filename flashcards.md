# Flashcards

<!-- Generated from .ai-tutor/cards.json. Edit the canonical JSON, then sync. -->

## card_tempos-01

**Frente:** Quais sao os dois tipos de erro que o Python distingue?

**Verso:** Erros de sintaxe, detectados na analise do codigo antes de executar, e excecoes, levantadas durante a execucao.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `new`
- Próxima revisão: `2026-09-13`
- Intervalo: `1 dias`

## card_tempos-02

**Frente:** A mensagem de erro nao traz o cabecalho "Traceback (most recent call last)". O que isso prova?

**Verso:** Que o codigo foi reprovado na analise. Nenhuma linha executou, por isso nao existe rastro de chamadas.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`, `source_python-traceback`
- Status: `new`
- Próxima revisão: `2026-09-13`
- Intervalo: `1 dias`

## card_tempos-03

**Frente:** O que a ultima linha de uma mensagem de erro informa, e o que informa o bloco acima dela?

**Verso:** A ultima linha informa o tipo da excecao e o detalhe. O bloco acima e o stack traceback: arquivo, linha e a cadeia de chamadas, lida de cima para baixo.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`, `source_python-traceback`
- Status: `new`
- Próxima revisão: `2026-09-13`
- Intervalo: `1 dias`

## card_tempos-04

**Frente:** NameError significa o que?

**Verso:** O nome usado nao existe ou nao foi definido naquele ponto. Exemplo da documentacao: 4 + spam*3 levanta NameError: name 'spam' is not defined.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `new`
- Próxima revisão: `2026-09-13`
- Intervalo: `1 dias`

## card_tempos-05

**Frente:** TypeError significa o que?

**Verso:** O nome existe, mas o valor tem tipo incompativel com a operacao. Exemplo da documentacao: '2' + 2 levanta TypeError: can only concatenate str (not "int") to str.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `new`
- Próxima revisão: `2026-09-13`
- Intervalo: `1 dias`

## card_tempos-06

**Frente:** O que uma funcao Python devolve quando termina sem `return`?

**Verso:** None, automaticamente. O calculo pode ter acontecido, mas nao sai da funcao, e o chamador recebe None sem nenhum aviso.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `new`
- Próxima revisão: `2026-09-13`
- Intervalo: `1 dias`

## card_tempos-07

**Frente:** Uma variavel recebeu None de uma funcao. O que acontece ao concatena-la com um texto?

**Verso:** TypeError: can only concatenate str (not "NoneType") to str. None e um valor, do tipo NoneType, nao a ausencia de uma atribuicao.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `new`
- Próxima revisão: `2026-09-13`
- Intervalo: `1 dias`

## card_tempos-08

**Frente:** A linha apontada pelo traceback e sempre a linha do defeito?

**Verso:** Nao. A linha apontada e onde a operacao falhou; a causa pode estar em outra funcao. No caso praticado, o erro apareceu em relatorio e o defeito era o return ausente em tempo_medio.

- Tópico: `topic_python-fundamentos`
- Lição: `lesson_03-testes-git`
- Fontes: `source_python-errors-exceptions`
- Status: `new`
- Próxima revisão: `2026-09-13`
- Intervalo: `1 dias`
