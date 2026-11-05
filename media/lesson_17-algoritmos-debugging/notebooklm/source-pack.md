# Verified Source Pack

## Python Documentation: Time complexity of operations on built-in types

- Source ID: `source_python-time-complexity`
- URL: https://docs.python.org/3/builtins/time-complexity.html

n is the number of elements in the container. For a list, getting an item by index (l[k]) is O(1) and checking membership (x in l) is O(n): Python compares item by item. For a dict, getting an item by key (d[key]) is O(1) on average, and for a set, membership (x in s) is O(1) on average. These are average-case times: they assume few hash collisions; in the worst case these O(1) operations can take O(n). In this study: O(1) is constant (the work does not change when the data grows), O(n) is linear (twice the data, twice the work).

## Python Documentation: bisect, array bisection algorithm

- Source ID: `source_python-bisect`
- URL: https://docs.python.org/3/library/bisect.html

The bisect module keeps a list in sorted order and uses binary search to find positions. It assumes the list is already sorted. The documentation calls the search step an O(log n) search, and notes that inserting into a list is O(n). In this study: binary search works only on a sorted list; on an unsorted list it fails silently, answering that an item does not exist even when it is in the list. The module is the ready-made tool; the lesson implements binary search by hand only to understand the mechanism.

## Python Documentation: Sorting Techniques

- Source ID: `source_python-sorting-howto`
- URL: https://docs.python.org/3/howto/sorting.html

sorted(iterable) builds and returns a new sorted list and leaves the original unchanged. list.sort() sorts the list in place and returns None. Both accept key, a function called once on each element whose result is used in the comparisons, and reverse=True for descending order. Sorts are guaranteed to be stable: records with equal keys keep their original order, also with reverse=True. Strings are compared character by character, so sorted(['10', '9', '100']) gives ['10', '100', '9']; key=int compares them as numbers.

## Estudo: teoria das partes 1 e 2 da lesson_17 e dificuldades observadas

- Source ID: `study_lesson17-teoria`
- URL: lessons/17-algoritmos-debugging.md

Parte 1, custo em passos. Medir em segundos muda com o computador; por isso se contam passos, como comparacoes. n e o tamanho da entrada. Constante O(1): lista[0] ou dicionario[chave], 1 passo com 1.000 ou 2.000 itens. Linear O(n): busca linear, olhar item por item; 1.000 itens dao 1.000 passos no pior caso, 2.000 dao 2.000. Logaritmico O(log n): cada passo corta pela metade o que sobrou; 1.000 itens dao 10 passos, 2.000 dao 11. Logaritmo aqui e quantas vezes da para dividir por 2 ate sobrar 1. Busca binaria numa lista ordenada: marcadores inicio e fim; meio = (inicio + fim) // 2, com divisao inteira; se o meio e menor que o alvo, inicio = meio + 1; se e maior, fim = meio - 1; quando inicio passa de fim, o alvo nao existe. Exemplo: precos = [3, 7, 12, 18, 25, 31, 40, 46, 58], buscando 31: meios 4 (25), 6 (40), 5 (31), achou em 3 passos; buscando 20: meios 4, 1, 2, 3 e para com inicio 4 e fim 3. fim e a ultima posicao, nao a quantidade de itens. Erros: lista fora de ordem (resposta errada sem aviso), x in lista e um laco escondido numa linha, / no lugar de // (TypeError ao usar float como indice). Parte 2, ordenacao. A busca binaria precisa de lista ordenada, e os dados quase nunca chegam assim. Ordenacao por selecao: a cada volta, achar o menor do trecho nao ordenado e troca-lo com o primeiro desse trecho; o trecho ordenado cresce um item por volta; com n itens bastam n - 1 voltas. Rastreio de [5, 2, 9, 1, 6]: [1, 2, 9, 5, 6], [1, 2, 9, 5, 6], [1, 2, 5, 9, 6], [1, 2, 5, 6, 9], com 4 + 3 + 2 + 1 = 10 comparacoes. Total n x (n - 1) / 2: 100 itens dao 4.950, 200 dao 19.900. Quadratico O(n2): um laco dentro de outro; dobrar os dados quadruplica o trabalho, porque dobram as voltas e o tamanho de cada volta. Trocar dois valores: a, b = b, a. sorted devolve lista nova; lista.sort() muda a propria lista e devolve None, entao lista = lista.sort() perde a lista. key recebe a funcao sem parenteses (key=pelo_preco); lambda p: p['preco'] e a mesma funcao numa linha. reverse=True inverte. Ordenacao estavel: empates mantem a ordem original. Datas AAAA-MM-DD ordenam certo como texto. Dificuldades observadas do aluno (checagens, nao avaliacao): chamou O(1) e O(n) de logaritmicos antes da aula; esqueceu o custo constante numa recuperacao e lembrou na seguinte; usou a quantidade de itens como fim; propos olhar a posicao vizinha numa lista fora de ordem; disse que dobrar os dados dobra o custo da selecao; trocou sort por sorted numa previsao; nao sabia por que '10' vem antes de '9'. Em todas, a explicacao foi dada e a pergunta seguinte saiu certa, menos a ordem de textos, que ainda nao foi retomada.
