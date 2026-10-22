# Lição `lesson_15-logica-decomposicao`

**Status:** em andamento desde 2026-10-09 (`session_2026-10-09-lesson15-abertura-01`). Tópico: `topic_logica-algoritmos`. Ciclo 5 da formação fechada.

Estrutura: **Teoria** (para reler), **Plano de prática** e **Progresso** (onde paramos). O checkpoint mais recente é o primeiro item de Progresso.

## Teoria

> Resumo escrito em 2026-10-17, quando o estudo adotou `teaching_policy: theory_first` (skill `6a43e26`). A lição começou em 09/10, antes de a teoria ficar escrita no arquivo. Os conceitos abaixo **já foram ensinados** nas sessões de 09 a 16/10 e estão aqui para reler sem o chat. É material do tutor: **não é evidência** e não muda domínio.

### Problema e porquê

Um programa pequeno pode "parecer certo" e estar errado. Isso acontece quando o valor esperado é descoberto rodando o próprio código: o teste passa a conferir o código com ele mesmo, como perguntar ao caixa qual é o troco certo e conferir o troco dele com a resposta dele.

**Decompor** um problema antes de programar evita isso. Você escreve primeiro o que entra, qual é a regra e o que sai, e calcula à mão o resultado de alguns exemplos. Só depois escreve o código, e o código precisa chegar nesses números.

### Como funciona: o caminho da regra até o `assert`

1. **Entrada:** o que a função recebe (por exemplo, a lista de cards e a data de hoje).
2. **Regra:** a frase em português que decide o resultado ("um card sem data deve ser revisado").
3. **Saída:** o que a função devolve, com o tipo certo (um `int`, um dicionário).
4. **Exemplos com o esperado à mão:** de 3 a 5 linhas numa tabela, incluindo **casos-limite**.
5. **Plano em português:** os subproblemas, na ordem em que vão virar código.
6. **Código:** uma função por subproblema.
7. **Verificação:** um `assert` por linha da tabela, comparando o **obtido** (do código) com o **esperado** (da regra).

O esperado vem da **regra**; o obtido vem do **código**. Se os dois saem do mesmo lugar, o teste não prova nada.

### Vocabulário

- **Decomposição:** quebrar um problema em entrada, regra, saída e subproblemas antes de escrever código.
- **Valor esperado × valor obtido:** o esperado é calculado à mão a partir da regra; o obtido é o que o código devolve.
- **Caso-limite:** uma entrada na beirada da regra, onde é mais fácil a regra falhar. Exemplos: a lista vazia, o card que vence hoje, o card sem data.
- **Contrato da saída:** a promessa sobre o formato do resultado. No problema 2, cada chave do dicionário é um tópico pedido. Um `{"lista": 0}` quebra esse contrato, mesmo que o teste tenha sido ajustado para aceitá-lo.
- **`assert`:** verificação que interrompe o programa com uma mensagem quando a condição é falsa: `assert obtido == esperado, f"esperava {esperado}, veio {obtido}"`. Quando passa, fica em silêncio.
- **Tabela de rastreio:** uma tabela que acompanha, volta a volta, o valor de cada variável enquanto o código roda. Serve para prever o resultado antes de executar.
- **Guarda:** a condição verificada primeiro para impedir uma operação impossível depois (por exemplo, testar se a data é `None` antes de compará-la).
- **Curto-circuito:** o Python para de avaliar assim que já sabe o resultado. O `or` para quando a primeira condição é `True`; o `and` para quando a primeira é `False`. É isso que faz a guarda funcionar.
- **`None` × `""`:** `null` no JSON vira `None` no Python. `None` quer dizer "sem valor"; `""` é um texto vazio. Texto vazio vem antes de qualquer texto: `"2026-10-09" >= ""` é `True`.
- **Dicionário com chave nova:** `d[chave] = 0` **cria** a chave; `d[chave] += 1` **lê** o valor e soma. Se a chave não existe, o `+= 1` dá `KeyError`.
- **Laço sobre lista vazia:** dá zero voltas. O que está recuado dentro dele não executa.
- **Código morto:** código que nunca é executado. O teste passar com e sem ele é um sinal.
- **Data em texto no formato ISO** (`"AAAA-MM-DD"`). Duas datas nesse formato podem ser comparadas como texto com `<`, `<=` e `>`. A comparação vai caractere por caractere, da esquerda para a direita, igual à ordem de um dicionário de papel. Como o ano vem antes do mês e o mês antes do dia, todos com zeros à esquerda, a ordem do texto é igual à ordem do calendário.
  - Contraexemplo: `"9/10/2026"` não serve.

