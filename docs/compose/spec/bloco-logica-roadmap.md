# Bloco de lógica, decomposição e estruturas de dados — proposta

Status: **aprovada pelo aluno em 2026-10-06** e gravada no estado canônico (`revision` 184). `study-config.json` passou a ter 16 ciclos, até 01/08/2027.

## Por que

Pedido do aluno em 2026-10-06: ele sente muita dificuldade em lógica de programação, principalmente em:

- juntar listas, dicionários, condicionais e laços num mesmo programa;
- decompor um problema antes de começar;
- saber o que esperar como entrada e como saída;
- debugar.

A dificuldade apareceu com força nas missões do Python Lab. Ele começou um estágio em análise e desenvolvimento de sistemas (departamento GFI, stack ainda indefinida) e quer chegar lá escrevendo código sozinho, com pensamento crítico. Aceita estender a formação além de maio de 2027.

O que os registros confirmam:

- `topic_python-fundamentos` está em 80 com evidência real, mas de **peças isoladas**: filtrar uma lista, função curta, CLI simples. **Compor** essas peças diante de um problema novo é outra capacidade, que ainda não foi ensinada nem medida. É lacuna do material.
- 4 dos 6 pontos fracos ativos são conceituais: `weak_condicionais-ordem-guarda`, `weak_verificacao-valor-esperado`, `weak_caminho-relativo-pasta-trabalho` e `weak_error-model-tempo-deteccao`.
- `cond-05` repetiu o mesmo raciocínio três vezes (01/10, 02/10 e 06/10). Nas tarefas longas, os trechos que exigiam decompor e verificar foram os que precisaram de ajuda.

## Termo que vale separar

O aluno usou "dividir para conquistar" no sentido de **decompor um problema**: quebrar em partes menores, resolver cada uma e juntar. É isso que o bloco ensina primeiro.

Nos livros, "dividir para conquistar" é também o nome de uma **técnica de algoritmo** específica. Ela aparece no capítulo do quicksort de *Entendendo Algoritmos*: o problema é quebrado em cópias menores dele mesmo, normalmente com recursão. As duas ideias são parentes, mas a segunda vem depois, na lição 17.

## O que muda

1. **Novo tópico** `topic_logica-algoritmos` (*Lógica, decomposição, algoritmos e estruturas de dados*), com domínio 0. Não herda o 80 de `topic_python-fundamentos` e não rebaixa esse 80, porque mede outra capacidade.
2. **Três lições novas**, uma por ciclo, entre a `lesson_02` (concluída) e a `lesson_14`.
3. **`lesson_14` passa a depender da `lesson_17`**, no lugar da `lesson_02`. O resto do roteiro do Segundo Cérebro continua igual, só desloca três ciclos.
4. **Calendário:** de 13 para **16 ciclos**. O fim de referência passa de 30/05/2027 para **01/08/2027**. O calendário continua informativo: quem decide o avanço é a evidência.
5. **Lógica em espiral.** Depois do bloco, toda sexta-feira (já reservada para lógica e debugging) traz um exercício curto de decomposição ou estruturas de dados, até o fim da formação.
6. **Ponto de partida por diagnóstico.** Antes da lição 15, um `/diagnostic` curto (cerca de 30 min). Ele estima onde começar em cada parte do bloco, sem gerar evidência nem mexer em domínio.

## Método de aula do bloco

O protocolo adaptativo continua valendo. Dentro dele, o bloco usa:

- **Prever → rodar → investigar → modificar → criar.** Primeiro o aluno prevê o que um código faz, depois executa, investiga o que surpreendeu, modifica e, só no fim, cria do zero.
- **Tabela de rastreio à mão.** Uma linha por passo do laço, uma coluna por variável. É a ferramenta para "ver o programa rodando por dentro", a lacuna que apareceu no `else` de 06/10.
- **Exemplos resolvidos que vão sumindo.** Um exemplo completo, depois um com lacunas e depois só o enunciado, sempre com pelo menos dois contextos por conceito (regra 4).
- **Entrada e saída antes do código.** Todo exercício começa com o aluno escrevendo exemplos de entrada e da saída esperada, calculada à mão, incluindo os casos-limite. Isso ataca diretamente `weak_verificacao-valor-esperado`.
- **Muitos exercícios curtos e variados**, em vez de poucos e longos.

## Lições

### `lesson_15-logica-decomposicao`: decompor, planejar e rastrear

- **Objetivo observável:** diante de um problema novo, escrever, antes do código:
  - entrada, regra e saída;
  - de 3 a 5 exemplos com a saída esperada calculada à mão, incluindo casos-limite;
  - o plano em português, dividido em subproblemas.

  Depois, implementar cada subproblema como função e prever à mão, com tabela de rastreio, o que um código com laço e condicional faz.
- **Conteúdo:** os quatro passos de resolução de problemas (entender, planejar, executar, revisar), entrada → processamento → saída, casos-limite, pseudocódigo, tabela de rastreio, `if` separados × `if`/`elif`, laço com acumulador e uma função por subproblema.
- **Âncora no projeto:** uma pasta de notas de exemplo no formato do cofre (dados fictícios no repositório; o cofre real só é lido localmente). Problemas: contar notas por pasta, achar notas sem `tags`, listar notas criadas numa data.
- **Revisita:** condicionais (`weak_condicionais-ordem-guarda`) e valor esperado (`weak_verificacao-valor-esperado`), com novo formato de dado.
- **Critérios de entrega:** plano escrito antes do código em pelo menos 3 problemas; tabelas de rastreio conferidas por execução; funções testadas com valor esperado à mão.
- **Evidências exigidas:** Feynman, aplicação e transferência.
- **Prática sugerida (referência, sem sincronizar):** Python Lab 006 (classificar ordens) e 007 (erros antes e durante a execução); *Entendendo Algoritmos*, cap. 1, só a ideia de passos e de "quanto trabalho o algoritmo faz".

