# Study Guide — lesson_02-arquivos-erros

Guia de revisão com perguntas de recuperação e citação de fonte. Use de memória primeiro; só depois confira a fonte. **Nada deste pacote é evidência de aprendizagem** — o que conta é a sua explicação ou aplicação autônoma depois.

## Perguntas de recuperação

1. Qual é a diferença de **formato de retorno** entre `csv.reader` e `csv.DictReader`, e o que muda no seu código por causa disso?
2. Onde foi parar a primeira linha do arquivo em cada um dos dois leitores?
3. Você passa `fieldnames` explicitamente. O que passa a acontecer com a primeira linha?
4. De onde vem o `None` numa chave quando uma linha tem menos células que o cabeçalho? E o que significa uma chave chamada `None`?
5. Qual é o tipo dos valores que saem do leitor, e o que você precisa fazer antes de somar `horas_paradas`?
6. Por que `next(leitor)` pode quebrar num arquivo vazio, e qual é a correção mínima?
7. Qual a diferença prática entre `result[1:]` e `result.pop(0)`, olhando o que acontece com a lista original?
8. Um arquivo tem `print(ler_clientes("dados.csv"))` na última linha. O que você vê ao escrever `from exercicios_03 import ler_clientes` em outro arquivo, e por quê?
9. Num arquivo só com cabeçalho, o que `fieldnames` devolve? E num arquivo totalmente vazio?

**Fontes para conferir:** `source_python-csv-module`, `source_python-builtins`, `source_python-datastructures`, `source_python-modules` (ver `source-pack.md`).

## Os três desfechos que a tarefa precisa provar

| Situação | O que precisa acontecer |
|---|---|
| Arquivo com várias linhas | devolve **todos** os registros, sem o cabeçalho entre eles |
| Arquivo ausente | o erro é distinguível de "sem registros" |
| Arquivo só com cabeçalho | zero registros — e distinguível de arquivo vazio |
| Importado por outro arquivo | nada é impresso, nada é lido: só a função fica disponível |

## Tarefa de transferência (a que você já disse que vai fazer)

Implemente a leitura **dos dois jeitos** — uma versão com o leitor posicional e uma com o leitor por nome — e responda:

1. O que cada versão devolve, exatamente, e em que a segunda é mais segura contra mudança de ordem das colunas?
2. O que você teve de fazer à mão numa versão e a outra resolveu sozinha?
3. Se o arquivo ganhasse uma coluna nova no meio, o que quebraria em cada versão?
4. Qual você escolheria para uma automação que lê arquivo de terceiro, e por quê?

Esse par de implementações com justificativa é o material que fecha a decisão de projeto — e é a resposta que eu quero ver na retomada.

## Erros já observados nesta formação (não repita sem perceber)

- Devolver o cabeçalho junto com os dados e chamar isso de "leitura completa" (sessão de 2026-09-17).
- Devolver `None` por falta de `return`, com a mensagem perdida num `print` (sessão de 2026-09-17).
- Descrever o que a função devolve em vez de escrever o valor literal e conferir com a saída.
