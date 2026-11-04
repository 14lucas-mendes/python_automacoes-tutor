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
> A teoria tem partes. A **parte 1** (custo em passos e busca) foi dada em 02/11. As partes seguintes (ordenação, recursão e dividir para conquistar, debugging por hipótese) abrem as próximas sessões.

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
- **Próximas partes da teoria:** ordenação por seleção e `sorted`/`key`; recursão e dividir para conquistar; debugging por hipótese.
- **Critérios de entrega da lição:** busca binária e ordenação implementadas e testadas com valor esperado; dois defeitos diagnosticados com hipótese escrita antes da correção; comparação de passos explicada.
- **Saída de `weak_notacao-custo-big-o`:** explicar corretamente, com contagem de passos, a diferença entre custo constante, linear e logarítmico.

## Progresso

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
