# Lição `lesson_15-logica-decomposicao`

**Status:** em andamento desde 2026-10-09 (`session_2026-10-09-lesson15-abertura-01`). Tópico: `topic_logica-algoritmos`. Ciclo 5 da formação fechada.

## Onde paramos (2026-10-16): problema 2 fechado, sessão concluída

A sessão `session_2026-10-13-lesson15-problema2-01` foi concluída em 16/10, às 19:59, depois de quatro trechos (13, 15, 15 à noite e 16/10).

**Código final** (`exe_01.py`, `6088b9fd…`):
- uma gaveta por tópico, criada a partir de `topicos`;
- uma evidência com `evidence_id` vazio não conta;
- o caso vazio segue o contrato: com a lista de evidências vazia, cada tópico sai com `0`; com a lista de tópicos vazia, sai `{}`;
- 4 `assert` com mensagem, dentro do bloco `__main__`;
- sem código morto.

**Conceitos trabalhados em 16/10:**
- **Duas situações diferentes:** "tópico sem evidência" (a gaveta aparece com `0`) não é o mesmo que "evidência sem `evidence_id`" (a ficha não entra na gaveta).
- **Caso-limite:** uma entrada na beirada da regra, onde é mais fácil a regra falhar.
- **Contrato da saída:** cada chave do resultado é um tópico pedido. Um `{"lista": 0}` quebra esse contrato.
- **Laço sobre lista vazia:** dá zero voltas. O que está recuado dentro dele não executa.
- **Código morto:** código que nunca é executado. O teste passar com e sem ele é um sinal.
- **`assert` que passa fica em silêncio.** Só aparece mensagem quando ele falha.

**Evidências de 16/10:**
- `evidence_logica-caso-limite-assert-01`: `assert` isolado com literais, **autônomo e correto**. É a primeira saída de `weak_python-test-literal-lista`; falta outra, em outra sessão.
- `evidence_logica-caso-vazio-01`: caso vazio só com o enunciado, **incorreto**. Os esperados estavam fora do contrato, e o código foi ajustado a eles.
- `evidence_logica-rastreio-laco-vazio-01`: rastreio do laço vazio, **incorreto**.
- `evidence_logica-laco-vazio-feynman-01`: explicação **guiada**, correta.

**Domínio (regra 9):** `topic_logica-algoritmos` segue em **40**.
- ✅ A metade **Feynman** do 60 foi cumprida em 13/10.
- ⏳ Falta a **aplicação autônoma**.

### O que falta para concluir a lição

| Requisito | Situação |
|---|---|
| Plano escrito antes do código em pelo menos 3 problemas | 2 de 3 (problemas 1 e 2). Falta o **problema 3**: pontos fracos ativos. |
| Tabelas de rastreio conferidas por execução | Falta uma tabela **montada pelo aluno**. A de 16/10 foi feita pelo tutor. |
| Funções testadas com valor esperado à mão | Cumprido nos problemas 1 e 2. |
| Domínio 60 em `topic_logica-algoritmos` | Feynman ✅; falta uma aplicação autônoma correta. |
| Domínio 80 | Falta uma aplicação autônoma em contexto novo (Python Lab 006/007 ou tarefa do estágio sem dados da empresa). |
| Repositório `segundo-cerebro` (roteiro da formação) | A pasta existe, mas ainda não é repositório Git. |

**Próximo:** criar o repositório Git `segundo-cerebro` (o aluno executa os comandos). Depois, o problema 3 só com o enunciado: decomposição, casos-limite, previsão antes de rodar, `assert` e uma tabela de rastreio feita pelo aluno.

## Onde paramos (2026-10-15), sessão interrompida e retomável

Sessão de 13/10 retomada em 15/10, das 19:25 às 20:25 (cerca de 60 de 45 min).

- **Gavetas:** "Eu preciso de uma gaveta para cada tópico" (correto, depois da pergunta direcional de 13/10).
- **Código do aluno** (`exe_01.py`, `494f60e3…`): um dicionário `result` com uma chave por tópico começando em `0`, e `result[topico] += 1` dentro do laço. Saiu o `evicence_id` e o `return 0`. A saída com a lista do arquivo está certa: `{'topic_python': 2, 'topic_sql': 2, 'topic_git': 1, 'topic_javascript': 1}`.
- **Bloqueio aberto:** as quatro chaves estão **escritas à mão**, e não criadas a partir do parâmetro `topicos`. Com outra lista de tópicos, a função erra. O próprio exemplo 1 da tabela abaixo (tópicos sem `javascript`) não passaria.
- Evidência `evidence_logica-gavetas-problema2-02`: aplicação **parcial**, depois do degrau 3. `topic_logica-algoritmos` continua em 40.
  - ✅ A metade **Feynman** do 60 foi cumprida em 13/10.
  - ⏳ Falta a **aplicação autônoma**.

