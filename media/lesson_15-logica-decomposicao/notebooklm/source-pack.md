# Verified Source Pack

## 7.3. The assert statement (The Python Language Reference)

- Source ID: `source_python-assert`
- URL: https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement

Resumo pedagogico (parafraseado, verificado por execucao em Python 3.11): 'assert expressao1, expressao2' equivale a 'se expressao1 for falsa, levante AssertionError com expressao2 como mensagem' (enquanto __debug__ for verdadeiro, o que e o normal; com a opcao -O os asserts sao removidos). O assert so compara: ele nao sabe qual valor e o correto. Por isso o valor esperado precisa vir de uma fonte independente do codigo testado, isto e, da regra calculada a mao antes de rodar. Se o esperado for copiado da execucao do proprio codigo, o teste compara o codigo com ele mesmo e passa mesmo quando a regra foi violada (caso observado: contar_vencidos devolvia 2 e o esperado escrito era 2; contando card por card, o certo era 4). Quando um assert falha, o programa para naquela linha com AssertionError; o que se investiga primeiro e o codigo, e o esperado so muda se a propria regra estiver errada. Cada caso de uma tabela de exemplos vira um assert com sua propria lista pequena escrita dentro da chamada, por exemplo contar_vencidos([], '2026-10-09') == 0 e contar_vencidos([{'card_id': 'a', 'due_at': '2026-10-05'}], '2026-10-09') == 1; envolver a lista com str() ou int() muda o tipo do dado (str([]) e o texto '[]'; int([]) levanta TypeError).

## 4. More Control Flow Tools (The Python Tutorial)

- Source ID: `source_python-controlflow`
- URL: https://docs.python.org/3/tutorial/controlflow.html

Resumo pedagogico (parafraseado, verificado por execucao em Python 3.11): uma sequencia if/elif/else testa as condicoes de cima para baixo e executa somente o bloco da primeira condicao verdadeira; as demais nao sao testadas. if separados sao avaliados todos, um apos o outro, entao um mesmo item pode entrar em mais de um bloco. Exemplo: com if valor == 0 (brinde) e outro if valor < 50 (pequeno), um pedido de valor 0 entra nos dois e e contado duas vezes; com if valor == 0 seguido de elif valor < 50, entra so no primeiro. Quando as condicoes se sobrepoem (todo valor 0 tambem e menor que 50), a mais especifica vem primeiro: com o teste de 'pequeno' antes, o brinde nunca seria contado. O operador or junta duas condicoes que levam a MESMA acao; nao serve para escolher entre acoes diferentes que se excluem.

## 5. Data Structures (The Python Tutorial)

- Source ID: `source_python-datastructures`
- URL: https://docs.python.org/3/tutorial/datastructures.html

Resumo pedagogico (parafraseado, verificado por execucao em Python 3.11): listas e dicionarios sao escritos de forma literal, [ ] e { }; uma lista de cards e uma lista de dicionarios, [{'card_id': 'a', 'due_at': '2026-10-05'}]. Passar um dicionario sozinho onde se espera uma lista faz o for percorrer as CHAVES (textos), e card['due_at'] sobre um texto levanta TypeError. Sequencias, inclusive textos, sao comparadas de forma lexicografica (secao 5.8): caractere a caractere, da esquerda para a direita. Por isso datas no formato 'AAAA-MM-DD' podem ser comparadas como texto, '2026-10-09' >= '2026-10-09' e verdadeiro e '2026-10-09' > '2026-10-09' e falso; o texto vazio '' vem antes de qualquer outro texto. Comparar texto com None com >= levanta TypeError.