### Exemplos já trabalhados

- **Problema 1, cards vencidos** (`contar_vencidos.py`): a regra "vencido é `due_at <= hoje`, e sem data também conta" virou um `if` só, `card["due_at"] == None or card["due_at"] <= hoje`. O `or` funciona aqui porque as duas condições levam à mesma ação, e o `None` vem primeiro como guarda. A tabela de 09/10, na seção Progresso, mostra os quatro exemplos, incluindo os casos-limite.
- **Problema 2, evidências por tópico** (`exe_01.py`): uma "gaveta" (chave do dicionário) para cada tópico pedido, criada a partir de `topicos` e começando em `0`. Evidência com `evidence_id` vazio não entra em gaveta nenhuma. Com a lista de evidências vazia, cada tópico sai com `0`; com a lista de tópicos vazia, sai `{}`.

### Erros comuns e limites

- Usar `<` no lugar de `<=`: o card que vence hoje fica fora.
- Esquecer a lista vazia, ou achar que o código dentro do laço roda quando a lista está vazia.
- Comparar datas fora do formato ISO (`"9/10/2026"` não serve).
- Inverter a ordem da guarda: a comparação impossível (`None <= "texto"` dá `TypeError`; `fila[0]` com a fila vazia dá `IndexError`) acontece antes da verificação.
- Usar **um contador para todos** quando o problema pede uma gaveta por item, ou escrever as chaves à mão em vez de criá-las a partir da entrada.
- Escrever o `assert` com o valor que o código devolveu, em vez do valor calculado à mão.
- Inventar um esperado fora do contrato da saída e ajustar o código até o teste passar.

### Checagens de entendimento

Perguntas curtas para reler antes da próxima sessão. Não contam como evidência.

1. Num `assert obtido == esperado`, de onde deve vir o `esperado`?
2. Por que a verificação de `None` precisa vir **antes** da comparação de datas num `or`?
3. Quantas vezes executa o corpo de `for x in []:`?

### Ponte para o projeto

Cada problema desta lição é uma pergunta que o app `segundo-cerebro` vai responder sobre o estudo fictício: quantos cards estão vencidos, quantas evidências cada tópico tem e quais pontos fracos estão ativos. O app lê arquivos JSON do estudo, e um erro de regra ali mostraria um painel errado ao aluno. Por isso cada função nasce com a tabela de exemplos e os `assert`.

## Plano de prática

### Objetivo observável

Antes de escrever código:

1. definir entrada, regra e saída;
2. montar de 3 a 5 exemplos com a saída esperada calculada à mão, incluindo casos-limite;
3. escrever um plano em português, dividido em subproblemas.

Depois, implementar cada subproblema como função e verificá-la com `assert`, usando o valor esperado que o próprio aluno escolheu. Também prever com uma tabela de rastreio o que faz um código com laço e condicional.

### Âncora no projeto

App `segundo-cerebro` (o app da formação). Esta lição **cria o repositório** e responde perguntas sobre o **estudo fictício** gerado com `scripts/init_study.py` dentro dele. O estudo real só é lido localmente e nunca entra no repositório.

Perguntas candidatas, uma por problema:

- Quantos cards estão vencidos numa data?
- Quantas evidências cada tópico tem?
- Quais pontos fracos estão ativos?

