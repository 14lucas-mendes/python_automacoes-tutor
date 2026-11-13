# Lição `lesson_17-algoritmos-debugging`

**Status:** em andamento, aberta em 2026-11-02 (`session_2026-11-02-lesson17-teoria-01`). Tópico: `topic_logica-algoritmos`. Ciclo 7 da formação fechada.

**Objetivo observável:** implementar e explicar busca linear × busca binária e uma ordenação simples, comparando passos; reconhecer recursão e dividir para conquistar num exemplo pequeno; diagnosticar defeitos com hipótese explícita (prever, rodar, comparar).

**Pré-requisito:** `lesson_16-estruturas-dados` (concluída em 31/10). Continua valendo o método do bloco: entrada, regra, saída, exemplos com o esperado a mão, plano em português, só depois o código.

**Âncora no projeto:** ordenar e buscar sessões e datas do estudo fictício no app `segundo-cerebro`; defeitos plantados nos índices da `lesson_16`.

**Fontes verificadas:**

- Python Documentation, [Time complexity of operations on built-in types](https://docs.python.org/3/builtins/time-complexity.html) (`source_python-time-complexity`): custo de `x in lista`, `lista[k]`, `dicionario[chave]` e `x in conjunto`.
- Python Documentation, [bisect](https://docs.python.org/3/library/bisect.html) (`source_python-bisect`): busca binária da biblioteca padrão, que exige lista ordenada.

Estrutura: **Teoria** (para reler), **Plano de prática** e **Progresso**.

## Teoria

> Escrita em 2026-11-02 para a abertura da lição (`theory_first`, tema novo). Material do tutor: **não é evidência** e não muda domínio. Os exemplos usam ônibus, um jogo de adivinhar e preços de propósito, para não entregar a tarefa do projeto.
>
> A teoria tem partes: **parte 1** (custo em passos e busca) em 02/11, **parte 2** (ordenação) em 05/11, **parte 3a** (recursão e dividir para conquistar) em 12/11 e **parte 3b** (debugging por hipótese) em 13/11.

### Parte 1: custo em passos e busca

### Problema e porquê

Até agora, a pergunta era "o código dá a resposta certa?". Agora entra outra: **"quanto trabalho ele faz quando os dados crescem?"**

Dois programas podem acertar a mesma resposta, e um deles ficar inutilizável. Com 10 sessões no estudo, qualquer código parece instantâneo. Com 1 milhão de registros, procurar item por item pode custar 1 milhão de comparações. Outro caminho resolve em 20.

Medir em segundos não serve para comparar: o tempo muda com o computador. Por isso contamos **passos**, as operações básicas que o programa faz, como comparar dois valores. O número de passos não depende da máquina.

Um **algoritmo** é a receita: a sequência de passos que resolve um problema. Vários algoritmos podem resolver o mesmo problema com custos muito diferentes.

### Como funciona: três formas de crescer

Pense em três jeitos de achar uma pessoa, com um grupo cada vez maior.

| Situação | O que você faz | Se o grupo dobrar | Nome |
|---|---|---|---|
| Você sabe a poltrona exata: fila 3, número 12 | Vai direto | O trabalho continua igual | **constante** |
| Ninguém tem lugar marcado | Olha um rosto de cada vez | O trabalho dobra | **linear** |
| A lista de nomes está em ordem alfabética | Abre no meio, descarta metade, repete | Só **um** passo a mais | **logarítmico** |

**Constante, O(1):** o número de passos não muda com o tamanho dos dados. `lista[0]` é assim: ter 10 ou 10 milhões de itens não faz diferença. `dicionario[chave]` e `x in conjunto` também são O(1), **em média**.

**Linear, O(n):** os passos crescem na mesma proporção dos dados. Dez vezes mais dados, dez vezes mais passos. `x in lista` é assim: o Python compara item por item até achar.

**Logarítmico, O(log n):** cada passo corta o problema pela metade, então dobrar os dados acrescenta só um passo.

"Logaritmo" aqui quer dizer só isto: **quantas vezes dá para dividir por 2 até sobrar 1**. Com 8 itens: 8 → 4 → 2 → 1, três divisões. Por isso log₂ 8 = 3. Com 1.024 itens, são 10 divisões.

### Vocabulário

- **Algoritmo:** sequência de passos que resolve um problema.
- **Passo:** uma operação básica contada, como uma comparação.
- **`n`:** o tamanho da entrada, por exemplo a quantidade de itens da lista.
- **Custo:** quanto trabalho o algoritmo faz em função de `n`.
- **Notação O grande, `O(...)`:** forma de escrever como o custo **cresce**. Ela ignora detalhes pequenos: `2n` passos ainda é `O(n)`, porque continua crescendo em linha reta.
- **Pior caso:** a entrada que dá mais trabalho. Procurar um item que não existe é o pior caso da busca linear.
- **Busca linear:** olhar um item de cada vez, do início ao fim.
- **Busca binária:** numa lista **ordenada**, olhar o meio e descartar a metade onde o alvo não pode estar, repetindo. "Binária" porque cada comparação escolhe entre dois lados.
- **Divisão inteira, `//`:** divide e joga fora a parte quebrada. `7 // 2` dá `3`, enquanto `7 / 2` dá `3.5`.

### Exemplo básico, linha a linha: busca linear com contador

```python
def busca_linear(lista, alvo):
    passos = 0
    for posicao, valor in enumerate(lista):
        passos += 1
        if valor == alvo:
            return posicao, passos
    return None, passos

paradas = ["Sé", "Paulista", "Pinheiros", "Butantã"]
print(busca_linear(paradas, "Sé"))       # (0, 1)
print(busca_linear(paradas, "Butantã"))  # (3, 4)
print(busca_linear(paradas, "Lapa"))     # (None, 4)
```

1. `def busca_linear(lista, alvo):` recebe onde procurar e o que procurar.
2. `passos = 0` é o contador. Ele não ajuda a achar nada: só mede o trabalho.
3. `enumerate(lista)` entrega posição e valor a cada volta do laço.
4. `passos += 1` conta uma comparação.
5. `if valor == alvo:` é a comparação em si.
6. `return posicao, passos` sai da função assim que acha, devolvendo uma tupla.
7. `return None, passos` só roda se o laço terminar sem achar.

As três chamadas mostram os casos: o melhor (1 passo, o primeiro item), o pior com o alvo presente (4, o último) e o pior com o alvo ausente (4, olhou tudo).

### Exemplo aprofundado: busca binária à mão

**Primeiro contexto: adivinhar um número de 1 a 100.** Alguém responde "maior" ou "menor". Chutar 1, 2, 3... pode levar 100 tentativas. Chutar o meio descarta metade a cada resposta:

```text
sobram 100 → chuta 50 → "maior" → sobram 50 (51 a 100)
sobram  50 → chuta 75 → "menor" → sobram 24 (51 a 74)
sobram  24 → chuta 62 → "maior" → sobram 12 (63 a 74)
...
```

Em no máximo 7 tentativas você acerta qualquer número de 1 a 100.

**Segundo contexto: preços em ordem crescente.** Dois marcadores delimitam o trecho que ainda pode conter o alvo: `inicio` e `fim`. O `meio` é `(inicio + fim) // 2`.

```python
precos = [3, 7, 12, 18, 25, 31, 40, 46, 58]
#         0  1   2   3   4   5   6   7   8     (posições)
```

Procurando **31** (existe):

| Passo | `inicio` | `fim` | `meio` | `precos[meio]` | Decisão |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 8 | 4 | 25 | 25 < 31: o alvo só pode estar depois da posição 4 |
| 2 | 5 | 8 | 6 | 40 | 40 > 31: o alvo só pode estar antes da posição 6 |
| 3 | 5 | 5 | 5 | 31 | achou, na posição 5 |

Procurando **20** (não existe):

| Passo | `inicio` | `fim` | `meio` | `precos[meio]` | Decisão |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 8 | 4 | 25 | 25 > 20: só antes da posição 4 |
| 2 | 0 | 3 | 1 | 7 | 7 < 20: só depois da posição 1 |
| 3 | 2 | 3 | 2 | 12 | 12 < 20: só depois da posição 2 |
| 4 | 3 | 3 | 3 | 18 | 18 < 20: só depois da posição 3 |
| fim | 4 | 3 | | | `inicio` passou de `fim`: o trecho acabou, 20 não existe |

**Comparando os custos no pior caso:**

| Itens (`n`) | Busca linear | Busca binária |
|---:|---:|---:|
| 10 | 10 | 4 |
| 100 | 100 | 7 |
| 1.000 | 1.000 | 10 |
| 1.000.000 | 1.000.000 | 20 |
| 1.000.000.000 | 1.000.000.000 | 30 |

A coluna da binária sobe devagar porque cada passo corta metade do que sobrou.

O código da busca binária **não** aparece aqui de propósito: transformar esse rastreio em função é a tarefa da prática.

### Erros comuns e limites

- **Lista fora de ordem:** a busca binária não avisa. Ela descarta a metade errada e pode dizer que o item não existe, mesmo com ele na lista.
- **Custo escondido em uma linha:** `alvo in lista` é uma linha só, mas é um laço por dentro. Uma linha de código não significa um passo.
- **Confundir os nomes:** O(1) é constante, O(n) é linear, O(log n) é logarítmico. Só o último divide o problema a cada passo.
- **`/` no lugar de `//`:** `/` dá um `float`, e `lista[3.5]` levanta `TypeError: list indices must be integers or slices, not float`.
- **Dicionário não substitui tudo:** ele acha a chave exata em O(1) em média, mas não responde "qual a primeira data depois de tal dia?". Numa lista ordenada, a busca binária responde.
- **O(1) em média não é garantia:** no pior caso, dicionário e conjunto caem para O(n). Na prática isso é raro.
- **Lista pequena:** com poucos itens, a busca linear basta. Ordenar só para buscar uma vez nem sempre compensa, porque ordenar também custa.
- **Na vida real:** o módulo `bisect` da biblioteca padrão já faz busca binária. Aqui você implementa à mão para entender o mecanismo.

### Checagens de entendimento

Não são evidência. Resposta errada pede mais explicação, não nota.

1. Uma lista cresceu de 1.000 para 2.000 itens. No pior caso, quantos passos a mais fazem a busca linear e a busca binária?
2. `"Lapa" in paradas` é uma linha só. Qual é o custo, e por quê?
3. Rastreie à mão a busca por **46** em `precos`, com as colunas `inicio`, `fim`, `meio` e `precos[meio]`.
4. Aplique a busca binária em `[25, 3, 40, 7, 12]`, procurando **7**. O que acontece, e por quê?

### Ponte para o projeto

As sessões do estudo fictício têm datas como `"2026-10-31"`. Nesse formato (ano, mês, dia), a ordem do texto é a ordem do tempo, então uma lista ordenada de datas aceita busca binária.

Na `lesson_16`, você escolheu dicionário e conjunto sem medir o custo. Agora dá para explicar a escolha em passos: chave exata pede dicionário; "a partir de tal data" pede lista ordenada.

### Parte 2: ordenação

> Escrita em 2026-11-05 (`session_2026-11-05-lesson17-ordenacao-teoria-01`). Material do tutor: não é evidência. Os exemplos usam cartas, números soltos e produtos de papelaria, para não entregar a tarefa do projeto.
>
> Fonte verificada: Python Documentation, [Sorting Techniques](https://docs.python.org/3/howto/sorting.html) (`source_python-sorting-howto`).

### Problema e porquê

A busca binária só funciona com a lista **ordenada**, mas os dados quase nunca chegam assim. No Índice 3, as revisões vinham fora de ordem. Muita pergunta do dia a dia também depende de ordem: "os 5 cards mais atrasados", "o produto mais barato", "o ranking do campeonato".

**Ordenar** é rearranjar os itens de uma lista segundo um critério: do menor para o maior (**ordem crescente**) ou do maior para o menor (**ordem decrescente**).

### Como funciona: ordenação por seleção

Pense em cartas viradas para cima na mesa. Você **seleciona** a menor, põe na ponta esquerda, e repete com as que sobraram. Daí o nome: **ordenação por seleção**.

A lista fica dividida em duas partes:

- o **trecho ordenado**, à esquerda, que cresce uma posição a cada rodada;
- o **trecho não ordenado**, à direita, onde se procura o menor.

Em cada rodada:

1. percorra o trecho não ordenado e ache a posição do menor;
2. **troque** esse menor com o primeiro item do trecho não ordenado;
3. agora o trecho ordenado tem um item a mais.

Rastreio de `[5, 2, 9, 1, 6]`:

| Rodada | Trecho não ordenado | Menor | Troca | Lista depois | Comparações |
|---|---|---|---|---|---:|
| 1 | posições 0–4: 5, 2, 9, 1, 6 | 1 (posição 3) | posições 0 e 3 | `[1, 2, 9, 5, 6]` | 4 |
| 2 | posições 1–4: 2, 9, 5, 6 | 2 (posição 1) | consigo mesmo | `[1, 2, 9, 5, 6]` | 3 |
| 3 | posições 2–4: 9, 5, 6 | 5 (posição 3) | posições 2 e 3 | `[1, 2, 5, 9, 6]` | 2 |
| 4 | posições 3–4: 9, 6 | 6 (posição 4) | posições 3 e 4 | `[1, 2, 5, 6, 9]` | 1 |

Com 5 itens bastam 4 rodadas: quando sobra um item só, ele já está no lugar.

**Trocar dois valores** em Python cabe numa linha: `a, b = b, a`. O lado direito monta a tupla `(b, a)` antes, e o lado esquerdo desempacota nela. Com `a = 1` e `b = 2`, depois da troca `a` vale 2 e `b` vale 1.

O código da ordenação por seleção **não** aparece aqui de propósito: transformar esse rastreio em função é tarefa da prática.

### Custo: quadrático

Conte as comparações do rastreio: 4 + 3 + 2 + 1 = 10. Com `n` itens, a soma é `(n - 1) + (n - 2) + ... + 1`, que dá `n × (n − 1) / 2`.

| Itens (`n`) | Comparações da seleção |
|---:|---:|
| 10 | 45 |
| 100 | 4.950 |
| 200 | 19.900 |
| 1.000 | 499.500 |
| 2.000 | 1.999.000 |

Dobrar os dados **quadruplica** o trabalho, mais ou menos. Esse crescimento se chama **quadrático**, `O(n²)`: um laço que percorre a lista dentro de outro laço que também percorre a lista.

| Custo | Notação | Dobrar os dados faz o trabalho... |
|---|---|---|
| constante | `O(1)` | ficar igual |
| logarítmico | `O(log n)` | ganhar 1 passo |
| linear | `O(n)` | dobrar |
| quadrático | `O(n²)` | quadruplicar |

### Vocabulário

- **Ordenar:** rearranjar segundo um critério.
- **Ordem crescente / decrescente:** do menor para o maior / do maior para o menor.
- **Ordenação por seleção:** a cada rodada, achar o menor do trecho não ordenado e trocá-lo com o primeiro desse trecho.
- **Trocar (`a, b = b, a`):** um valor vai para o lugar do outro.
- **Quadrático, `O(n²)`:** dobrar os dados quadruplica o trabalho.
- **`sorted(lista)`:** devolve uma lista **nova**, ordenada, e deixa a original intacta.
- **`lista.sort()`:** ordena a própria lista (mutação) e devolve `None`.
- **`key`:** função que recebe um item e devolve o valor usado na comparação.
- **`reverse=True`:** ordem decrescente.
- **`lambda`:** uma função curta, sem nome, escrita numa linha só. `lambda p: p["preco"]` faz o mesmo que um `def` que recebe `p` e devolve `p["preco"]`.
- **Ordenação estável:** itens com a mesma chave mantêm a ordem em que estavam. O `sorted` do Python é estável, inclusive com `reverse=True`.

### Exemplo básico: `sorted` e `.sort()`

```python
notas = [7, 3, 9]
print(sorted(notas))   # [3, 7, 9]   (lista nova)
print(notas)           # [7, 3, 9]   (original intacta)

resultado = notas.sort()
print(resultado)       # None        (sort não devolve a lista)
print(notas)           # [3, 7, 9]   (a própria lista mudou)
```

É a mesma diferença do card de fatiar × `pop`: `sorted` cria uma cópia; `.sort()` mexe na original.

### Exemplo aprofundado: `key`, `reverse` e empate

```python
produtos = [
    {"nome": "caderno", "preco": 12.5},
    {"nome": "caneta", "preco": 3.0},
    {"nome": "mochila", "preco": 89.9},
    {"nome": "lápis", "preco": 3.0},
    {"nome": "régua", "preco": 5.5},
]

def pelo_preco(produto):
    return produto["preco"]

baratos = sorted(produtos, key=pelo_preco)
# caneta, lápis, régua, caderno, mochila

caros = sorted(produtos, key=pelo_preco, reverse=True)
# mochila, caderno, régua, caneta, lápis

por_nome = sorted(produtos, key=lambda p: p["nome"])
# caderno, caneta, lápis, mochila, régua
```

1. Sem `key`, o Python não sabe comparar dois dicionários: `sorted(produtos)` levanta `TypeError: '<' not supported between instances of 'dict' and 'dict'`.
2. `key=pelo_preco` entrega a **função**, sem parênteses. O `sorted` a chama uma vez para cada produto e compara os preços.
3. Caneta e lápis custam 3.0. Como a ordenação é estável, a caneta, que vinha antes na lista original, continua antes, também com `reverse=True`.
4. `lambda p: p["nome"]` é a mesma ideia do `def`, em uma linha.

### Erros comuns e limites

- **`lista = lista.sort()`:** a lista vira `None`, porque `.sort()` não devolve nada. É o mesmo problema da função sem `return`.
- **Chamar a função na `key`:** `key=pelo_preco()` executa a função na hora, sem argumento, e dá `TypeError: pelo_preco() missing 1 required positional argument`. O certo é `key=pelo_preco`.
- **Número guardado como texto:** `sorted(["10", "9", "100"])` dá `['10', '100', '9']`. Texto é comparado caractere por caractere, e `"1"` vem antes de `"9"`. Converta com `int()` ou use `key=int`.
- **Datas:** no formato `"AAAA-MM-DD"`, a ordem do texto é a ordem do tempo. Em `"05/11/2026"`, não é.
- **A seleção é lenta para listas grandes:** `O(n²)`. Na vida real, use `sorted`, que usa um algoritmo bem mais rápido. Aqui você implementa a seleção para entender o mecanismo e contar passos.

### Checagens de entendimento

Não são evidência.

1. Rastreie a ordenação por seleção em `[4, 9, 2, 7]`: a lista depois de cada rodada e o total de comparações.
2. Com 100 itens, a seleção faz 4.950 comparações. Com 200, quantas, mais ou menos, e por quê?
3. Preveja a saída: `notas = [7, 3, 9]`, `resultado = notas.sort()`, `print(resultado, notas)`.
4. Por que `sorted(["10", "9", "100"])` não dá `['9', '10', '100']`?

### Ponte para o projeto

As sessões e revisões do estudo fictício nem sempre chegam em ordem. Para usar a busca binária da Tarefa 1, primeiro se ordena a lista por data, com `key`. Ordena-se **uma vez**, e depois se fazem muitas buscas baratas.

A revisão de cards de cada sessão faz exatamente isso: ordena os cards vencidos pela data (`due_at`) e pega os 5 mais atrasados.

### Parte 3a: recursão e dividir para conquistar

> Escrita em 2026-11-12 (`session_2026-11-12-lesson17-recursao-teoria-01`). Material do tutor: não é evidência. Os exemplos usam contagem regressiva, fatorial e números soltos, para não entregar a tarefa do projeto.
>
> Fonte verificada: Python Documentation, [Built-in Exceptions: RecursionError](https://docs.python.org/3/library/exceptions.html#RecursionError) (`source_python-recursionerror`).

### Problema e porquê

Alguns problemas são feitos de **versões menores de si mesmos**:

- uma pasta pode ter pastas dentro, que têm pastas dentro, como o cofre: `20 - Áreas` → `Pessoal` → `Estudos`;
- uma boneca russa (matrioska) tem outra boneca menor dentro, até a menor de todas, que não abre;
- na busca binária, depois de olhar o meio, sobra **o mesmo problema** numa lista com metade do tamanho.

Para esse tipo de problema existe a **recursão**: uma função que, para resolver o problema, **chama a si mesma** com um pedaço menor dele.

### Como funciona: caso-base e caso recursivo

Toda função recursiva tem duas partes:

1. **Caso-base:** o pedaço tão pequeno que a resposta é direta, sem chamar ninguém. É a boneca que não abre. É ele que **faz a recursão parar**.
2. **Caso recursivo:** a função faz um pouco do trabalho e chama a si mesma com um problema **menor**, que anda em direção ao caso-base.

Quando uma função chama outra (ou a si mesma), a chamada de cima **fica esperando** a de baixo terminar. O Python guarda essas chamadas que esperam numa **pilha de chamadas**, como pratos empilhados: a última que entrou é a primeira que termina. É essa mesma pilha que o traceback mostra quando dá erro.

### Vocabulário

- **Recursão:** uma função que chama a si mesma.
- **Caso-base:** a situação em que a função responde direto, sem se chamar de novo. Sem ele, a recursão não para.
- **Caso recursivo:** a parte que chama a função de novo com um problema menor.
- **Pilha de chamadas:** a lista das chamadas que estão esperando uma resposta. A mais recente fica em cima.
- **`RecursionError`:** a exceção que o Python levanta quando a pilha passa do limite, que é 1000 chamadas por padrão (`sys.getrecursionlimit()`).
- **Dividir para conquistar:** quebrar o problema em pedaços menores do mesmo tipo, resolver cada pedaço e juntar as respostas.

### Exemplo básico, linha a linha: contagem regressiva

```python
def regressiva(n):
    if n == 0:            # caso-base
        print("Fogo!")
        return
    print(n)
    regressiva(n - 1)     # caso recursivo: problema menor

regressiva(3)
# 3
# 2
# 1
# Fogo!
```

1. `regressiva(3)`: 3 não é 0, então imprime `3` e chama `regressiva(2)`.
2. `regressiva(2)`: imprime `2` e chama `regressiva(1)`.
3. `regressiva(1)`: imprime `1` e chama `regressiva(0)`.
4. `regressiva(0)`: caso-base. Imprime `Fogo!` e para.

O `n - 1` é o que faz o problema **diminuir** até chegar no caso-base.

### Exemplo aprofundado: fatorial e a pilha que volta

O fatorial de 4 é `4 × 3 × 2 × 1 = 24`. Repare que `4! = 4 × 3!`: o problema contém uma versão menor dele.

```python
def fatorial(n):
    if n == 1:                    # caso-base
        return 1
    return n * fatorial(n - 1)    # caso recursivo

print(fatorial(4))   # 24
```

A pilha cresce na ida e se desfaz na volta:

```text
fatorial(4) espera 4 * fatorial(3)
  fatorial(3) espera 3 * fatorial(2)
    fatorial(2) espera 2 * fatorial(1)
      fatorial(1) devolve 1            ← caso-base
    fatorial(2) devolve 2 * 1 = 2
  fatorial(3) devolve 3 * 2 = 6
fatorial(4) devolve 4 * 6 = 24
```

Na ida ninguém termina: cada chamada fica esperando. Só quando o caso-base responde é que as contas acontecem, de baixo para cima.

### Dividir para conquistar

A **busca binária** que você implementou já é dividir para conquistar: olha o meio e resolve o mesmo problema numa metade. Você escreveu com `while`, mas ela também pode ser escrita com recursão, em que cada chamada recebe a metade que sobrou.

Outro exemplo é o **quicksort**, uma ordenação bem mais rápida que a seleção. A ideia, rastreada à mão em `[5, 2, 9, 1, 6]`:

1. Escolha um **pivô**, por exemplo o primeiro: `5`.
2. Divida o resto em **menores** que o pivô, `[2, 1]`, e **maiores**, `[9, 6]`.
3. Ordene cada parte **do mesmo jeito**, que é a recursão: `[2, 1]` vira `[1, 2]`, e `[9, 6]` vira `[6, 9]`.
4. Junte: `[1, 2] + [5] + [6, 9] = [1, 2, 5, 6, 9]`.

Caso-base: uma lista com 0 ou 1 item já está ordenada.

### Erros comuns e limites

- **Esquecer o caso-base** (ou nunca chegar nele): a função se chama para sempre, até `RecursionError: maximum recursion depth exceeded`.
- **O problema não diminui:** chamar `regressiva(n)` em vez de `regressiva(n - 1)` dá o mesmo `RecursionError`.
- **Esquecer o `return` no caso recursivo:** escrever `n * fatorial(n - 1)` sem `return` faz a chamada de baixo devolver `None`, e a de cima tenta `3 * None`: `TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'`. É o card da função sem `return`, agora dentro da recursão.
- **Limite de profundidade:** o Python aceita cerca de 1000 chamadas empilhadas. Para percorrer uma lista grande item por item, um laço é melhor. A recursão brilha quando o problema se divide (metades, pastas dentro de pastas).

### Checagens de entendimento

Não são evidência.

1. Preveja a saída de `regressiva(2)`.
2. Na `fatorial`, qual é o caso-base? E o que acontece se ele for apagado?
3. Desenhe a pilha de `fatorial(3)`: o que cada chamada espera e o que devolve.
4. Por que esquecer o `return` no caso recursivo dá `TypeError`, e não um resultado errado?

### Ponte para o projeto

O cofre e o estudo têm estruturas aninhadas: pastas dentro de pastas, lições com sessões, cards com histórico de revisões. Percorrer uma estrutura de profundidade desconhecida é o caso típico da recursão. E a busca binária da Tarefa 1 pode ser reescrita com recursão, dividindo a lista de sessões a cada chamada.

### Parte 3b: debugging por hipótese

> Escrita em 2026-11-13 (`theory_first`, tema novo). Exemplos com chuva e carrinho de compras, diferentes dos defeitos que serão plantados nos índices da `lesson_16`. Saídas conferidas por execução. Fonte: Python Documentation, [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) (`source_python-errors-exceptions`).

### Problema e porquê

Um **defeito** (em inglês, *bug*) é um trecho de código que faz o programa se comportar diferente do esperado. O que você vê é o **sintoma** (um número errado, uma mensagem de erro); o que precisa achar é a **causa** (a linha e o motivo).

O jeito mais comum de procurar a causa é a tentativa e erro: mudar uma coisa, rodar, mudar outra, rodar de novo. Funciona às vezes, mas tem três problemas:

1. gasta tempo, porque cada mudança é um chute;
2. quando "funciona", você não sabe **por quê**, e o defeito pode voltar;
3. você pode mudar três coisas de uma vez, consertar uma e estragar outra.

**Debugging por hipótese** é procurar a causa como um médico: ele não receita cinco remédios para ver qual funciona. Ele olha o sintoma, diz o que acha que é ("é infecção, porque tem febre e a garganta está vermelha"), pede o exame que confirma ou descarta, e só então trata.

### Como funciona: o ciclo em quatro passos

1. **Reproduzir.** Ache o menor exemplo que mostra o defeito e escreva três coisas: a entrada, o **esperado** (calculado à mão) e o **obtido** (o que o programa deu). Sem isso, você nem sabe se consertou.
2. **Escrever a hipótese, com uma previsão.** Uma frase no formato: *"Acho que a causa é X, porque Y. Se eu estiver certo, quando eu fizer Z vou ver W."* A previsão é o que torna a hipótese testável.
3. **Testar sem consertar ainda.** Rode o exame que a hipótese pediu (um `print` dirigido, um rastreio à mão, uma chamada isolada) e **compare** o previsto com o visto.
   - Bateu: a hipótese está confirmada. Vá para o passo 4.
   - Não bateu: a hipótese foi descartada. Isso **não é fracasso**: você eliminou um suspeito. Escreva a próxima hipótese.
4. **Consertar com um teste que falha antes.** Escreva o `assert` do exemplo do passo 1 e rode: ele **tem que falhar** (prova que o teste enxerga o defeito). Conserte só a causa. Rode de novo: agora ele passa. Rode também os outros testes, para ver se nada quebrou.

### Os três tempos do erro

Antes de procurar, vale saber **quem avisa** e **quando**. O Python separa os erros em dois tempos, e existe um terceiro caso que ninguém avisa:

| Tipo | Quando aparece | Quem avisa | Sinal |
|---|---|---|---|
| **Erro de sintaxe** (`SyntaxError`) | Antes de rodar: o Python lê o arquivo inteiro e reprova | O Python, sem executar nenhuma linha | Mensagem **sem** `Traceback (most recent call last)` |
| **Exceção** (`TypeError`, `NameError`, `KeyError`...) | Durante a execução, na linha que falhou | O Python, com o rastro das chamadas | Mensagem **com** traceback |
| **Erro de lógica** | Nunca: o programa termina normalmente | **Ninguém.** Só um teste com o esperado à mão pega | Resultado errado, sem mensagem |

Exemplo de erro de sintaxe, conferido por execução. A terceira linha (`print("oi")`) **não** roda, porque nada roda:

```python
def f(:
    return 1
print("oi")
```

```
  File "sint.py", line 1
    def f(:
          ^
SyntaxError: invalid syntax
```

O erro de lógica é o mais perigoso, porque parece sucesso. É por isso que o método do bloco exige o esperado calculado à mão **antes** do código.

### Vocabulário

- **Defeito (*bug*):** o trecho de código errado.
- **Sintoma:** o que se observa por fora (resultado errado, exceção).
- **Causa:** a linha e o motivo que produzem o sintoma.
- **Reproduzir:** fazer o defeito aparecer de propósito, com uma entrada conhecida.
- **Hipótese:** um palpite sobre a causa, com uma previsão que pode dar errado.
- **`print` dirigido:** um `print` colocado num ponto escolhido pela hipótese, mostrando só as variáveis de que ela fala. O contrário é espalhar `print` por todo lado.
- **Teste de regressão:** o `assert` que falhava antes da correção e passa depois. Ele fica no código para avisar se o defeito voltar.

### Exemplo básico, linha a linha: dias de chuva forte

A função deveria contar quantos dias tiveram chuva **igual ou acima** do limite:

```python
def dias_com_chuva_forte(chuvas_mm, limite):
    """Conta quantos dias tiveram chuva igual ou acima do limite."""
    contagem = 0
    for i in range(1, len(chuvas_mm)):
        if chuvas_mm[i] >= limite:
            contagem += 1
    return contagem
```

**Passo 1, reproduzir.** Entrada `[12, 3, 15]` com limite `10`. Esperado à mão: o 12 e o 15 passam do limite, então **2**. Obtido: **1**. Nenhuma mensagem de erro: é erro de lógica.

**Passo 2, primeira hipótese.** "Acho que a causa é o `>=`, que deveria ser `>`." Previsão: se fosse isso, só um dia com **exatamente** 10 mm seria contado errado. Mas na entrada não existe dia com 10 mm, e mesmo assim faltou um. A hipótese **não explica o sintoma**: descartada sem mexer no código.

**Passo 2 de novo, segunda hipótese.** "Acho que o laço não olha todos os dias. Se for isso, um `print` dentro do laço vai mostrar menos de 3 dias."

**Passo 3, testar.** `print` dirigido, só com o que a hipótese pede:

```python
    for i in range(1, len(chuvas_mm)):
        print("olhando dia", i, "->", chuvas_mm[i], "mm")
```

Saída real:

```
olhando dia 1 -> 3 mm
olhando dia 2 -> 15 mm
1
```

Previsto: menos de 3 dias. Visto: 2 dias, e falta o dia 0 (os 12 mm). **Confirmada.** A causa é o `range(1, ...)`, que começa no índice 1.

**Passo 4, consertar com teste que falha antes.**

```python
assert dias_com_chuva_forte([12, 3, 15], 10) == 2   # falha com o código antigo
```

Conserta só a causa, `range(len(chuvas_mm))`, apaga o `print` e roda: o `assert` passa. Um segundo teste protege o caso que escondia o defeito: chuva forte **só no primeiro dia**, `dias_com_chuva_forte([20, 1, 1], 10) == 1`.

### Exemplo aprofundado: o erro explode longe da causa

```python
def preco_com_desconto(preco, cupom):
    if cupom == "DEZ":
        return preco * 0.9
    elif cupom == "VINTE":
        return preco * 0.8


def total_carrinho(itens, cupom):
    total = 0
    for preco in itens:
        total += preco_com_desconto(preco, cupom)
    return total


print(total_carrinho([100, 50], "DEZ"))
print(total_carrinho([100, 50], ""))
```

Saída real (caminho do arquivo encurtado):

```
135.0
Traceback (most recent call last):
  File "carrinho.py", line 16, in <module>
    print(total_carrinho([100, 50], ""))
  File "carrinho.py", line 11, in total_carrinho
    total += preco_com_desconto(preco, cupom)
TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'
```

**Como ler.** A última linha diz o quê: somar um `int` com `None`. O bloco acima diz onde: na linha 11, dentro de `total_carrinho`. Mas a linha 11 é onde a conta **falhou**, não onde o `None` **nasceu**.

**Hipótese.** "O `None` vem de `preco_com_desconto`: com cupom vazio, nenhum `if` é verdadeiro, a função chega ao fim sem `return` e devolve `None` sozinha. Se eu estiver certo, `print(preco_com_desconto(100, ""))` vai mostrar `None`."

**Teste.** Saída real: `None`. **Confirmada.** O traceback apontou a vítima (`total_carrinho`); o culpado estava em outra função.

**Conserto.** O teste que falha antes: `assert total_carrinho([100, 50], "") == 150`. A correção é um `return preco` no fim de `preco_com_desconto` (sem cupom válido, sem desconto). Repare no que **não** fazer: trocar a linha 11 por um `if valor is not None` esconderia o sintoma, e o carrinho sem cupom passaria a custar 0.

### Erros comuns e limites

- **Mudar várias coisas de uma vez.** Se funcionar, você não sabe qual mudança consertou. Uma hipótese, uma mudança.
- **Consertar o sintoma, não a causa.** Um `try`/`except` ou um `if` que engole o erro deixa o programa quieto e errado.
- **`print` em todo lugar.** Vira ruído. O `print` dirigido responde a uma pergunta da hipótese.
- **Esquecer os `print` no código** depois de consertar.
- **Consertar sem o teste que falha antes.** Se o `assert` já passava com o código errado, ele não testa o defeito.
- **Acreditar na hipótese sem testar.** Ela é um palpite até a previsão bater.
- **"Rodou sem erro, então está certo."** Erro de lógica roda sem erro. Quem pega é o esperado à mão.

### Checagens de entendimento

Não são evidência.

1. No exemplo da chuva, a primeira hipótese foi descartada **sem mexer no código**. Como?
2. Um arquivo dá `SyntaxError` e o `print` da primeira linha não aparece. Por quê?
3. Por que o `assert` tem que **falhar** antes da correção?
4. No carrinho, o traceback aponta a linha 11. Onde estava a causa, e por que a linha apontada é outra?

### Ponte para o projeto

Os índices que você escreveu na `lesson_16` (tópico → evidências e o resumo do histórico de cards) vão voltar com **defeitos plantados** pelo tutor. Para cada um: reproduzir com esperado e obtido, escrever a hipótese com previsão **antes** de rodar qualquer `print`, testar, e só então consertar com o teste que falha antes.

## Plano de prática

Comece a sessão seguinte com uma recuperação curta da teoria da parte 1, antes de qualquer código.

- **Núcleo cognitivo:** decompor e implementar sozinho a busca binária, contar os passos e comparar com a busca linear.

### Tarefa 1: sessão por data (enunciado entregue em 2026-11-04)

O app precisa achar a sessão de um dia. As sessões do estudo fictício já vêm **ordenadas por data**, sem datas repetidas:

```python
sessoes = [
    {"session_id": "s01", "data": "2026-10-01"},
    {"session_id": "s02", "data": "2026-10-04"},
    {"session_id": "s03", "data": "2026-10-09"},
    {"session_id": "s04", "data": "2026-10-12"},
    {"session_id": "s05", "data": "2026-10-18"},
    {"session_id": "s06", "data": "2026-10-23"},
    {"session_id": "s07", "data": "2026-10-30"},
    {"session_id": "s08", "data": "2026-11-02"},
]
```

Regras:

1. Uma função recebe a lista e uma data e faz **busca binária** pelo campo `"data"`.
2. Ela devolve uma tupla `(session_id, passos)`. Sem sessão naquela data: `(None, passos)`.
3. `passos` é quantas sessões a busca **olhou**. O meio é sempre `(inicio + fim) // 2`, como na teoria.
4. Lista vazia: `(None, 0)`.
5. Para as **mesmas** datas buscadas, conte também os passos de uma busca linear e mostre os dois lado a lado.
6. Um comentário curto no código diz por que essa função só funciona com a lista ordenada.
7. `assert` com os esperados calculados **à mão**: uma data que existe e casos-limite (primeira, última, antes de todas, entre duas, depois de todas, lista vazia).

Antes do código: entrada, regra, saída, exemplos com o esperado à mão (casos-limite incluídos) e plano em português, num `.md` em `segundo-cerebro/exercicios/`.

### Tarefa 3: busca binária recursiva (enunciado entregue em 2026-11-12)

O app guarda as lições concluídas do estudo fictício, **ordenadas pela data de conclusão**, sem datas repetidas:

```python
licoes = [
    {"lesson_id": "l01", "concluida_em": "2026-09-07"},
    {"lesson_id": "l03", "concluida_em": "2026-09-12"},
    {"lesson_id": "l04", "concluida_em": "2026-09-17"},
    {"lesson_id": "l02", "concluida_em": "2026-10-06"},
    {"lesson_id": "l15", "concluida_em": "2026-10-23"},
    {"lesson_id": "l16", "concluida_em": "2026-10-31"},
    {"lesson_id": "l17", "concluida_em": "2026-11-20"},
]
```

Regras:

1. Uma função acha a lição concluída numa data com **busca binária recursiva**: ela olha o meio do trecho e **chama a si mesma** com a metade que pode ter a data. Nada de `while` nem `for` dentro dela.
2. Ela devolve o `lesson_id`, ou `None` se nenhuma lição foi concluída naquela data.
3. A lista recebida não muda.
4. Lista vazia: `None`.
5. Um comentário no código diz qual é o caso-base (ou os casos-base) e por que o problema diminui a cada chamada.
6. `assert` com os esperados calculados **à mão**: primeira, última, uma do meio, data antes de todas, data entre duas, data depois de todas, lista vazia e lista com uma lição só.

Antes do código: entrada, regra, saída, exemplos com o esperado à mão (casos-limite incluídos) e plano em português, num `.md` em `segundo-cerebro/exercicios/`.

### Defeito 1: índice de evidências que perde itens (enunciado entregue em 2026-11-13)

O tutor reescreveu o Índice 1 da `lesson_16` (tópico → evidências) e **plantou um defeito**. Os `assert` antigos foram tirados.

```python
topicos = ["topic_python", "topic_sql", "topic_git"]

evidencias = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
    {"evidence_id": "ev_02", "topic_id": "topic_git"},
    {"evidence_id": "ev_03", "topic_id": "topic_python"},
    {"evidence_id": "ev_04", "topic_id": "topic_react"},
]


def classificar_indice(evidencias, topicos):
    """Para cada topico, os IDs das evidencias dele, na ordem de evidencias."""
    result = {}
    for topico in topicos:
        result[topico] = []
    for evidencia in evidencias:
        topico = evidencia["topic_id"]
        if topico in result:
            result[topico] = [evidencia["evidence_id"]]
    return result


print(classificar_indice(evidencias, topicos))
```

**Sintoma relatado:** "Na tela do tópico Python aparece só uma evidência, mas eu sei que registrei mais de uma."

Siga o ciclo, **na ordem**, num `.md` em `segundo-cerebro/exercicios/modulo 05/`:

1. **Reproduzir:** a entrada, o esperado calculado à mão e o obtido.
2. **Hipótese com previsão**, escrita **antes** de rodar qualquer `print`: "acho que a causa é X, porque Y; se eu estiver certo, quando eu fizer Z vou ver W".
3. **Testar sem consertar:** o `print` dirigido (ou rastreio) e o que apareceu. Se a previsão não bater, escreva a próxima hipótese.
4. **Consertar com teste que falha antes:** o `assert` do passo 1 rodado **antes** da correção (copie a saída da falha), a correção só da causa e o `assert` passando depois.

O código corrigido, com o teste de regressão, vai num `.py` na mesma pasta.

### Tarefa 2: cards mais atrasados (enunciado entregue em 2026-11-09)

Na revisão, o app mostra primeiro os cards com a data mais antiga. Os cards do estudo fictício chegam **fora de ordem**, sem datas repetidas:

```python
cards = [
    {"card_id": "c1", "due_at": "2026-11-12"},
    {"card_id": "c2", "due_at": "2026-11-03"},
    {"card_id": "c3", "due_at": "2026-11-20"},
    {"card_id": "c4", "due_at": "2026-11-01"},
    {"card_id": "c5", "due_at": "2026-11-15"},
    {"card_id": "c6", "due_at": "2026-11-07"},
]
```

Regras:

1. Uma função ordena os cards por `"due_at"`, da data mais antiga para a mais nova, com **ordenação por seleção** escrita por você. Dentro dela, nada de `sorted`, `.sort()` ou `min`.
2. Ela devolve uma tupla `(lista_ordenada, comparacoes)`. `comparacoes` é quantas vezes duas datas foram comparadas.
3. A lista recebida **não pode mudar**, como acontece com `sorted`.
4. Lista vazia: `([], 0)`. Um card só: a lista com ele e `0` comparações.
5. Um `assert` confere o resultado da sua função com `sorted(cards, key=...)`.
6. Mostre os `card_id` dos 3 cards mais atrasados.
7. `assert` com os esperados calculados **à mão**, incluindo os casos-limite: vazia, um card, lista já ordenada e lista em ordem inversa.

Antes do código: entrada, regra, saída, exemplos com o esperado à mão (casos-limite incluídos) e plano em português, num `.md` em `segundo-cerebro/exercicios/`.
- **Próximas partes da teoria:** ordenação por seleção e `sorted`/`key`; recursão e dividir para conquistar; debugging por hipótese.
- **Critérios de entrega da lição:** busca binária e ordenação implementadas e testadas com valor esperado; dois defeitos diagnosticados com hipótese escrita antes da correção; comparação de passos explicada.
- **Saída de `weak_notacao-custo-big-o`:** explicar corretamente, com contagem de passos, a diferença entre custo constante, linear e logarítmico.

## Progresso

### Onde paramos (2026-11-13): debugging por hipótese e Defeito 1, faltam Defeito 2 e transferência

- **Sessão:** `session_2026-11-13-lesson17-debugging-teoria-01`, 11:47–13:01 (cerca de 74 min de 60).
- **Card:** `git-diff-staged-01` parcial. O `--staged` saiu certo; o `git diff` puro foi descrito como "tudo o que não foi commitado", sem separar o que já passou pelo `git add`.
- **Recuperação da parte 3a:** sem pista, não lembrou as duas partes. Com o código de `regressiva`, explicou o caso-base e o problema que diminui; os nomes foram retomados.
- **Teoria da parte 3b (debugging por hipótese):** dada em três blocos. Checagens (não são evidência):
  - médico: sintoma, hipótese e previsão certos (a previsão é o exame, não o tratamento);
  - chuva: causa certa, mas a previsão era "consertar e ver 2"; ensinado que o passo 3 observa sem mexer;
  - carrinho: lugar do `None` certo, sem o porquê e sem previsão;
  - `SyntaxError` e o `print` que não aparece: certo;
  - `assert` que falha antes: ideia parcial, ensinada com o alarme de fumaça.
- **Defeito 1 (índice de evidências com sobrescrita):** `segundo-cerebro/exercicios/modulo 05/defeito_01.md` e `.py`.
  - v1: ciclo completo no `.md`, com previsão exata, mas o `.py` ainda tinha o defeito (`evidence_logica-debugging-defeito1-01`, parcial);
  - v2, só com a conferência: correção aplicada e `assert` passando (`evidence_logica-debugging-defeito1-02`, correta).
- **Regra 9:** busca binária, ordenação, recursão, Feynman e Defeito 1 ✅. Faltam o Defeito 2 e a transferência.
- **Próximo:** recuperação curta do ciclo de quatro passos e Defeito 2, plantado no Índice 3 da `lesson_16`.

### Onde paramos (2026-11-12): recursão feita, faltam debugging e transferência

- **Sessão:** `session_2026-11-12-lesson17-recursao-teoria-01`, 18:39–19:47 (cerca de 70 min de 60).
- **Cards:** 5 de 5 certos. O `tempos-03` saiu certo pela primeira vez.
- **Teoria da parte 3a (recursão):** dada em três blocos. Checagens (não são evidência):
  - a volta da pilha de `fatorial(3)` saiu embaralhada; ensinada com a fila de recados, e a de `soma_ate(3)` saiu certa;
  - no caso sem `return`, achou que a recursão ficava infinita; ensinado que o caso-base é alcançado e que o `None` vem da chamada do meio;
  - `regressiva(2)`, o caso-base e o `RecursionError` sem caso-base saíram certos.
- **Tarefa 3 (busca binária recursiva):**
  - decomposição correta de primeira (`evidence_logica-recursao-decomposicao-01`, apoio);
  - código v1: função certa, mas sem `assert` nem comentário (`evidence_logica-recursao-codigo-01`, parcial);
  - código v2, só com a conferência: completo e correto (`evidence_logica-recursao-codigo-02`). Usa compreensão de lista, que ainda não foi ensinada e vai para a `lesson_19`.
- **Regra 9:** busca binária, ordenação, recursão e Feynman ✅. Faltam dois defeitos com hipótese e a transferência.
- **Próximo:** teoria da parte 3b (debugging por hipótese).

### Onde paramos (2026-11-10): ordenação no código e Feynman, faltam debugging e transferência

- **Sessão:** `session_2026-11-10-lesson17-ordenacao-codigo-01`, 16:46–17:31.
- **Cards:** 3 de 3 certos.
- **Tarefa 2, código:** `segundo-cerebro/exercicios/modulo 05/busca_ordenacao.py`. Todos os `assert` passam, e os 3 mais atrasados são c4, c2 e c6. Os casos extras do tutor também saíram certos: lista original intacta, 2 itens e 12 listas aleatórias. A IA só formatou o texto (declarado).
  - `evidence_logica-ordenacao-codigo-01`: aplicação autônoma e correta.
- **Feynman (comparação de passos):**
  - v1 parcial: constante explicado como "o valor não muda", seleção descrita como comparação de vizinhos.
  - v2, só com a conferência: corrigiu os dois pontos. O tutor a classificou como parcial por causa do 1.000.000 no quadrático; **o aluno contestou, e a objeção foi aceita**. Para um custo quadrático genérico, `n × n` vale, e a teoria ignora fatores constantes. `evidence_logica-feynman-custos-02` ficou correta, com notas de precisão.
- **Regra 9:** busca binária e ordenação ✅, Feynman ✅. Faltam dois defeitos com hipótese e a transferência.
- **Próximo:** teoria da parte 3 (recursão, dividir para conquistar e debugging por hipótese).

### Onde paramos (2026-11-09): decomposição da Tarefa 2 correta, código pendente

- **Sessão:** `session_2026-11-09-lesson17-ordenacao-pratica-01`, 17:57–18:39, dentro dos 45 min.
- **Cards:** 5 de 5 certos.
- **Recuperação da parte 2:** correta. 200 itens dão 19.900 comparações, porque dobram as voltas e o tamanho de cada uma (2 × 2 = 4); o porquê foi pedido de novo.
- **Tarefa 2 (cards mais atrasados):** `segundo-cerebro/exercicios/modulo 05/busca_ordenacao.md`.
  - v1 parcial: faltavam as comparações calculadas à mão e os casos já ordenada e inversa (`evidence_logica-ordenacao-decomposicao-01`, apoio).
  - v2, só com a conferência genérica: correta e autônoma. 15 comparações em qualquer ordem inicial (`evidence_logica-ordenacao-decomposicao-02`, apoio).
- **Regra 9:** só a busca binária cumprida. A ordenação conta quando o código estiver pronto e verificado.
- **Próximo:** o código, `busca_ordenacao.py`, a partir da decomposição v2.

### Onde paramos (2026-11-05): teoria da parte 2 dada, prática de ordenação pendente

- **Sessão:** `session_2026-11-05-lesson17-ordenacao-teoria-01`, 19:25–20:05, dentro dos 45 min.
- **Cards:** 4 certos; `tempos-03` parcial de novo, porque faltou o detalhe da última linha.
- **Recuperação:** custo constante correto (`weak_notacao-custo-big-o` continua ativo até uma evidência).
- **Teoria da parte 2:** dada em quatro blocos. Checagens (não são evidência):
  - rastreio de `[4, 9, 2, 7]`: pediu uma explicação mais simples; com a primeira volta feita junto, fez as outras sozinho e certo;
  - 200 itens: disse que dobrava (9.900). Ensinado que quadruplica (19.900), e depois completou a tabela certo;
  - `notas.sort()`: previu a saída de `sorted`. Ensinado; a nova previsão, com `cidades`, saiu certa;
  - `"10"` × `"9"`: não soube; ensinada a comparação caractere a caractere e o `key=int`.
- **Falta:** recuperação curta da parte 2 e a Tarefa 2 (ordenação), depois recursão e debugging por hipótese.

### Onde paramos (2026-11-04): busca binária autônoma e correta

- **Sessão:** `session_2026-11-04-lesson17-busca-binaria-01`, 18:22–19:37 (cerca de 75 min de 60).
- **Cards:** 5 de 5 certos.
- **Recuperação da parte 1:** parcial. Lembrou o custo linear com a contagem e a ideia do logarítmico, sem a conta. Não lembrou o constante. Os dois foram reexplicados.
- **Tarefa 1 (sessão por data):** `segundo-cerebro/exercicios/exe_04.md` e `exe_04.py`. Decomposição com o rastreio à mão dos casos-limite, busca binária e linear, `assert` e comparação lado a lado. Todos passam e conferem com o gabarito do tutor. A IA só formatou o texto (declarado).
  - `evidence_logica-busca-binaria-01`: aplicação autônoma e correta da parte de busca.
  - Melhorias opcionais: `elif` nos dois ramos exclusivos, um só `passos += 1` e o `if` redundante da linear.
- **Regra 9:** busca binária implementada e testada, com a comparação de passos ✅. Faltam: ordenação, dois defeitos com hipótese, Feynman e transferência.
- **`weak_notacao-custo-big-o`:** continua ativo.
- **Próximo:** teoria da parte 2 (ordenação por seleção, `sorted` e `key`).

### Onde paramos (2026-11-02): teoria da parte 1 aberta, prática pendente

- **Sessão:** `session_2026-11-02-lesson17-teoria-01`, 18:22–18:58, dentro dos 45 min informados.
- **Cards (retrieval_first):** 5 de 5 certos.
- **Teoria da parte 1:** dada em dois blocos, com as checagens 1, 3 e 4 e o caso binário da checagem 1 feitos no chat. Checagens não são evidência.
  - rastreio do 46 certo, em 3 passos;
  - 1.000 → 2.000: linear com 1.000 passos a mais, binária com 1 a mais, justificado por "mais uma divisão";
  - lista fora de ordem: viu que a busca vai para o lado errado. Dois pontos ensinados: `fim` é a última posição, não a quantidade de itens, e olhar o vizinho não resolve (o caminho é ordenar antes ou usar busca linear).
- **Evidência:** nenhuma. Regra 9: Feynman, aplicação padrão e transferência da lição continuam pendentes.
- **`weak_notacao-custo-big-o`:** continua ativo. A explicação correta nas checagens não é evidência; a saída vem na prática.
- **Falta:** recuperação curta da parte 1, enunciado da busca binária com dados do estudo fictício, decomposição, código e comparação de passos. Depois, as partes de ordenação, recursão e debugging por hipótese.
