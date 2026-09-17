# Brief de imagem didática — modelo de dois tempos

Lição: `lesson_03-testes-git` · Origem: `source_python-errors-exceptions`, `source_python-traceback`

## Objetivo pedagógico

Fazer o estudante ver que a análise acontece **antes** da execução e que a ausência do cabeçalho `Traceback` é o sinal observável disso.

## Conteúdo obrigatório na imagem

1. Dois estágios em sequência: **1 — ANÁLISE** (confere a forma) e **2 — EXECUÇÃO** (confere os valores).
2. Uma seta da análise para a execução, rotulada como "só passa se a forma estiver válida".
3. Uma saída lateral da análise para `SyntaxError`, com a nota "nada executa · sem Traceback".
4. Duas saídas da execução: `NameError` (o nome não existe) e `TypeError` (o valor não serve para a operação), ambas com a nota "com Traceback".
5. Uma entrada adicional para `TypeError`: "função terminou sem `return` → devolveu `None`".

## Restrições

- Rótulos em português, curtos.
- Não usar cor como único portador de significado: cada bloco carrega rótulo em texto.
- Não inventar conteúdo ausente das fontes.

## Arquivo pronto

`didactic-image.svg` — diagrama vetorial já produzido, com texto correto e editável. Preferido em relação a imagem gerada por IA, que costuma errar rótulos em português.

## Texto alternativo (alt text)

"Diagrama de dois estágios. O estágio 1 é a análise, que confere a forma do código: se a forma é inválida, sai um SyntaxError e nada executa, sem traceback. Se a forma é válida, passa para o estágio 2, a execução, que confere os valores: se o nome não existe, sai NameError; se o valor não serve para a operação, sai TypeError, ambos com traceback. Uma seta extra mostra que uma função que termina sem return devolve None, e esse None chega ao chamador e provoca TypeError."