**Atualização das 20:52** (o aluno trabalhou sozinho depois de encerrar e pediu revisão): `exe_01.py`, `def56e11…`.
- ✅ As gavetas agora são **criadas a partir de `topicos`** (`result[topico] = 0` dentro do laço). Com `["topic_python", "topic_rust"]`, sai `{python: 2, rust: 0}`, e o exemplo 1 passa.
- **Regra nova, criada só no código:** evidência com `evidence_id` vazio não conta. Ela ainda não está na decomposição.
- Evidência `evidence_logica-gavetas-problema2-03`: aplicação parcial, depois da devolutiva.

**Próximo:**
1. decidir e escrever na decomposição a regra do `evidence_id` vazio, com um exemplo de caso-limite;
2. fazer o caso vazio devolver um dicionário;
3. escrever um `assert` por exemplo, prevendo o resultado antes de rodar.

## Onde paramos (2026-10-13), sessão interrompida e retomável

**Problema 2: evidências por tópico.** A decomposição está pronta, feita com ajuda dos degraus 1 a 3:

- **Entrada:** a lista de evidências e a lista de tópicos pedidos. Os nomes dos tópicos são iguais ao `topic_id` (`"topic_python"`). O próprio aluno percebeu o descompasso entre `"python"` e `"topic_python"`.
- **Saída:** um dicionário `tópico → quantidade`. Um tópico pedido sem evidência vale **0**, porque é um tópico não iniciado (decisão do aluno).

| # | Evidências | Tópicos | Esperado | Testa |
|---|---|---|---|---|
| 1 | 2 de python, 2 de sql, 1 de git, 1 de javascript | python, sql, git | `{python: 2, sql: 2, git: 1}` | caso normal; o tópico que não foi pedido fica de fora |
| 2 | 2 de python, 2 de sql, 1 de git | python, sql, git, javascript | `{…, javascript: 0}` | tópico pedido sem evidência |

**Pré-requisito ensinado** (regras 1 e 7): criar uma chave nova num dicionário.
- `d[chave] = 0` **cria** a chave.
- `d[chave] += 1` **lê** o valor e soma; se a chave não existe, dá `KeyError`.
- Houve dois exemplos executados, `estoque` e `placar`.

**Código em andamento:** `segundo-cerebro/exercicios/exe_01.py` (`a4d0cff5…`). O bloqueio é que existe **um contador para todos os tópicos**, quando o painel precisa de uma "gaveta" para cada tópico.

**Próximo:** retomar pela pergunta "quantas gavetas o seu código tem, para 4 tópicos?", com o rastreio à mão do exemplo 1. Depois:
1. rodar o código e ler o traceback;
2. tirar o `return 0` de dentro do laço;
3. fazer o caso vazio devolver um dicionário;
4. escrever um `assert` por exemplo, prevendo o resultado antes de rodar.

## Onde paramos (2026-10-12)

**Problema 1: fechado.** A versão final (`f4898339…`) usa um `if` só, `card["due_at"] == None or card["due_at"] <= hoje`. O `or` funciona aqui porque as duas condições levam à mesma ação. O `None` vem primeiro, como **guarda**, e 6 `assert` passam com os esperados da tabela.

**Curto-circuito** (revisto em 12/10):
- `or` para quando a primeira é **True**;
- `and` para quando a primeira é **False**.

Com a ordem invertida, a comparação impossível (`None <= "texto"` → `TypeError`; `fila[0]` com a fila vazia → `IndexError`) acontece antes da guarda.

**Próximo:**
1. uma pergunta rápida de `and`/`or`;
2. o Feynman "o esperado vem da regra", feito sozinho;
3. o **problema 2** (evidências por tópico), decomposto sozinho antes do código.

## Onde paramos (2026-10-11)

Feito: saída `int`, lista vazia → `0`, `>=` no lugar de `>`, verificação do "sem data" **antes** da comparação, um `assert` por linha da tabela com a data fixa `"2026-10-09"`.

Falta:

1. "sem data" e "venceu" se excluem → `if`/`elif` (hoje o card com `""` conta 2);
2. o teste do "sem data" usar `None` (o `null` do JSON), não `""`;
3. todos os `assert` passando com os esperados **da tabela**, sem rodar o código para descobrir o esperado.

**Conceito reforçado em 11/10: de onde vem o esperado.** O esperado sai da **regra**; o obtido sai do **código**. Se o esperado for copiado da execução, o teste confere o código com ele mesmo — como perguntar ao caixa qual é o troco certo e conferir o troco dele com a resposta dele.

Pré-requisito ensinado em 11/10: `null` no JSON vira `None` no Python; `None` ("sem valor") ≠ `""` (texto vazio). Texto vazio vem antes de qualquer texto: `"2026-10-09" >= ""` é `True`.

## Onde paramos (2026-10-09)

