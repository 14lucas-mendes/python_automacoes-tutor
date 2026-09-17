# Lição `lesson_03-testes-git`

**Status:** concluída em 2026-09-12. Próxima lição: `lesson_04-descoberta-processo`.

## Objetivo observável

Diagnosticar falhas passo a passo, formular hipóteses e corrigir programas Python pequenos.

## Pré-requisitos

`lesson_01-python-core` — concluída. Esta lição reusa funções, listas, `return` e tipos.

## Fontes verificadas

- Python Documentation — [8. Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html), acesso em 2026-09-12. Origem da regra usada aqui: a última linha da mensagem nomeia o **tipo** da exceção e o restante traz o detalhe; o bloco anterior é o *stack traceback* com arquivo e linha.
- Python Documentation — [`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html), acesso em 2026-09-12. Referência para inspecionar o traceback de forma programática.

## Ideia central

*(Material de estudo. A tentativa autônoma desta lição foi feita em 2026-09-12 — este material pode ser consultado livremente daqui em diante.)*

Uma falha entrega três informações separáveis: **onde** (arquivo e linha), **o que** (tipo da exceção) e **detalhe** (a mensagem). Diagnosticar não é adivinhar a correção — é converter o sintoma observado em uma hipótese verificável e só então alterar o código.

Duas falhas parecidas têm causas diferentes:

- `NameError` — o nome **não existe** no escopo em que foi usado.
- `TypeError` — o nome **existe**, mas o valor tem tipo incompatível com a operação. Exemplo clássico: uma função termina sem `return`, devolve `None` implicitamente, e o chamador soma esse `None` a um número.

O erro de leitura mais comum é nomear a operação pelo que ela parece em vez do que ela é naquele ponto do código. `None + 1` é uma **soma numérica** entre tipos incompatíveis — não uma concatenação de strings.

## Exemplo concreto

Um programa de manutenção guarda o tempo de parada de cada falha e calcula a média. Se a função auxiliar esquecer o `return`, o chamador recebe `None`; a divisão ou a soma quebra com `TypeError`, e a linha apontada não é a linha com o defeito de origem. Ler a cadeia do traceback (de cima para baixo) mostra a chamada que entrou na função defeituosa.

## Prática guiada

Depois da tentativa autônoma, revisar apenas o que impediu o diagnóstico: distinguir erro de sintaxe de exceção, localizar a origem pela cadeia de chamadas, e separar "o nome não existe" de "o valor não serve para a operação".

## Tarefa autônoma

Dado um programa pequeno e a saída de erro observada, sem editar o código, responder:

1. **Sintoma** — qual é a última linha da mensagem e em qual linha do arquivo ela ocorre.
2. **Hipótese** — qual é a causa provável, e por que essa causa produz exatamente esse tipo de exceção.
3. **Verificação** — o que você faria para confirmar a hipótese antes de mudar o código.

Depois, aplicar a correção mínima e **executar** o programa para confirmar o resultado.

## Erros esperados

- Ler o `NameError` como se a variável existisse, ou o `TypeError` como se fosse apenas um nome errado.
- Corrigir uma linha antes de localizar a origem real do defeito.
- Chamar de concatenação uma operação numérica (ou o inverso).
- Declarar a correção como pronta sem executar o programa.

## Critérios de evidência

- Explicação autônoma da diferença entre `NameError` e `TypeError` causado por `None`.
- Aplicação autônoma do diagnóstico em uma falha nova, com hipótese registrada antes da correção.
- Transferência para um contexto diferente do já praticado.
- Correção verificada por execução real, com a saída registrada.

Classificação **correta** quando ideia central, contexto e justificativa forem materialmente adequados; **parcial** só se faltar um elemento que impeça cumprir o objetivo com segurança.

Uma solução explicada pelo tutor permanece material de estudo e não conta como evidência autônoma.

## Atualização de estado

Ao fechar a sessão, registrar a tentativa, o resultado, a retenção percebida, eventuais pontos fracos e o próximo foco em `.ai-tutor/state.json`; validar o estudo antes de concluir.

## Resultado

- Sessões: `session_2026-09-10-debugging-01` (encerrada no limite de tempo) e `session_2026-09-12-debugging-02`.
- Evidências autônomas: `evidence_debugging-diagnosis-15` (transferência, correta), `-16` (parcial), `-17` (correta), `-18` (aplicação verificada por execução), `-19` (Feynman do alvo da lição).
- Correção verificada: `return media` em `tempo_medio` + f-string em `relatorio`; execução com `Tempo medio: 60.0 min` e `exited with code=0`.
- Lacuna conceitual aberta nesta lição: `weak_error-model-tempo-deteccao` — o modelo de dois tempos do Python (por que `SyntaxError` não traz traceback) nunca havia sido ensinado e passou a ser requisito de aula explicativa.
- Fonte oficial usada: [Python Tutorial, cap. 8 — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html).
- Programa com o defeito (material): `projects/diagnostico-erros/manutencao_relatorio.py`.
