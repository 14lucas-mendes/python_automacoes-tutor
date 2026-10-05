# Verified Source Pack

## 4. More Control Flow Tools (The Python Tutorial)

- Source ID: `source_python-controlflow`
- URL: https://docs.python.org/3/tutorial/controlflow.html

Resumo pedagogico (parafraseado, verificado por execucao em Python 3.11): uma sequencia if/elif/else testa as condicoes de cima para baixo e executa somente o bloco da primeira condicao verdadeira; as demais nao sao testadas. O else roda quando nenhuma foi verdadeira. if separados sao avaliados todos, um apos o outro. O match compara um valor com padroes (case) na ordem escrita e executa o primeiro que casar; o padrao curinga _ casa com qualquer valor e, por isso, precisa ser o ultimo: colocado antes de outros case, o Python recusa o codigo com SyntaxError ('wildcard makes remaining patterns unreachable'). Quando as condicoes se sobrepoem (toda nota >= 9 tambem e >= 5), a mais especifica deve vir primeiro.

## Built-in Types - Boolean Operations (and, or, not)

- Source ID: `source_python-boolean-ops`
- URL: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

Resumo pedagogico (parafraseado, verificado por execucao): 'x and y' avalia x primeiro; se x for falso, devolve x e nunca avalia y. 'x or y' avalia x; se x for verdadeiro, nunca avalia y. Esse curto-circuito permite escrever uma guarda antes do uso: em 'len(fila) > 0 and fila[0] == "Ana"', com a lista vazia o Python para no primeiro operando e nao chega a fila[0], evitando IndexError.

## 8. Errors and Exceptions (The Python Tutorial)

- Source ID: `source_python-errors-exceptions`
- URL: https://docs.python.org/3/tutorial/errors.html

Resumo pedagogico (parafraseado): erros de sintaxe sao detectados antes da execucao; excecoes, como IndexError, sao levantadas durante a execucao, no momento em que a operacao invalida acontece (por exemplo, acessar lista[0] numa lista vazia). Tudo o que rodou antes dessa linha ja aconteceu, inclusive gravacoes em arquivo; por isso uma acao irreversivel deve vir depois das verificacoes.