### `lesson_16-estruturas-dados`: listas, dicionários e os padrões de dados

- **Objetivo observável:** escolher e justificar a estrutura certa (lista, dicionário, tupla ou conjunto) para um problema e aplicar sem ajuda os padrões básicos:
  - acumular, contar e agrupar por chave;
  - filtrar, buscar, achar o maior ou o menor;
  - percorrer dados aninhados (lista de dicionários, dicionário de listas).
- **Conteúdo:** operações e custo intuitivo de cada estrutura; dicionário como tabela hash (busca rápida por chave); `in`, `get`, `items` e `setdefault`; cópia × referência; percorrer e montar estruturas aninhadas.
- **Âncora no projeto:** índice das notas de exemplo: `tag → [notas]`, `pasta → quantidade`, notas duplicadas por título, links quebrados. É o embrião do importador do Segundo Cérebro (ponte opcional que estava na `lesson_02`).
- **Revisita:** decomposição e rastreio da lição 15, com dados aninhados; CSV e JSON da `lesson_02`.
- **Critérios de entrega:** `indice.json` gerado e verificado com valor esperado; escolha de cada estrutura justificada por escrito; casos-limite (lista vazia, chave ausente, empate) tratados.
- **Evidências exigidas:** Feynman, aplicação e transferência.
- **Prática sugerida:** Python Lab 001 (consolidar falhas), 002 (limpar relatório CSV), 003 (validar inventário JSON) e 005 (relatório operacional); *Entendendo Algoritmos*, cap. 2 (arrays × listas encadeadas) e cap. 5 (tabelas hash); Groner, capítulos de arrays, pilhas, filas, conjuntos e dicionários. O livro é em JavaScript: ler o conceito e implementar em Python.

### `lesson_17-algoritmos-debugging`: algoritmos clássicos e debugging por hipótese

- **Objetivo observável:**
  - implementar e explicar busca linear × busca binária e uma ordenação simples, comparando o custo pelo número de passos;
  - reconhecer recursão e "dividir para conquistar" num exemplo pequeno;
  - diagnosticar um defeito com hipótese explícita (prever → rodar → comparar), sem tentativa e erro às cegas.
- **Conteúdo:** Big O intuitivo (contar passos); busca binária; ordenação por seleção; recursão (caso-base e caso recursivo); quicksort como exemplo de dividir para conquistar; `sorted`/`key` no dia a dia; debugging com `print` dirigido e com o depurador do editor; teste que falha antes da correção.
- **Âncora no projeto:** ordenar e buscar nas notas de exemplo (por data, por título); corrigir defeitos plantados no próprio índice da lição 16.
- **Revisita:** estruturas da lição 16 com restrição de custo; modelo de erros (`weak_error-model-tempo-deteccao`).
- **Critérios de entrega:** busca binária e ordenação implementadas e testadas com valor esperado; pelo menos dois defeitos diagnosticados com hipótese escrita antes da correção; comparação de passos explicada.
- **Evidências exigidas:** Feynman, aplicação e transferência.
- **Prática sugerida:** Python Lab 004 (recuperar script) e 008 (testes com valor esperado); *Entendendo Algoritmos*, caps. 1 a 4; Groner, capítulos de recursão, ordenação e busca.

## Calendário de referência proposto

| Ciclo | Janela | Conteúdo |
|---|---|---|
| 1 a 4 | 31/08 – 22/11/2026 | Inalterados (concluídos por evidência) |
| 5 | 23/11 – 13/12/2026 | `lesson_15` Decompor e rastrear |
| 6 | 14/12/2026 – 03/01/2027 | `lesson_16` Estruturas de dados |
| 7 | 04/01 – 24/01/2027 | `lesson_17` Algoritmos e debugging |
| 8 | 25/01 – 14/02/2027 | `lesson_14` Git profissional + `lesson_05` SQL |
| 9 a 16 | 15/02 – 01/08/2027 | `lesson_06` a `lesson_13`, na ordem atual |

O trabalho real está cerca de 6 semanas à frente do calendário. Por isso o bloco provavelmente começa em outubro, não em novembro. A data não trava nada.

## Em aberto

- **Horas semanais:** dependem da carga do estágio, ainda indefinida. Mantém-se 8 h e os dias protegidos atuais até o aluno informar a nova rotina. Sessões de 45 a 60 min continuam válidas: o protocolo é flexível.
- **Estágio como transferência:** quando a stack for conhecida, tarefas parecidas com as do estágio podem entrar como contexto de transferência. Dados da empresa nunca entram no repositório nem no tutor.
- **Python Lab:** continua só como referência (decisão de 2026-10-04). Não há missões de busca e ordenação; se o aluno criar alguma no Lab, ela pode entrar como prática sugerida da lição 17.

## O que é preservado

Sessões, evidências, domínios, pontos fracos e lições concluídas ficam como estão. `topic_python-fundamentos` continua em 80. O Segundo Cérebro continua sendo o projeto da formação, e as lições do bloco já produzem a primeira peça dele (o índice das notas).
