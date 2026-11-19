# Lição `lesson_19-python-intermediario`

**Status:** em andamento, aberta em 2026-11-19 (`session_2026-11-19-lesson19-classes-teoria-01`). Tópico: `topic_python-intermediario` (domínio 0, tema novo). Ciclo 8 da formação fechada.

**Objetivo observável:** reescrever os dados da formação (tópico, lição, sessão, card) como dataclasses tipadas num pacote com `pyproject`, com logging e exceções próprias.

**Critérios de entrega:** modelos como dataclasses com dicas de tipo; pacote importável e instalável; logging configurado; exceção própria com teste; entrega por commit no repositório.

**Pré-requisito:** `lesson_17-algoritmos-debugging` (concluída em 17/11). Continua valendo decompor antes de codar e o debugging por hipótese.

**Âncora no projeto:** o pacote do app `segundo-cerebro`, com os modelos do estudo fictício. **Transferência prevista:** modelar sozinho uma entidade nova (fonte ou ponto fraco).

**Fontes verificadas:**

- Python Documentation, [9. Classes](https://docs.python.org/3/tutorial/classes.html) (`source_python-tutorial-classes`): `__init__` (9.3.2), objetos de instância (9.3.3), métodos (9.3.4), variáveis de classe e de instância (9.3.5) e `self` como convenção (9.4).
- Python Documentation, [dataclasses](https://docs.python.org/3/library/dataclasses.html) (`source_python-dataclasses`): `__init__`, `__repr__` e `__eq__` gerados; campos são variáveis de classe com anotação de tipo; padrão não hashável recusado com `ValueError`; `default_factory`; `slots=True`.

## Material em vídeo

Vídeo é aquecimento ou revisão: não substitui a teoria escrita e não é evidência. Mapa completo em `docs/compose/spec/material-video-python.md`.

| Quando | Material |
|---|---|
| **Antes ou depois da parte 1** (classes e objetos) | Guanabara, Curso Python POO, aulas 1 a 5 (classes, objetos, atributos) |
| Depois da parte 1, como revisão | Guanabara, Curso Python POO, aulas 7 a 12 (herança, abstração, encapsulamento, `@property`); estes temas vão além do objetivo da lição |
| Antes da parte 3 (pacote) | Guanabara, aula #22 (módulos e pacotes) |
| Revisão livre | Cod3r AI › Python (os 25% restantes); Cod3r DEV › Programação Orientada a Objetos e Introdução aos Paradigmas; DEV › Design › Modelagem de Domínio |
| **Só depois da sua tentativa** | Guanabara, desafios POO 16 a 33. Assistidos antes, a tarefa vira prática guiada. |

Sem vídeo de consulta ainda: `dataclasses`, dicas de tipo, `pyproject.toml`, `logging` e exceções próprias. Para esses, a fonte é a teoria escrita aqui.

Estrutura: **Teoria** (para reler), **Plano de prática** e **Progresso**.

## Teoria

> Material do tutor: **não é evidência** e não muda domínio. Os exemplos usam ônibus, playlists, lâmpadas e contadores de propósito, para não entregar a tarefa do projeto. Saídas conferidas por execução (Python 3.11).
>
> A teoria tem partes: **1** classes e objetos (19/11); **2** dicas de tipo e dataclasses; **3** módulos, pacote e `pyproject`; **4** logging; **5** exceções próprias com teste.

### Parte 1: classes e objetos

### Problema e porquê

Até aqui, todo dado do estudo foi um **dicionário**: `{"card_id": "c1", "due_at": "2026-11-20"}`. Funciona, mas tem três problemas que crescem com o app:

1. **Nada diz que forma um card tem.** Quem lê o código precisa adivinhar as chaves.
2. **Um erro de digitação não é avisado.** `card["due_on"] = "2026-11-25"` não dá erro: cria uma chave nova, e o card fica com duas datas. Conferido por execução:

   ```
   {'card_id': 'c1', 'due_at': '2026-11-20', 'due_on': '2026-11-25'}
   ```

3. **O comportamento fica espalhado.** As funções que mexem num card ficam soltas pelo código, longe do dado.

Uma **classe** junta numa peça só a **forma** do dado (que campos ele tem) e o **comportamento** dele (o que dá para fazer com ele).

Analogia: a classe é uma **ficha de cadastro em branco**, que diz quais campos existem. Cada **objeto** é uma ficha **preenchida**. Uma ficha em branco serve para preencher quantas fichas forem precisas, cada uma com seus próprios dados.

### Como funciona

```python
class Viagem:
    def __init__(self, linha, passageiros, capacidade):
        self.linha = linha
        self.passageiros = passageiros
        self.capacidade = capacidade
```

1. `class Viagem:` cria a ficha em branco. Nada é preenchido ainda.
2. `Viagem("8000", 40, 50)` **cria um objeto**: o Python faz uma ficha nova, vazia, e chama `__init__` **sozinho**, passando os valores.
3. Dentro do `__init__`, `self` **é a ficha que está sendo preenchida**. `self.linha = linha` escreve o campo `linha` **nessa** ficha.
4. O objeto pronto volta para quem chamou: `manha = Viagem("8000", 40, 50)`.

Quando você chama um método, `manha.lotacao()`, o Python faz por baixo `Viagem.lotacao(manha)`: o objeto antes do ponto vira o `self`. É por isso que todo método recebe `self` primeiro.

### Vocabulário

- **Classe:** o molde (a ficha em branco). Nome com inicial maiúscula, por convenção: `Viagem`.
- **Objeto** ou **instância:** uma ficha preenchida, criada a partir da classe.
- **Instanciar:** criar um objeto, chamando a classe como função: `Viagem("8000", 40, 50)`.
- **Atributo:** um campo do objeto, acessado com ponto: `manha.linha`.
- **Método:** uma função escrita dentro da classe, que trabalha com o objeto: `manha.lotacao()`.
- **`__init__`:** o método que o Python chama sozinho ao criar o objeto, para preencher os atributos iniciais. Os dois sublinhados antes e depois do nome indicam um método especial do Python.
- **`self`:** o próprio objeto, dentro dos métodos. O nome `self` é uma **convenção**, não uma palavra reservada, mas todo mundo usa.
- **Variável de classe:** escrita direto na classe, fora dos métodos. É **uma só**, compartilhada por todos os objetos.
- **Variável de instância:** escrita com `self.` (em geral no `__init__`). Cada objeto tem a sua.

### Exemplo básico, linha a linha: viagens de ônibus

```python
class Viagem:
    def __init__(self, linha, passageiros, capacidade):
        self.linha = linha
        self.passageiros = passageiros
        self.capacidade = capacidade

    def lotacao(self):
        return round(self.passageiros * 100 / self.capacidade)

    def esta_cheia(self):
        return self.passageiros >= self.capacidade


manha = Viagem("8000", 40, 50)
noite = Viagem("702U", 50, 50)
print(manha.linha, manha.lotacao(), manha.esta_cheia())
print(noite.linha, noite.lotacao(), noite.esta_cheia())
```

- `manha = Viagem("8000", 40, 50)`: cria um objeto; o `__init__` recebe `linha="8000"`, `passageiros=40`, `capacidade=50` e grava os três em `self`, que é a `manha`.
- `noite = Viagem("702U", 50, 50)`: outra ficha, com os dados dela. As duas não se misturam.
- `manha.lotacao()`: o `self` vira `manha`, então a conta é `40 * 100 / 50 = 80`.
- `noite.esta_cheia()`: `50 >= 50` é `True`.

Saída real:

```
8000 80 False
702U 100 True
```

Repare que `lotacao` e `esta_cheia` **não recebem os dados como argumento**: eles já estão no objeto. Essa é a vantagem de juntar dado e comportamento.

### Exemplo aprofundado: playlists e a lista compartilhada

Uma playlist guarda uma **lista** de músicas. Primeiro, o jeito errado: a lista como **variável de classe**.

```python
class PlaylistErrada:
    musicas = []

    def __init__(self, nome):
        self.nome = nome

    def adicionar(self, musica):
        self.musicas.append(musica)


treino = PlaylistErrada("Treino")
estudo = PlaylistErrada("Estudo")
treino.adicionar("Eye of the Tiger")
estudo.adicionar("Clair de Lune")
print(treino.musicas)
```

Saída real:

```
['Eye of the Tiger', 'Clair de Lune']
```

A música de estudo apareceu no treino. `musicas = []` fora do `__init__` cria **uma lista só**, da classe, e as duas playlists escrevem nela. É como um mural no corredor: todo mundo escreve no mesmo papel.

O jeito certo é criar a lista **no `__init__`**, com `self.`, para cada objeto ganhar a sua:

```python
class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar(self, musica, minutos):
        self.musicas.append({"titulo": musica, "minutos": minutos})

    def duracao_total(self):
        total = 0
        for m in self.musicas:
            total += m["minutos"]
        return total


treino = Playlist("Treino")
estudo = Playlist("Estudo")
treino.adicionar("Eye of the Tiger", 4)
treino.adicionar("Lose Yourself", 5)
estudo.adicionar("Clair de Lune", 5)
print(treino.duracao_total(), estudo.duracao_total())
```

Saída real: `9 5`. O método `duracao_total` usa o padrão **acumular**, da `lesson_16`, só que agora sobre um atributo do objeto.

### Erros comuns e limites

- **Esquecer `self` no método.** O Python passa o objeto mesmo assim, e sobra um argumento:

  ```python
  class Lampada:
      def __init__(self):
          self.acesa = False

      def ligar():
          self.acesa = True

  Lampada().ligar()
  ```

  ```
  TypeError: Lampada.ligar() takes 0 positional arguments but 1 was given
  ```

  "Recebe 0 argumentos, mas 1 foi dado": o 1 é o objeto, que o Python passou como `self`.

- **Esquecer o `self.` na atribuição.** `valor = 0` dentro do `__init__` cria uma variável local, que some quando o método termina. Depois, `c.valor` dá `AttributeError: 'Contador' object has no attribute 'valor'`.
- **Lista ou dicionário como variável de classe**, quando cada objeto deveria ter o seu: os objetos passam a dividir o mesmo dado (exemplo das playlists).
- **Esquecer os parênteses:** `manha.lotacao` (sem `()`) não chama o método; devolve o próprio método.
- **Limite desta parte:** a classe ainda não confere os tipos, e o objeto aceita atributos novos com erro de digitação (`manha.passageros = 3` cria outro atributo). As dicas de tipo e as dataclasses, na parte 2, atacam isso.

### Checagens de entendimento

Não são evidência.

1. Na analogia da ficha, o que é a classe e o que é o objeto?
2. Preveja a saída de `print(Viagem("175T", 10, 40).lotacao())`.
3. Por que `ligar()` sem `self` dá `TypeError`, se a chamada `l.ligar()` não passa nenhum argumento?
4. Na `PlaylistErrada`, onde está a única lista, e por que as duas playlists escrevem nela?

### Ponte para o projeto

No app, um card hoje é um dicionário. Com uma classe, o card passa a ter forma declarada (`card_id`, `due_at`) e comportamento junto do dado, como "está vencido em tal data?". A prática desta lição começa por aí, depois da parte 2, quando as dataclasses deixarem o modelo mais curto e com tipos.

### Parte 2: dicas de tipo e dataclasses

> Escrita em 2026-11-19. Fonte: Python Documentation, [dataclasses](https://docs.python.org/3/library/dataclasses.html) (`source_python-dataclasses`). Saídas conferidas por execução (Python 3.11).

### Problema e porquê

A classe da parte 1 resolveu a forma e o comportamento, mas deixou três coisas para trás:

1. **O tipo de cada campo não está escrito.** Quem lê `Viagem("8000", 40, 50)` não sabe se `passageiros` é número ou texto.
2. **O `__init__` é repetitivo.** Cada campo aparece três vezes: no parâmetro, em `self.campo` e no valor.
3. **O objeto comum não se mostra nem se compara.** Conferido por execução com a `Viagem` da parte 1:

   ```
   <__main__.Viagem object at 0x...>
   False
   ```

   O `print` mostra só um endereço de memória, e duas viagens com os **mesmos** dados não são iguais com `==`, porque o Python compara se são **o mesmo objeto**, não se têm os mesmos dados.

As **dicas de tipo** resolvem o primeiro problema, e as **dataclasses** resolvem os três de uma vez.

### Como funciona: dicas de tipo

Uma **dica de tipo** (em inglês, *type hint*) é uma anotação que diz o tipo esperado. Ela vem depois de dois-pontos, e o tipo da resposta vem depois de `->`:

```python
def lotacao(passageiros: int, capacidade: int) -> int:
    return round(passageiros * 100 / capacidade)
```

Lê-se: "`passageiros` é `int`, `capacidade` é `int`, e a função devolve `int`".

**O Python não confere a dica ao rodar.** Ela é documentação que o editor e ferramentas de verificação (como o `mypy`) leem. Conferido por execução:

```python
def dobro(x: int) -> int:
    return x * 2

print(dobro("ab"))   # abab, sem erro
```

Tipos mais usados:

| Dica | Significa |
|---|---|
| `int`, `float`, `str`, `bool` | número inteiro, número com vírgula, texto, verdadeiro/falso |
| `list[str]` | lista de textos |
| `dict[str, int]` | dicionário com chave texto e valor inteiro |
| `str \| None` | texto **ou** `None` (por exemplo, uma data que pode faltar) |

### Como funciona: dataclasses

Uma **dataclass** é uma classe em que o Python **escreve sozinho** o `__init__`, o `print` legível e a comparação com `==`, a partir dos campos anotados.

```python
from dataclasses import dataclass


@dataclass
class Viagem:
    linha: str
    passageiros: int
    capacidade: int = 50
```

- `from dataclasses import dataclass` traz a ferramenta do módulo `dataclasses`, que já vem com o Python.
- `@dataclass` em cima da classe é um **decorador**: uma linha com `@` que acrescenta recursos à classe logo abaixo. Aqui, ele gera o `__init__`, o `__repr__` (o texto que o `print` mostra) e o `__eq__` (a comparação com `==`).
- Cada linha `nome: tipo` é um **campo**. A ordem dos campos é a ordem dos argumentos.
- `capacidade: int = 50` é um campo com **valor padrão**: se ninguém passar, vale 50. Campos com padrão vêm **depois** dos campos sem padrão.

### Vocabulário

- **Dica de tipo (*type hint*):** anotação `nome: tipo` ou `-> tipo`. Documenta; não é conferida pelo Python ao rodar.
- **Decorador:** linha com `@` em cima de uma classe ou função, que acrescenta recursos a ela.
- **Dataclass:** classe marcada com `@dataclass`, que tem o `__init__`, o `__repr__` e o `__eq__` gerados a partir dos campos.
- **Campo:** cada linha `nome: tipo` da dataclass. Vira atributo do objeto.
- **Valor padrão:** o valor de um campo quando ninguém passa outro (`capacidade: int = 50`).
- **`field(default_factory=list)`:** padrão que **cria uma lista nova para cada objeto**. É o jeito certo de dar lista vazia como padrão.
- **`__repr__`:** o texto que representa o objeto no `print`.
- **`__eq__`:** o que o `==` usa para comparar dois objetos.

### Exemplo básico, linha a linha: a viagem como dataclass

```python
from dataclasses import dataclass


@dataclass
class Viagem:
    linha: str
    passageiros: int
    capacidade: int = 50

    def lotacao(self) -> int:
        return round(self.passageiros * 100 / self.capacidade)


manha = Viagem("8000", 40)
print(manha)
print(manha.lotacao())
print(manha == Viagem("8000", 40))
```

Saída real:

```
Viagem(linha='8000', passageiros=40, capacidade=50)
80
True
```

- `Viagem("8000", 40)`: o `__init__` gerado recebe `linha` e `passageiros`; `capacidade` fica com o padrão 50.
- `print(manha)`: o `__repr__` gerado mostra todos os campos, em vez do endereço de memória.
- `==` agora compara os **dados**: duas viagens com os mesmos campos são iguais.
- O método `lotacao` funciona igual à parte 1. A dataclass continua sendo uma classe.

Um erro de digitação no **nome do argumento** agora é avisado na hora:

```python
Viagem(linha="702U", passageros=50)
```

```
TypeError: Viagem.__init__() got an unexpected keyword argument 'passageros'
```

### Exemplo aprofundado: a playlist com `default_factory`

O erro da lista compartilhada (parte 1) não passa numa dataclass. Tentar `musicas: list = []` dá erro **ao criar a classe**:

```
ValueError: mutable default <class 'list'> for field musicas is not allowed: use default_factory
```

O jeito certo é `field(default_factory=list)`, que chama `list()` e cria uma lista nova **para cada objeto**:

```python
from dataclasses import dataclass, field


@dataclass
class Playlist:
    nome: str
    musicas: list[str] = field(default_factory=list)

    def adicionar(self, musica: str) -> None:
        self.musicas.append(musica)


treino = Playlist("Treino")
estudo = Playlist("Estudo")
treino.adicionar("Eye of the Tiger")
estudo.adicionar("Clair de Lune")
print(treino)
print(estudo)
```

Saída real:

```
Playlist(nome='Treino', musicas=['Eye of the Tiger'])
Playlist(nome='Estudo', musicas=['Clair de Lune'])
```

`-> None` diz que `adicionar` não devolve nada: ela só muda o objeto.

### Erros comuns e limites

- **Achar que a dica de tipo é conferida.** `Viagem("8000", "quarenta")` é aceito e mostra `Viagem(linha='8000', passageiros='quarenta', capacidade=50)`. O erro só aparece quando alguém fizer conta com o texto.
- **Lista ou dicionário como padrão direto** (`= []`, `= {}`): `ValueError` ao criar a classe. Use `field(default_factory=list)` ou `field(default_factory=dict)`.
- **Campo sem padrão depois de campo com padrão:** a ordem dos argumentos ficaria ambígua, e o Python recusa a classe.
- **Esquecer o `@dataclass`:** a classe vira uma classe comum sem `__init__`, e `Viagem("8000", 40)` dá `TypeError`.
- **Erro de digitação depois de criado:** `manha.passageros = 3` ainda cria um atributo novo, sem aviso. Com `@dataclass(slots=True)`, isso dá `AttributeError: 'V' object has no attribute 'passageros'`. É um recurso extra, sem uso obrigatório nesta lição.

### Checagens de entendimento

Não são evidência.

1. O que o `@dataclass` escreve sozinho, e o que você continua escrevendo?
2. Preveja a saída de `print(Viagem("175T", 10, 40))`.
3. Por que `Viagem("8000", "quarenta")` não dá erro ao criar?
4. Por que a dataclass recusa `musicas: list = []`, e o que resolve?

### Ponte para o projeto

Os modelos do app (tópico, lição, sessão e card) viram dataclasses: cada um com os campos e os tipos escritos, uma data que pode faltar como `str | None`, e listas com `default_factory`. É a primeira tarefa da prática.

## Plano de prática

- **Núcleo cognitivo:** modelar sozinho os dados da formação como dataclasses tipadas, decidindo campos, tipos, padrões e métodos.

### Tarefa 1: card e sessão como dataclasses (enunciado entregue em 2026-11-19)

Os cards do estudo fictício chegam como dicionários, e nem todo card tem todos os campos:

```python
dados_cards = [
    {"card_id": "c1", "topic_id": "topic_python", "due_at": "2026-11-18", "review_count": 3, "last_result": "correct"},
    {"card_id": "c2", "topic_id": "topic_git", "due_at": "2026-11-19"},
    {"card_id": "c3", "topic_id": "topic_sql", "due_at": "2026-11-25", "review_count": 1, "last_result": "partial"},
]
```

Regras:

1. Uma dataclass `Card` com `card_id`, `topic_id`, `due_at`, `review_count` e `last_result`, cada campo com dica de tipo.
   - Card sem `review_count` começa com `0`; card sem `last_result` fica com `None`.
2. Um método do `Card` diz se ele está **vencido numa data**: vencido quando `due_at` é **igual ou anterior** à data.
3. Uma função recebe a lista de dicionários e devolve a **lista de objetos `Card`**, na mesma ordem.
4. Uma dataclass `Sessao` com `session_id`, `started_at`, `ended_at` (que pode faltar) e `lesson_ids` (lista de lições, vazia por padrão), com dicas de tipo.
5. Um método da `Sessao` diz se ela **está aberta**: aberta quando não tem `ended_at`.
6. Duas sessões criadas sem `lesson_ids` **não** podem dividir a mesma lista.
7. `assert` com os esperados calculados **à mão**: os três cards convertidos, os vencidos em `"2026-11-19"` (incluindo o caso da data igual), dois cards com os mesmos dados iguais com `==`, uma sessão aberta e uma fechada, e a regra 6.

Antes do código: entrada, regra, saída, exemplos com o esperado à mão (casos-limite incluídos) e plano em português, num `modelos.md` em `segundo-cerebro/exercicios/modulo 06/`. Depois, o `modelos.py` na mesma pasta.

## Progresso

### Onde paramos (2026-11-19): partes 1 e 2 dadas, Tarefa 1 correta

- **Sessão:** `session_2026-11-19-lesson19-classes-teoria-01`, 15:31–17:16 (cerca de 105 min, além dos 60).
- **Fase e estratégia:** `topic_python-intermediario` em 0, superfície (aquisição): teoria do zero.
- **Cards:** 3 de 3 certos (`tempos-06`, `tempos-07`, `cond-03`).
- **Teoria das partes 1 e 2:** dadas em blocos. Checagens (não são evidência):
  - chamou a classe de "instância"; ensinado: a classe é a ficha em branco, e as instâncias são as fichas preenchidas;
  - `lotacao()` de `Viagem("175T", 10, 40)` = 25, certo;
  - a lista da `PlaylistErrada` está no lugar certo, mas é compartilhada **entre objetos**, não entre métodos (o mural);
  - dica de tipo documenta (e o editor e o `mypy` leem), o `repr` da dataclass e o `default_factory`: certos.
- **Tarefa 1 (Card e Sessão como dataclasses):** `segundo-cerebro/exercicios/modulo 06/dataclass.md` e `.py`, completos e corretos de primeira, depois do enunciado reformulado a pedido. `evidence_intermediario-modelos-card-sessao-01` (apoio: cobre só a modelagem do objetivo).
- **Janelas quebradas (pendências pequenas):** renomear os arquivos para `modelos.md` e `modelos.py`, como pedia o enunciado, antes da parte 3; opcional, dicas de tipo em `converter_dicionarios`.
- **Ensinado na devolutiva:** `Card(**item)` desempacota o dicionário em argumentos com nome; as chaves precisam ser exatamente os nomes dos campos.
- **Regra 9:** domínio 0 → 40. Modelos ✅; faltam pacote, logging e exceção própria (partes 3 a 5) e o Feynman.
- **Próximo:** recuperação curta das partes 1 e 2 e a teoria da parte 3 (módulos, pacote e `pyproject`).