### Pré-requisitos

- `lesson_02-arquivos-erros`: concluída.
- O diagnóstico `diagnostic_2026-10-06-logica-01` (`partial`) posicionou a entrada. Laço, acumulador e `if` servem de base. Os focos são:
  - exemplos esperados **em números**;
  - `assert` explícito;
  - tabela de rastreio montada pelo aluno;
  - dicionário com chave nova.

### Fontes verificadas

- Python Documentation, [4. More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (`source_python-controlflow`): `if`/`elif`, `for` e funções.
- Python Documentation, [5. Data Structures](https://docs.python.org/3/tutorial/datastructures.html) (`source_python-datastructures`): listas, dicionários e a comparação **lexicográfica** de sequências (seção 5.8). Comparar texto também segue essa regra.

### Opções de andaime (usar só se precisar)

1. Reformular o problema com um card só.
2. Recuperar o pré-requisito: o percurso de uma lista de dicionários, já usado em `ordens.json`.
3. Pergunta direcional sobre o caso-limite que faltou.
4. Pista parcial: qual comparação decide "vencido".
5. Esqueleto incompleto da função (tem teto de 20).

### Variações de tarefa independente

- Contar os cards vencidos por **status** (`new`, `learning`, `review`).
- Listar os `card_id` vencidos, em vez de só contar.
- Transferência: Python Lab 006/007, ou uma tarefa do estágio sem dados da empresa.

### Erros esperados

- Usar `<` no lugar de `<=`: o card que vence hoje fica fora.
- Esquecer a lista vazia.
- Comparar datas em outro formato.
- Escrever o `assert` com o valor que o código devolveu, em vez do valor calculado à mão.

### Transferência para o 80: classificar ordens de serviço

Adaptada da missão 006 do Python Lab em 2026-10-20. No Lab, a missão só abre depois das anteriores, e o Lab é só referência: nada foi alterado nele.
- **Contexto novo:** ordens de serviço de manutenção, no repositório real `formacao-python` (`E:\Lucas\Documents\formação_python`), que já trata ordens desde o módulo 02. Não é o app nem são os dados de cards.
- **Onde fazer:** criar `src/modulo-03/classificar_ordens.py` no `formacao-python`. O aluno cria o arquivo e faz o commit.
- **Ajuste em relação ao Lab:** a missão original rejeita a lista vazia com `raise ValueError`. Lançar exceções ainda não foi ensinado nesta formação (regra 1), então a guarda devolve uma categoria própria, `"sem_itens"`. O núcleo continua o mesmo: guarda antes do acesso e ordem das condições.
- **Não abrir** o `reference_solution.py`, o `hints.json` nem os testes da missão 006 antes de terminar.

**Enunciado, só ele:**

> Uma central de manutenção recebe ordens de serviço e precisa classificá-las antes de encaminhar. Implemente `classificar_ordem(ordem)`.
>
> **Entrada:** um dicionário com:
> - `tipo`: `"falha"`, `"preventiva"` ou outro texto;
> - `prioridade`: `"urgente"` ou outro texto;
> - `itens`: uma lista de dicionários. Cada item pode ter `bloqueado`, com `True` ou `False`.
>
> Exemplo: `{"tipo": "falha", "prioridade": "urgente", "itens": [{"bloqueado": False}]}`
>
> **Saída:** um texto, uma categoria entre:
> - `"sem_itens"`, se a ordem não tem a chave `itens` ou se a lista está vazia;
> - `"bloqueada"`, se o primeiro item está bloqueado;
> - `"emergencia"`, se o tipo é `falha` e a prioridade é `urgente`;
> - `"corretiva"`, se o tipo é `falha`;
> - `"preventiva"`, se o tipo é `preventiva`;
> - `"administrativa"`, nos demais casos.
>
> Uma ordem pode se encaixar em mais de uma regra ao mesmo tempo. Decida a ordem das verificações e justifique na decomposição.

**Entregue, nesta ordem:**
1. decomposição (entrada, regra na ordem das verificações, saída, de 3 a 5 exemplos com o esperado à mão, incluindo casos-limite, e plano);
2. código com um `assert` por exemplo, com a mensagem mostrando o esperado e o obtido;
3. previsão antes de rodar;
4. tabela de rastreio de um exemplo, conferida com `print`.

### Critérios de evidência

- `application` (autônoma): o plano escrito antes do código em pelo menos 3 problemas; as funções testadas com valor esperado escolhido pelo aluno.
- `feynman` (autônoma): explicar por que decompor e escrever o esperado antes de rodar evita o erro de "parece certo".
- `transfer`: decompor sozinho um problema de outro contexto.
- Saídas dos pontos fracos: ver `programming_plan.weak_point_exits` no `state.json`.

### Atualização de estado

Ao fechar cada sessão:

- registrar o checkpoint e as evidências autônomas reais;
- registrar o hash SHA-256 dos arquivos do aluno enquanto não houver commit.

A lição só passa a `completed` com domínio 80 em `topic_logica-algoritmos` e com os três critérios de entrega cumpridos.
## Progresso

Checkpoints das sessões, do mais recente para o mais antigo. Evidências e domínio valem só pelo `state.json`.

### Onde paramos (2026-10-22): transferência parcial, sessão interrompida e retomável

`session_2026-10-22-lesson15-transferencia-01`, das 16:36 às 18:44, interrompida a pedido do aluno ("Amanhã eu corrijo").

- **Cards:** `tempos-04` ✅, `git-remote-familia-01` ✅, `dictreader-fieldnames-01` ❌ (não lembrado; volta em 23/10), `dictreader-restval-01` ✅ e `git-log-oneline-01` ✅.
  - O `cond-01`, que vencia hoje, ficou **para depois** da transferência, para não dar pista sobre a ordem das verificações.
- **Pré-requisito ensinado** (regras 1 e 7): o operador `in` / `not in` em dicionário, que só olha as **chaves**. Dois exemplos executados (estoque e perfil com `KeyError`). Na checagem de entendimento, que não é evidência, acertou 3 de 3.
- **Duas dúvidas sobre o enunciado**, respondidas sem falar da ordem das regras: a saída é **uma** palavra, entregue com `return`; a entrada é **uma** ordem, e a lista fica dentro dela, em `itens`.
- **Transferência "classificar ordens de serviço"**, em modo avaliação (`src/modulo-03/classificar_ordens.py` no `formacao-python`, `c2f10399…`):
  - ✅ **A ordem das verificações saiu certa e sem pista:**
    1. a guarda `"itens" not in ordem or ...`, antes do acesso;
    2. bloqueado antes do tipo;
    3. falha com urgente antes de falha.
  - ❌ `if __name__ == "__name__"`: os 5 `assert` nunca rodaram, e o "Todos os testes passaram" sai sempre. Com `__main__`, o caso 3 falha.
  - ❌ O esperado do caso 3 (`"preventiva"`, com o item bloqueado) contradiz a ordem decidida pelo próprio aluno.
  - ❌ A lista vazia `[]` foi comparada com `""` e escapa da guarda (`StopIteration`). Nenhum `assert` cobre `sem_itens`.
  - ❌ Os textos estão fora do contrato (`"bloqueado"`, `"adiministrativa"`).
  - ❌ Faltaram a previsão e a tabela à mão.
  - A conferência genérica foi pedida uma vez: "Acredito que esteja completa".
  - Registrado em `evidence_logica-transferencia-ordens-01`: **transferência autônoma parcial**.
- **Domínio (regra 9):** continua em **60**.
  - ✅ Feynman autônomo (13/10).
  - ✅ Aplicação padrão (20/10).
  - ⏳ Transferência autônoma correta.

**Checklist da v2**, prática guiada que não conta para o 80:
1. corrigir a condição do `__main__` e mostrar a mensagem final só quando os testes passarem;
2. refazer o esperado do caso 3 pela própria ordem;
3. fazer a guarda pegar a lista vazia;
4. escrever os `assert` de "sem chave" e de "lista vazia";
5. usar os textos do contrato;
6. escrever a previsão;
7. fazer a tabela à mão de um caso.

**Próximo:**
1. retomar esta sessão com uns 5 cards, incluindo `cond-01` e `fieldnames-01`;
2. fazer a v2 guiada;
3. depois, fazer uma **tarefa diferente com ordens de serviço**, só com o enunciado. Pela skill `e87e2d7`, alinhada às 19:04 de 22/10, ela conta para o 80, sem precisar de outro contexto.

### Onde paramos (2026-10-20): problema 4 autônomo, lógica em 60, sessão concluída

`session_2026-10-20-lesson15-variacao-01`, das 18:00 às 18:43.

- **Cards:** `tempos-05`, `tempos-06`, `tempos-07`, `tempos-08` e `dictreader-chaves-01`, todos ✅.
- **Problema 4: quantos cards vencidos há em cada status?** Modo avaliação, só com o enunciado (`exe_03.py`, `73bd869b…`).
  - **Decomposição antes do código**, com as decisões do aluno: "sem data conta", "vence hoje entra", "o futuro fica de fora".
  - **5 exemplos com o esperado à mão:** caso normal, vence hoje, futuro, `None` e lista vazia.
  - **Função:** gavetas fixas para os três status, `None` testado antes do `<=` e proteção contra status desconhecido. Os 5 `assert` têm mensagem.
  - **Previsão** "os cinco passam" ✅, e a tabela de rastreio do caso 1 estava certa.
  - O aluno declarou que fez sozinho. A conferência genérica foi pedida uma vez, e ele considerou a entrega completa.
  - Registrado em `evidence_logica-problema4-aplicacao-01`: **aplicação padrão, autônoma e correta**.
- **A tabela foi conferida por execução,** com um `print` dentro do laço, e bateu linha por linha (`evidence_logica-rastreio-execucao-01`, de apoio).
- **Domínio (regra 9):** `topic_logica-algoritmos` subiu de **40 para 60**.
  - ✅ Feynman autônomo (13/10).
  - ✅ Aplicação padrão autônoma e correta (20/10).
  - ⏳ Para o 80, falta uma aplicação autônoma em **contexto novo**.
- **Ponto fraco resolvido:** `weak_python-test-literal-lista`, com duas aplicações autônomas corretas em sessões diferentes (16/10 e 20/10).

**O que falta para concluir a lição:**
- ✅ 3 problemas com plano antes do código (são 4);
- ✅ tabela de rastreio conferida por execução;
- ✅ funções testadas com esperado à mão;
- ✅ domínio 60;
- ⏳ domínio 80: a transferência.

**Próximo:**
1. abrir com uns 5 cards;
2. fazer a **transferência "classificar ordens de serviço"** (seção do Plano de prática; adaptada da missão 006 em 20/10, porque no Lab ela só abre depois das anteriores) só com o enunciado, no `formacao-python`: decomposição, `assert` próprios, previsão e rastreio.

Se sair correta, a lição fecha e entra a avaliação do pedido de unificação.

### Onde paramos (2026-10-19): problema 3 fechado no código, sessão concluída

A sessão `session_2026-10-17-lesson15-problema3-01` foi retomada e concluída em 19/10, das 17:16 às 18:45.

- **Cards:** `git-remote-v-01` ✅ e `git-push-u-01` ✅. Ficaram parciais:
  - `cond-01`: "juntas: apenas um `if`" (o certo é um `if` para cada situação);
  - `git-remote-familia-01`: o `add` saiu sem o nome do remoto;
  - `tempos-04`: a resposta ficou vaga.
- **`exe_02.py` v1, feito sozinho** (`evidence_logica-problema3-codigo-01`): autônomo e **parcial**.
  - O filtro por status e a saída `{id: tópico}` estão certos, e os 5 `assert` passam com esperados calculados à mão.
  - Faltaram as exclusões de "sem tópico" e "sem id", que estavam na regra citada na tarefa.
- **Previsão correta, autônoma** (`evidence_logica-previsao-return-laco-01`): um `return {}` dentro do laço encerra a função no primeiro item inválido. Em 16/10 essa leitura tinha saído errada.
- **Versão final, guiada e correta** (`evidence_logica-problema3-codigo-02`, `4b2587c8…`):
  - um laço só, com a condição `item["status"] == status and item["weak_point_id"] != "" and item["topic_id"] != ""`;
  - status pedido vazio dá `{}`;
  - item inválido é só pulado, e as listas mistas funcionam.
- **Conceitos de hoje:**
  - **Um `if` por situação independente;** com `and`, uma situação depende da outra.
  - **`return` dentro do laço** encerra a função inteira. Para pular um item, o certo é não deixá-lo entrar, e não sair da função.
  - **Testes com um item por lista** não pegam defeitos que só aparecem em listas mistas.
- **Domínio (regra 9):** `topic_logica-algoritmos` segue em **40**.
  - ✅ A metade Feynman do 60 foi cumprida em 13/10.
  - ⏳ Falta a aplicação autônoma correta. Candidata: uma **variação nova só com o enunciado**.
- O aluno contestou o rigor do critério 40 → 60. Ficou registrado no `session-log.md`.

**O que falta para concluir a lição:**
- ✅ 3 problemas com plano antes do código;
- ⏳ uma tabela de rastreio feita pelo aluno;
- ⏳ o domínio 60, que depende de uma aplicação autônoma correta;
- ⏳ o domínio 80, que depende de uma aplicação em contexto novo.

### Onde paramos (2026-10-17): decomposição do problema 3 fechada, sessão interrompida e retomável

`session_2026-10-17-lesson15-problema3-01`, das 18:34 às 20:00.

- **Cards:** `tempos-03` ✅. Não deram certo: `cond-01` (resposta invertida) e os três de Git, que o aluno não lembrou. Esses quatro voltam em 18/10.
- **Repositório criado e publicado pelo aluno:** [`14lucas-mendes/second-brain-agent`](https://github.com/14lucas-mendes/second-brain-agent), público, com a branch `main` ligada a `origin/main`. O primeiro commit, `ac8833d`, tem só os exercícios com dados fictícios (`evidence_git-repo-second-brain-01`). Ele não mandou o plano antes de executar e ainda falta o `.gitignore`.
- **Problema 3, decomposição fechada** (guiada, `evidence_logica-decomposicao-problema3-01`):
  - **Entrada:** a lista de pontos fracos e o status pedido (`"active"` ou `"resolved"`). Usar o status como parâmetro foi decisão do aluno.
  - **Regra:** entra no resultado quem tem o status pedido. Ponto fraco sem status, sem tópico ou sem id fica de fora.
  - **Saída:** `{weak_point_id: topic_id}`. Um id é único, então nenhum ponto fraco apaga outro.
  - **Caminho até a saída:**
    1. `{tópico: status}`: dois pontos fracos do mesmo tópico, e um apaga o outro;
    2. contagem por tópico: virou o problema 2;
    3. `{"weak_point_id": ...}` repetido: o `print` mostrou só o último;
    4. `{id: tópico}` ✅.
  - **Esperados finais:** os dois ativos do mesmo tópico entram juntos; o resolvido entra só quando o pedido é `"resolved"`; status vazio, status pedido vazio e lista vazia dão `{}`.
- **Conceitos de hoje:**
  - **Chave repetida num dicionário:** a última substitui a anterior, sem aviso.
  - **Filtrar é peneirar:** o que não passa fica de fora. Não entra com uma etiqueta como `"sem status ativo"`, `None` ou `0`.
  - **"Quais" × "quantos":** "quais" identifica cada item; "quantos" só conta.
- **Domínio (regra 9):** `topic_logica-algoritmos` segue em **40**.
  - ✅ A metade Feynman do 60 foi cumprida em 13/10.
  - ⏳ Falta a aplicação autônoma. O código do problema 3 pode cumprir essa parte se o aluno fizer sozinho, a partir da decomposição dele.

**Próximo:**
1. abrir com uns 5 cards;
2. escrever o código do problema 3, com `assert` em listas literais e mensagem, prevendo o resultado antes de rodar;
3. montar uma tabela de rastreio própria, conferida rodando.

### Onde paramos (2026-10-16): problema 2 fechado, sessão concluída

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

#### O que falta para concluir a lição

| Requisito | Situação |
|---|---|
| Plano escrito antes do código em pelo menos 3 problemas | 2 de 3 (problemas 1 e 2). Falta o **problema 3**: pontos fracos ativos. |
| Tabelas de rastreio conferidas por execução | Falta uma tabela **montada pelo aluno**. A de 16/10 foi feita pelo tutor. |
| Funções testadas com valor esperado à mão | Cumprido nos problemas 1 e 2. |
| Domínio 60 em `topic_logica-algoritmos` | Feynman ✅; falta uma aplicação autônoma correta. |
| Domínio 80 | Falta uma aplicação autônoma em contexto novo (Python Lab 006/007 ou tarefa do estágio sem dados da empresa). |
| Repositório `segundo-cerebro` (roteiro da formação) | A pasta existe, mas ainda não é repositório Git. |

**Próximo:** criar o repositório Git `segundo-cerebro` (o aluno executa os comandos). Depois, o problema 3 só com o enunciado: decomposição, casos-limite, previsão antes de rodar, `assert` e uma tabela de rastreio feita pelo aluno.

### Onde paramos (2026-10-15), sessão interrompida e retomável

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

### Onde paramos (2026-10-13), sessão interrompida e retomável

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

### Onde paramos (2026-10-12)

**Problema 1: fechado.** A versão final (`f4898339…`) usa um `if` só, `card["due_at"] == None or card["due_at"] <= hoje`. O `or` funciona aqui porque as duas condições levam à mesma ação. O `None` vem primeiro, como **guarda**, e 6 `assert` passam com os esperados da tabela.

**Curto-circuito** (revisto em 12/10):
- `or` para quando a primeira é **True**;
- `and` para quando a primeira é **False**.

Com a ordem invertida, a comparação impossível (`None <= "texto"` → `TypeError`; `fila[0]` com a fila vazia → `IndexError`) acontece antes da guarda.

**Próximo:**
1. uma pergunta rápida de `and`/`or`;
2. o Feynman "o esperado vem da regra", feito sozinho;
3. o **problema 2** (evidências por tópico), decomposto sozinho antes do código.

### Onde paramos (2026-10-11)

Feito: saída `int`, lista vazia → `0`, `>=` no lugar de `>`, verificação do "sem data" **antes** da comparação, um `assert` por linha da tabela com a data fixa `"2026-10-09"`.

Falta:

1. "sem data" e "venceu" se excluem → `if`/`elif` (hoje o card com `""` conta 2);
2. o teste do "sem data" usar `None` (o `null` do JSON), não `""`;
3. todos os `assert` passando com os esperados **da tabela**, sem rodar o código para descobrir o esperado.

**Conceito reforçado em 11/10: de onde vem o esperado.** O esperado sai da **regra**; o obtido sai do **código**. Se o esperado for copiado da execução, o teste confere o código com ele mesmo — como perguntar ao caixa qual é o troco certo e conferir o troco dele com a resposta dele.

Pré-requisito ensinado em 11/10: `null` no JSON vira `None` no Python; `None` ("sem valor") ≠ `""` (texto vazio). Texto vazio vem antes de qualquer texto: `"2026-10-09" >= ""` é `True`.

### Onde paramos (2026-10-09)

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