**Problema 1: "contar cards vencidos".** A decomposição foi feita com ajuda:

| # | `due_at` dos cards | `hoje` | Esperado | Testa |
|---|---|---|---|---|
| 1 | `"2026-10-05"`, `"2026-10-12"` | `"2026-10-09"` | 1 | caso normal |
| 2 | `"2026-10-09"` | `"2026-10-09"` | 1 | vence hoje |
| 3 | `None` | `"2026-10-09"` | 1 | sem data conta (regra do aluno: "se não posso comprovar a data, ele deve ser revisado") |
| 4 | `[]` | `"2026-10-09"` | 0 | lista vazia |

O código está em `segundo-cerebro/exercicios/contar_vencidos.py`. Ainda faltam quatro ajustes:

1. o sentido da comparação;
2. a saída como `int`;
3. um `assert` por linha da tabela, com a data fixa;
4. o `None` verificado antes da comparação.

## Objetivo observável

Antes de escrever código:

1. definir entrada, regra e saída;
2. montar de 3 a 5 exemplos com a saída esperada calculada à mão, incluindo casos-limite;
3. escrever um plano em português, dividido em subproblemas.

Depois, implementar cada subproblema como função e verificá-la com `assert`, usando o valor esperado que o próprio aluno escolheu. Também prever com uma tabela de rastreio o que faz um código com laço e condicional.

## Âncora no projeto

App `segundo-cerebro` (o app da formação). Esta lição **cria o repositório** e responde perguntas sobre o **estudo fictício** gerado com `scripts/init_study.py` dentro dele. O estudo real só é lido localmente e nunca entra no repositório.

Perguntas candidatas, uma por problema:

- Quantos cards estão vencidos numa data?
- Quantas evidências cada tópico tem?
- Quais pontos fracos estão ativos?

## Pré-requisitos

- `lesson_02-arquivos-erros`: concluída.
- O diagnóstico `diagnostic_2026-10-06-logica-01` (`partial`) posicionou a entrada. Laço, acumulador e `if` servem de base. Os focos são:
  - exemplos esperados **em números**;
  - `assert` explícito;
  - tabela de rastreio montada pelo aluno;
  - dicionário com chave nova.

## Fontes verificadas

- Python Documentation, [4. More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (`source_python-controlflow`): `if`/`elif`, `for` e funções.
- Python Documentation, [5. Data Structures](https://docs.python.org/3/tutorial/datastructures.html) (`source_python-datastructures`): listas, dicionários e a comparação **lexicográfica** de sequências (seção 5.8). Comparar texto também segue essa regra.

## Conceitos a ensinar antes de avaliar (regra 1)

- **Data em texto no formato ISO** (`"AAAA-MM-DD"`). Duas datas nesse formato podem ser comparadas como texto com `<`, `<=` e `>`. A comparação vai caractere por caractere, da esquerda para a direita, igual à ordem de um dicionário de papel. Como o ano vem antes do mês e o mês antes do dia, todos com zeros à esquerda, a ordem do texto é igual à ordem do calendário.
  - Contraexemplo: `"9/10/2026"` não serve.
- **`assert`** como verificação com mensagem de falha: `assert obtido == esperado, f"esperava {esperado}, veio {obtido}"`.

## Opções de andaime (usar só se precisar)

1. Reformular o problema com um card só.
2. Recuperar o pré-requisito: o percurso de uma lista de dicionários, já usado em `ordens.json`.
3. Pergunta direcional sobre o caso-limite que faltou.
4. Pista parcial: qual comparação decide "vencido".
5. Esqueleto incompleto da função (tem teto de 20).

## Variações de tarefa independente

- Contar os cards vencidos por **status** (`new`, `learning`, `review`).
- Listar os `card_id` vencidos, em vez de só contar.
- Transferência: Python Lab 006/007, ou uma tarefa do estágio sem dados da empresa.

## Erros esperados

- Usar `<` no lugar de `<=`: o card que vence hoje fica fora.
- Esquecer a lista vazia.
- Comparar datas em outro formato.
- Escrever o `assert` com o valor que o código devolveu, em vez do valor calculado à mão.

## Critérios de evidência

- `application` (autônoma): o plano escrito antes do código em pelo menos 3 problemas; as funções testadas com valor esperado escolhido pelo aluno.
- `feynman` (autônoma): explicar por que decompor e escrever o esperado antes de rodar evita o erro de "parece certo".
- `transfer`: decompor sozinho um problema de outro contexto.
- Saídas dos pontos fracos: ver `programming_plan.weak_point_exits` no `state.json`.

## Atualização de estado

Ao fechar cada sessão:

- registrar o checkpoint e as evidências autônomas reais;
- registrar o hash SHA-256 dos arquivos do aluno enquanto não houver commit.

A lição só passa a `completed` com domínio 80 em `topic_logica-algoritmos` e com os três critérios de entrega cumpridos.
