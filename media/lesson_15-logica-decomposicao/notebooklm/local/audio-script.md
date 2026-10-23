# Roteiro do áudio: revisão da lesson_15

Este é o guia do **Resumo em áudio** do NotebookLM (formato "Análise detalhada", em português do Brasil, de 8 a 12 min) e também o **texto de apoio**, para quem preferir ler. A gravação só pode usar as fontes do `source-pack.md`. É material do tutor: **não é evidência**.

## Instrução para colar em "Personalizar" no NotebookLM

> Fale em português do Brasil, com linguagem simples, para um iniciante em Python que acabou de concluir esta lição. Siga as seis etapas do método na ordem: regra e saída, exemplos à mão, ordem das regras, código, assert e `__main__`, casos-limite. Em cada etapa, explique o conceito com uma analogia do dia a dia. Depois conte a dificuldade real que aparece na fonte `study_lesson15-percurso`, com a data, e como ela foi resolvida. Não invente erros, datas nem números que não estejam nas fontes. Termine com três perguntas para o ouvinte responder em voz alta, sem dar as respostas.

## Roteiro, por blocos

1. **Abertura (30 s).** A lição ensinou um caminho: regra → exemplos com o esperado à mão → plano → código → `assert` → rastreio. Ela foi concluída em 23/10/2026, com lógica em 80.
2. **Regra e saída.** O contrato da saída é uma promessa de formato. *Dificuldade (16/10):* no caso vazio, o aluno inventou `{'lista': 0}` e ajustou o código até o teste passar. *Solução:* o esperado sai do contrato.
3. **Exemplos à mão.** O esperado vem da regra; o obtido vem do código. *Analogia:* conferir o troco do caixa com a conta feita por você, e não com a resposta do próprio caixa. *Dificuldade (09–11/10):* o esperado foi tirado da execução, e o `''` no lugar de `None` escondia o caso sem data.
4. **Ordem das regras.** A guarda vem antes do acesso, e a regra específica antes da geral. O `or` para no primeiro `True`; o `and` para no primeiro `False`.
   - *Dificuldade (12/10):* com `<=` antes de `== None`, o resultado foi `TypeError`.
   - *Dificuldade (22/10):* o esperado `"preventiva"` foi escrito para uma ordem com o item bloqueado.
   - *Solução:* uma ordem travada não vai para setor nenhum.
5. **Código.** Uma gaveta por chave: `d[k] = 0` cria e `d[k] += 1` soma. Um laço sobre uma lista vazia dá zero voltas. O `return` encerra a função. *Dificuldades:* um contador só para todos os tópicos (13/10) e um `return {}` dentro do laço (19/10).
6. **`assert` e `__main__`.** O teste só prova algo se rodar.
   - *Dificuldade (22/10):* `if __name__ == "__name__"`, com uma mensagem "Todos os testes passaram" que aparecia sempre.
   - *Analogia:* um detector de fumaça com o fio solto.
   - *Solução (23/10):* `"__main__"`, com a mensagem final dentro do bloco.
7. **Casos-limite.** Lista vazia, chave ausente, sem data, vence hoje. *Dificuldade (22/10):* `== ""` deixava a lista `[]` passar. *Solução:* `== []` e um `assert` para cada caso-limite.
8. **Fechamento.** Em 23/10, a tarefa "filas do fim de turno" saiu autônoma e correta. Ela pôs o status antes das peças e o `"pecas" not in ordem` antes do acesso, e os 5 `assert` passaram.
9. **Perguntas para o ouvinte, sem resposta no áudio:**
   1. Num `assert`, de onde deve vir o esperado?
   2. Por que `"pecas" not in ordem` vem antes de `ordem["pecas"]`?
   3. O que a frase "Todos os testes passaram" prova quando está fora do bloco `__main__`?

## Depois de ouvir

Responda às três perguntas **sem consultar nada**. Depois confira no mapa `revisao-lesson15.excalidraw`: a pergunta 1 está na coluna 2, a 2 na coluna 3 e a 3 na coluna 5. Se errar alguma, avise o tutor; essa resposta vira uma tentativa de recuperação na próxima sessão.
