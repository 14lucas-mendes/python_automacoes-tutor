# Lição `lesson_16-estruturas-dados`

**Status:** em andamento desde 2026-10-24 (`session_2026-10-24-lesson16-teoria-01`). Tópico: `topic_logica-algoritmos`. Ciclo 6 da formação fechada.

**Objetivo observável:** escolher e justificar lista, dicionário, tupla ou conjunto e aplicar sem ajuda os padrões acumular, contar, agrupar por chave, filtrar, buscar e maior/menor, inclusive em dados aninhados.

**Pré-requisito:** `lesson_15-logica-decomposicao` (concluída em 23/10). Continua valendo o método dela: entrada, regra, saída, exemplos com o esperado a mão, plano em português, só depois o código.

**Âncora no projeto:** índices do estudo fictício no app `segundo-cerebro`: tópico → evidências, lição → sessões, card → histórico. Entrega: um `indice.json` gerado e verificado com valor esperado.

**Fonte verificada:** Python Documentation, [5. Data Structures](https://docs.python.org/3/tutorial/datastructures.html) (`source_python-datastructures`): listas (5.1), tuplas (5.3), conjuntos (5.4), dicionários (5.5) e técnicas de laço (5.6).

Estrutura: **Teoria** (para reler), **Plano de prática** e **Progresso**.

## Teoria

> Escrita em 2026-10-24 para a abertura da lição (`theory_first`, tema novo). Material do tutor: **não é evidência** e não muda domínio. Os exemplos usam biblioteca e ônibus de propósito, para não entregar a tarefa do projeto.
>
> A teoria tem duas partes. A **parte 1** (as quatro estruturas e como escolher) foi dada em 24/10. A **parte 2** (os padrões) abre a próxima sessão, antes da prática.

### Problema e porquê

Até aqui você guardou valores soltos (`nota = 7`) ou numa lista. Os dados reais chegam **em grupo**: as evidências de um estudo, as sessões de uma lição, os livros emprestados numa biblioteca. A pergunta deixa de ser "qual valor?" e passa a ser **"como organizo esse grupo para responder rápido o que eu preciso?"**.

Uma **estrutura de dados** é a forma de organizar vários valores dentro do programa. A escolha muda três coisas:

- **como você acha um item:** pela posição, pelo nome ou "está ou não está?";
- **o que pode mudar depois:** acrescentar, trocar, remover;
- **quanto custa achar:** olhar item por item ou ir direto.

Exemplo do mundo real: numa estante, os livros ficam em fila (posição). Na ficha de um livro, cada informação tem um nome (título, autor). No carimbo de "já lido", só importa se está lá ou não.

### Como funciona: quatro caixas diferentes

| Estrutura | Analogia | Acha o item por | Pode mudar? | Repete? | Escreve-se |
|---|---|---|---|---|---|
| **lista** (`list`) | fila numerada de senhas | posição (`[0]`, `[1]`...) | sim | sim | `["a", "b"]` |
| **dicionário** (`dict`) | ficha com campos, ou uma agenda | chave (`["autor"]`) | sim | chaves não; valores sim | `{"autor": "Alencar"}` |
| **tupla** (`tuple`) | coordenada de um mapa, impressa | posição | **não** | sim | `(-23.55, -46.63)` |
| **conjunto** (`set`) | lista de presença: só nomes, sem ordem | "está ou não está?" (`in`) | sim | **não** | `{"a", "b"}` |

Como escolher, em quatro perguntas:

1. **A ordem importa, ou pode haver repetição?** → lista.
2. **Vou procurar pelo nome de alguma coisa** (o tópico, o livro, a parada)? → dicionário, com esse nome como chave.
3. **O grupo é fixo, um "registro" que não deve mudar** (latitude e longitude, data e hora)? → tupla.
4. **Só preciso saber se algo está presente, ou tirar repetidos?** → conjunto.

Sobre o **custo de achar**: para responder `"Iracema" in emprestimos`, a lista olha item por item até achar ou chegar ao fim. Com 4 itens, tanto faz; com 1 milhão, faz diferença. O dicionário e o conjunto vão **direto** ao item, como abrir a agenda na letra certa em vez de ler todas as páginas. Por isso se usa dicionário quando a pergunta é "quanto/quais para **este** nome?".

### Vocabulário

- **Estrutura de dados:** forma de organizar vários valores dentro do programa.
- **Elemento ou item:** cada valor guardado dentro da estrutura.
- **Índice:** a posição de um item numa lista ou tupla. Começa em **0**.
- **Chave e valor:** num dicionário, a chave é o nome ("autor") e o valor é o que fica guardado nela ("José de Alencar"). O par chave-valor também se chama **item**.
- **Mutável / imutável:** mutável pode mudar depois de criado (lista, dicionário, conjunto). Imutável não pode (tupla, texto, número).
- **Desempacotar:** separar os itens de uma tupla em variáveis numa linha só: `lat, lon = ponto`.
- **Hashable:** palavra em inglês para "pode servir de chave". Na prática: valores imutáveis (texto, número, tupla) podem ser chave de dicionário ou item de conjunto; listas e dicionários não podem.
- **Dados aninhados:** uma estrutura dentro da outra, como uma lista de dicionários, cada um com uma lista dentro.
- **`dict.get(chave, padrao)`:** lê uma chave sem dar erro se ela não existir; devolve `padrao` (ou `None`, se não houver padrão).
- **`set()`:** cria um conjunto vazio. `{}` sozinho é um **dicionário** vazio, não um conjunto.

### Exemplo básico, linha a linha: uma biblioteca

```python
emprestimos = ["Dom Casmurro", "O Cortiço", "Dom Casmurro", "Iracema"]
print(emprestimos[0], len(emprestimos))      # Dom Casmurro 4
print("Iracema" in emprestimos)              # True
```

- Linha 1: uma **lista**, porque a ordem dos empréstimos importa e o mesmo livro pode ser emprestado duas vezes.
- Linha 2: `[0]` é o primeiro item; `len` conta 4 itens, contando o repetido.
- Linha 3: `in` pergunta "está na lista?". A lista confere item por item.

```python
livro = {"titulo": "Iracema", "autor": "José de Alencar", "ano": 1865}
print(livro["autor"])                         # José de Alencar
print(livro.get("editora"))                   # None
print(livro.get("editora", "sem editora"))    # sem editora
```

- Um **dicionário**, porque cada informação tem um nome. Você pede pelo nome, não pela posição.
- `livro["editora"]` daria `KeyError`, porque a chave não existe. O `.get` devolve `None` ou o padrão que você der.

```python
ponto = (-23.55, -46.63)
lat, lon = ponto
print(lat, lon)                               # -23.55 -46.63
ponto[0] = 0      # TypeError: 'tuple' object does not support item assignment
```

- Uma **tupla**, porque latitude e longitude andam juntas e não devem ser trocadas por engano. Tentar mudar dá `TypeError`.
- `lat, lon = ponto` **desempacota**: o primeiro item vai para `lat`, o segundo para `lon`.

```python
titulos = set(emprestimos)
print(len(titulos), "Dom Casmurro" in titulos)   # 3 True
print(sorted(titulos))     # ['Dom Casmurro', 'Iracema', 'O Cortiço']
```

- `set(...)` cria um **conjunto** a partir da lista e **tira o repetido**: sobram 3 títulos.
- O conjunto **não tem ordem**. Para mostrar em ordem, use `sorted`, que devolve uma lista nova.
- Operações de conjunto: `{"a","b"} & {"b","c"}` → `{'b'}` (o que está nos dois); `|` junta os dois; `-` tira os do segundo.

### Exemplo aprofundado: dados aninhados de ônibus

```python
linhas = [
    {"linha": "8000", "paradas": ["Sé", "Paulista", "Pinheiros"]},
    {"linha": "702U", "paradas": ["Butantã", "Pinheiros"]},
    {"linha": "175T", "paradas": []},
]
print(linhas[0]["paradas"][1])                 # Paulista
```

Leia de fora para dentro: `linhas[0]` é o primeiro dicionário; `["paradas"]` é a lista de paradas dele; `[1]` é o segundo item dessa lista.

A pergunta "**quais linhas passam em cada parada?**" pede para inverter a organização: o dado vem por linha, mas a resposta é por parada. Isso pede um dicionário com a parada como chave:

```python
por_parada = {}
for registro in linhas:
    for parada in registro["paradas"]:
        if parada not in por_parada:
            por_parada[parada] = []
        por_parada[parada].append(registro["linha"])

print(por_parada)
# {'Sé': ['8000'], 'Paulista': ['8000'], 'Pinheiros': ['8000', '702U'], 'Butantã': ['702U']}
print(por_parada.get("Luz", []))               # []
```

- Dois `for`, um dentro do outro: o de fora anda pelas linhas de ônibus, o de dentro pelas paradas de cada uma.
- A guarda `if parada not in por_parada` cria a lista vazia **na primeira vez** que a parada aparece. Sem ela, o `.append` daria `KeyError`.
- A linha `175T` não tem paradas: o `for` de dentro não roda, e ela simplesmente não aparece. Esse é um caso-limite tratado sem código extra.
- `.get("Luz", [])` responde "nenhuma linha" para uma parada que não existe, sem erro.

### Erros comuns e limites

- **`KeyError`:** ler `d["chave"]` com uma chave que não existe. Use a guarda `if chave in d` ou `d.get(chave, padrao)`.
- **`{}` não é conjunto vazio:** `type({})` é `dict`. Para conjunto vazio, `set()`.
- **Tupla de um item precisa de vírgula:** `("so",)` é tupla; `("so")` é só um texto entre parênteses.
- **Lista não pode ser chave:** `{["x"]: 1}` dá `TypeError: unhashable type: 'list'`. Se precisar de chave com duas partes, use uma tupla: `{("2026-10-24", "Pinheiros"): ...}`.
- **Conjunto perde ordem e repetição:** se a ordem ou a quantidade importam, conjunto é a escolha errada.
- **Lista para "procure pelo nome":** funciona, mas obriga a percorrer tudo a cada pergunta. Se você pergunta pelo nome muitas vezes, monte um dicionário uma vez.

### Checagens de entendimento

Não são evidência; servem para ver se a explicação funcionou.

1. Para guardar o histórico de notas de um aluno, na ordem em que saíram, com notas repetidas, qual estrutura? Por quê?
2. O que imprime `print(len({"Sé", "Sé", "Luz"}))`?
3. Por que `por_parada[parada].append(...)` sem a guarda dá erro na primeira parada?

### Ponte para o projeto

No estudo fictício do app, cada evidência é um dicionário com `topic_id`, e cada sessão tem uma lista `lesson_ids`. As perguntas que o app precisa responder ("quais evidências tem este tópico?", "quais sessões tem esta lição?") são perguntas **por nome**. O índice do projeto é a mesma ideia de `por_parada`, aplicada a outro dado, que você vai decompor e montar sozinho na prática.

### Parte 2: os padrões

> Começada em 2026-10-24, no fim da sessão. Exemplos com viagens de ônibus, diferentes das tarefas do projeto. Saídas conferidas por execução.

Um **padrão** é uma receita de laço que aparece em quase todo problema com dados em grupo. Reconhecer o padrão é metade da decomposição: "isto é uma contagem", "isto é uma busca".

```python
viagens = [
    {"linha": "8000", "passageiros": 40},
    {"linha": "702U", "passageiros": 25},
    {"linha": "8000", "passageiros": 35},
    {"linha": "175T", "passageiros": 0},
]
```

| Padrão | Pergunta típica | Começa com | A cada item | Resultado no exemplo |
|---|---|---|---|---|
| **acumular** | quanto no total? | `total = 0` | `total += v["passageiros"]` | `100` |
| **contar por chave** | quantas de cada? | `contagem = {}` | `contagem[k] = contagem.get(k, 0) + 1` | `{'8000': 2, '702U': 1, '175T': 1}` |
| **agrupar por chave** | quais de cada? | `grupos = {}` | guarda da chave nova + `.append` | ver `por_parada` na parte 1 |
| **filtrar** | quais cumprem a regra? | `cheias = []` | `if regra: cheias.append(...)` | `['8000', '8000']` (≥ 30) |
| **buscar** | existe um? qual é o primeiro? | `achada = None` | `if regra: achada = v; break` | `{'linha': '175T', 'passageiros': 0}` |
| **maior / menor** | qual tem mais? | `maior = None` | `if maior is None or v[...] > maior[...]: maior = v` | `{'linha': '8000', 'passageiros': 40}` |

- **Contar** responde "quantos"; **agrupar** responde "quais". Os dois usam dicionário com a mesma chave, mas o valor muda: um número ou uma lista.
- **`break`** interrompe o `for` na hora: na busca, depois de achar o primeiro, não há por que continuar olhando.
- **Começar com `None`** em busca e maior/menor resolve o caso vazio: se não houver nenhum item, o resultado continua `None`, e o código que chamou decide o que fazer.

**Empate em maior/menor.** Com duas viagens de 30 passageiros (linhas A e B):

- com `>`, o primeiro encontrado fica: resultado `A`;
- com `>=`, o último encontrado fica: resultado `B`.

Nenhum dos dois está errado; errado é **não decidir**. A regra de empate vai para o enunciado e para um exemplo com o esperado a mão, como qualquer caso-limite.

## Plano de prática

### Índice 1: tópico → evidências (enunciado entregue em 2026-10-25)

O app precisa responder "quais evidências tem este tópico?" sem percorrer todas as evidências a cada pergunta. Monte o índice uma vez.

```python
topicos = ["topic_python", "topic_sql", "topic_git"]

evidencias = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
    {"evidence_id": "ev_02", "topic_id": "topic_git"},
    {"evidence_id": "ev_03", "topic_id": "topic_python"},
    {"evidence_id": "ev_04", "topic_id": "topic_react"},
]
```

Regras:

1. A saída tem **todos** os tópicos de `topicos`, mesmo os sem evidência.
2. Para cada tópico, os IDs das evidências dele, **na ordem em que aparecem** em `evidencias`.
3. Evidência de um tópico que não está em `topicos` fica **fora** do índice.
4. Escreva, num comentário, **por que** escolheu cada estrutura da saída.

Antes do código: entrada, regra, saída, exemplos com o esperado calculado a mão (incluindo casos-limite) e plano em português. Depois: a função, os `assert` com os seus esperados e uma execução.

### Andaime (usar só se precisar)

1. Reformular a pergunta do índice em português.
2. Recuperar a guarda de chave nova da `lesson_15`, problema 2.
3. Pergunta direcional: "o dado vem organizado por quê? a resposta é por quê?".
4. Pista parcial: o nome da estrutura do resultado, sem o laço.

### Tarefas independentes (só o enunciado; diferentes dos exemplos)

- **Índice 1:** tópico → lista de IDs de evidência do estudo fictício; tópico sem evidência aparece com lista vazia.
- **Índice 2:** lição → sessões, em que uma sessão pode estar em mais de uma lição (`lesson_ids` é lista: dado aninhado).
- **Índice 3:** card → histórico; com maior/menor e empate.
- Gerar `indice.json` e verificar com `assert` contra o esperado calculado a mão.

### Erros esperados

- `KeyError` na primeira chave nova.
- Escolher lista onde a pergunta é por nome, sem justificar.
- Esquecer o caso vazio ou a chave ausente.
- Empate em maior/menor sem regra declarada.

### Critérios de evidência

- **Aplicação padrão (60):** montar um índice do projeto de ponta a ponta, com a estrutura justificada por escrito, casos-limite (vazio, chave ausente, empate) e `assert` com esperado a mão.
- **Feynman (60):** explicar com as próprias palavras por que a estrutura escolhida responde a pergunta e o que aconteceria com outra.
- **Transferência (80):** aplicar os padrões em dados de outro domínio (Python Lab 001/002/003/005 ou o trabalho do aluno), com `transfer: true`.
- Prever uma saída ou um `assert` isolado é `supporting`.
- Diante de entrega parcial: uma vez por tarefa, "Confira sua solução contra cada regra e exemplo do enunciado." antes de qualquer devolutiva.

## Progresso

### Onde paramos (2026-10-27): decomposição do Índice 1 correta, código pendente

- Retomada da sessão `session_2026-10-25-lesson16-indice1-01` (20:53–21:48), concluída.
- Cards: fatia × `pop` (agora com o retorno do `pop`), os dois tipos de erro e o que prova a falta do `Traceback`. Os três certos.
- **Índice 1, decomposição:**
  - v1 parcial: saída como lista de dicionários, `topic_react` na saída, `topic_sql` ausente, e vazio devolvido se qualquer lista estivesse vazia;
  - a conferência genérica foi pedida uma vez;
  - v2 correta, sem outra ajuda: dicionário tópico → lista, `topic_sql: []`, `topic_react` fora, evidências vazias com os tópicos em listas vazias, e o caso de ordem `ev_03` antes de `ev_01`.
  - O aluno declarou ter usado uma IA só para formatar o markdown; os casos são dele.
- **Evidência:** `evidence_logica-indice1-decomposicao-01` (`supporting`). Ainda não é a aplicação padrão.
- **Falta para a aplicação padrão:** a função, o comentário justificando a estrutura, os `assert` com os esperados da v2 e a execução.
- **Falta para o 60:** também a explicação Feynman.

### Onde paramos (2026-10-25): Índice 1 entregue, sessão interrompida e retomável

- Sessão `session_2026-10-25-lesson16-indice1-01` (30 min, interrompida às 12:01 a pedido do aluno, `resumable: true`).
- Cards: `fieldnames` e `next` com padrão certos; fatia × `pop` parcial (o `pop` **devolve** o item).
- Recuperação da teoria: parcial. Lista e tupla certas; dicionário vago; conjunto não lembrado. O tutor completou.
- **Enunciado do Índice 1 entregue** (seção *Índice 1*, no Plano de prática). Nenhuma tentativa ainda e nada revelado além do enunciado.
- **Retomar:** a decomposição do aluno, sem andaime; depois função, `assert` e execução.

### Onde paramos (2026-10-24): teoria completa, prática pendente

- Sessão `session_2026-10-24-lesson16-teoria-01` (concluída, ~62 min de 60).
- Cards antes da teoria: 2 certos, 2 parciais, 1 não lembrado (detalhes no `session-log.md`).
- **Teoria escrita e dada, partes 1 e 2.** Checagens de entendimento (não são evidência):
  - lista para notas em ordem com repetição: certa;
  - `len({"Sé", "Sé", "Luz"})`: número certo por raciocínio errado (contou os repetidos); corrigido depois da explicação e confirmado numa variação;
  - sem a guarda: disse que dá erro, sem nomear o `KeyError` nem o porquê; o tutor rodou e mostrou `KeyError: 'Sé'`;
  - empate no menor com o último: `<=`, certa.
- **Domínio:** nenhuma evidência nesta sessão. Feynman e aplicação padrão da lição continuam em aberto.
- **Próxima sessão:** recuperação curta da teoria; depois o **Índice 1** só com o enunciado.
