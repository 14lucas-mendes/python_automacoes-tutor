# Verified Source Pack

## Python Language Reference: The assert statement

- Source ID: `source_python-assert`
- URL: https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement

Assert statements are a convenient way to insert debugging assertions into a program. The simple form, assert expression, is equivalent to: if __debug__: if not expression: raise AssertionError. The extended form, assert expression1, expression2, raises AssertionError(expression2) when expression1 is false, so the second expression works as the failure message. When Python runs with optimization (-O), assert statements are not executed. In this study: an assert compares the value obtained from the code with the value expected from the rule; when it passes it is silent.

## Python Standard Library: Boolean Operations - and, or, not

- Source ID: `source_python-boolean-ops`
- URL: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

x or y: if x is true, then x, else y. This is a short-circuit operator: it only evaluates the second argument if the first one is false. x and y: if x is false, then x, else y. It only evaluates the second argument if the first one is true. not x: if x is false, then True, else False. Short-circuit evaluation is what makes a guard work: in card['due_at'] == None or card['due_at'] <= hoje, the comparison on the right never runs when the left side is True.

## Python Tutorial: More Control Flow Tools

- Source ID: `source_python-controlflow`
- URL: https://docs.python.org/3/tutorial/controlflow.html

An if statement can have zero or more elif parts and an optional else part; the conditions are tested in order and only the first true branch runs. Python's for statement iterates over the items of any sequence in the order they appear; iterating over an empty list runs the body zero times. The break statement breaks out of the innermost enclosing for or while loop. The continue statement continues with the next iteration of the loop. The return statement returns with a value from a function and ends the function at that point; a function without return gives None. Functions can define default argument values, such as rastrear=False.

## Python Tutorial: Data Structures

- Source ID: `source_python-datastructures`
- URL: https://docs.python.org/3/tutorial/datastructures.html

A dictionary is a set of key: value pairs with unique keys. Storing a value with d[key] = value creates or replaces the key; reading d[key] when the key does not exist raises KeyError. The expression key in d checks whether a single key is in the dictionary (keys only, not values); not in is the opposite. Sequence objects are compared lexicographically, item by item from the left; strings compare character by character, which is why ISO dates written as AAAA-MM-DD can be compared as text with <, <= and >. An empty list [] is not equal to an empty string ''.

## Python Tutorial: Modules - Executing modules as scripts

- Source ID: `source_python-modules`
- URL: https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts

When you run a Python module with python fibo.py, the code in the module is executed just as if you imported it, but with __name__ set to "__main__". By adding if __name__ == "__main__": at the end of the module, the code under it only runs when the file is executed as the main file and not when the module is imported. Comparing __name__ with the text "__name__" is never true when the file is run, so a block guarded that way never executes.

## Registro do estudo: percurso e dificuldades da lesson_15 (09/10 a 23/10/2026)

- Source ID: `study_lesson15-percurso`
- URL: lessons/15-logica-decomposicao.md (estudo local python_automacoes-tutor)

Licao 15, decompor, planejar e rastrear, concluida em 23/10/2026 com logica em 80. Metodo: entrada, regra, saida, exemplos com o esperado calculado a mao (com casos-limite), plano em portugues, codigo, um assert por exemplo e tabela de rastreio conferida por execucao.

Dificuldades e como foram resolvidas, em ordem:
1. 09-11/10, problema 1 (cards vencidos): o esperado era tirado da execucao do proprio codigo, e uma comparacao invertida coincidiu com um esperado errado. Resolvido com a regra: o esperado vem da regra, o obtido vem do codigo. Usar '' no lugar de None no teste mascarava o caso sem data.
2. 12/10: na ordem invertida (<= antes de == None), previu que passaria; deu TypeError. Aprendeu o curto-circuito: or para no primeiro True, and para no primeiro False. A guarda vem antes da comparacao impossivel.
3. 13-16/10, problema 2 (evidencias por topico): um contador unico para todos os topicos; precisou de uma gaveta (chave) por topico, criada a partir da entrada. Chave nova: d[k] = 0 cria, d[k] += 1 soma, KeyError se nao existe. No caso vazio inventou {'lista': 0}, fora do contrato da saida. Achou que o corpo do laco rodava com a lista vazia (roda zero vezes).
4. 17-19/10, problema 3 (pontos fracos ativos): a decomposicao precisou de ajuda; o codigo autonomo esqueceu duas exclusoes da regra; return {} dentro do laco encerrava a funcao cedo.
5. 20/10, problema 4 (vencidos por status): primeira aplicacao padrao inteira sozinho, com previsao e tabela certas. Logica 40 -> 60.
6. 22/10, transferencia 'classificar ordens de servico': ordem das regras certa sem pista, mas if __name__ == '__name__' fazia os asserts nunca rodarem e 'Todos os testes passaram' aparecia sempre; o esperado do caso preventiva com item bloqueado contradizia a propria ordem (o certo era 'bloqueada'); ordem['itens'] == '' deixava a lista vazia [] passar (StopIteration); textos fora do contrato ('bloqueado', 'adiministrativa'). Conferencia generica pedida: considerou completo.
7. 23/10: v2 guiada corrigiu os 7 itens; depois a tarefa 2 'filas do fim de turno' (contar_filas) saiu autonoma e correta: status antes das pecas, 'pecas' not in ordem antes do acesso, peca zerada antes do resto, 5 asserts no bloco main, previsao e rastreio certos. Logica 60 -> 80.

Licoes que ficaram: o esperado sai da regra; guarda antes do acesso; regra especifica antes da geral; o silencio dos testes so vale se eles rodarem; caso-limite que fica so na tabela nao protege nada; 'exclusivas' quer dizer que so uma acontece (if/elif).
