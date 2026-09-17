# Estudo guiado — modelo de dois tempos do Python

Lição: `lesson_03-testes-git` · Tópico: `topic_python-fundamentos`
Ponto fraco alvo: `weak_error-model-tempo-deteccao`

Material de estudo. **Não é evidência.** Depois de consumir, a evidência só nasce de uma explicação ou aplicação autônoma sua.

## Como usar

Responda cada pergunta em voz alta ou por escrito **antes** de conferir a fonte. Se travar, volte ao trecho citado em vez de adivinhar.

## Bloco 1 — os dois tempos

**P1.** O Python distingue quantos tipos de erro? Quais?
→ Fonte: `source_python-errors-exceptions`, trecho *"There are (at least) two distinguishable kinds of errors: syntax errors and exceptions."*

**P2.** Em que momento cada um é detectado?
→ Um é detectado **antes** de qualquer linha executar; o outro **durante** a execução.

**P3.** Um programa quebra e a mensagem **não** tem o cabeçalho `Traceback (most recent call last)`. O que isso prova sobre o que já rodou?
→ Fonte: `source_python-traceback`, trecho sobre `print_exception`: *"if tb is not None, it prints a header Traceback (most recent call last):"*

## Bloco 2 — ler a mensagem

**P4.** O que a **última linha** informa? E o **bloco acima** dela?
→ Fonte: `source_python-errors-exceptions`, trechos *"The last line of the error message indicates what happened"* e *"The preceding part of the error message shows the context where the exception occurred, in the form of a stack traceback."*

**P5.** A linha apontada pelo traceback é sempre a linha do defeito?
→ Pense no caso praticado hoje: onde o erro apareceu e onde estava a causa.

## Bloco 3 — os três nomes

**P6.** `NameError` significa o quê? Qual exemplo a documentação usa?
→ Fonte: `source_python-errors-exceptions`. Esperado: nome inexistente ou não definido.

**P7.** `TypeError` significa o quê? Qual exemplo a documentação usa?
→ Fonte: `source_python-errors-exceptions`. Esperado: nome existe, valor com tipo incompatível.

**P8.** Complete: no `NameError` o problema é o ______; no `TypeError` o problema é o ______.
→ Cuidado com a armadilha de usar "compatível" para o `NameError`.

## Bloco 4 — de onde vem o `None`

**P9.** O que uma função devolve quando termina sem `return`?
**P10.** O cálculo aconteceu, mas não saiu da função. Quem chamou recebeu o quê?
**P11.** Você concatena esse valor com um texto. Qual é a mensagem exata do erro?
→ Esperado: `TypeError: can only concatenate str (not "NoneType") to str`.
**P12.** A operação que falhou foi uma **soma** ou uma **concatenação**? Por que essa distinção importa para nomear o erro corretamente?
**P13.** `None` é o mesmo que "a variável não foi iniciada"? Explique.
→ Esperado: não. `None` é um valor, do tipo `NoneType`.

## Auto-verificação

- [ ] Consigo dizer, sem consultar, o critério que separa os dois tempos.
- [ ] Consigo explicar por que o `SyntaxError` vence o `TypeError` quando os dois estão no mesmo arquivo.
- [ ] Consigo mostrar de onde vem o `None` que provoca um `TypeError`.
- [ ] Não chamo de "compatibilidade" um `NameError`.
- [ ] Sei que a linha apontada não é necessariamente a linha do defeito.

## Fontes

- `source_python-errors-exceptions` — [8. Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- `source_python-traceback` — [traceback](https://docs.python.org/3/library/traceback.html)
