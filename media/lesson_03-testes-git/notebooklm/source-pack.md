# Verified Source Pack

## 8. Errors and Exceptions (The Python Tutorial)

- Source ID: `source_python-errors-exceptions`
- URL: https://docs.python.org/3/tutorial/errors.html

Excertos literais da documentacao oficial (Python 3.14.7, consultada em 2026-09-12).

"There are (at least) two distinguishable kinds of errors: syntax errors and exceptions."

Sobre erros de sintaxe:
"The parser repeats the offending line and displays little arrows pointing at the place where the error was detected. Note that this is not always the place that needs to be fixed."
"The file name (<stdin> in our example) and line number are printed so you know where to look in case the input came from a file."

Sobre excecoes:
"Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions."

Exemplos do proprio capitulo:
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero

>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined

>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    \~~~~^~~
TypeError: can only concatenate str (not "int") to str

Como ler a mensagem:
"The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string printed as the exception type is the name of the built-in exception that occurred."
"The rest of the line provides detail based on the type of exception and what caused it."
"The preceding part of the error message shows the context where the exception occurred, in the form of a stack traceback."

Funcoes sem return:
O capitulo mostra que uma funcao que termina sem return devolve None, e que esse None chega ao chamador; qualquer operacao que combine esse None com outro tipo levanta TypeError.

## traceback - Print or retrieve a stack traceback

- Source ID: `source_python-traceback`
- URL: https://docs.python.org/3/library/traceback.html

Excertos literais da documentacao oficial (Python 3.14.7, consultada em 2026-09-12).

"This module provides a standard interface to extract, format and print stack traces of Python programs. It is more flexible than the interpreter's default traceback display."

"The module uses traceback objects - these are objects of type types.TracebackType, which are assigned to the __traceback__ field of BaseException instances."

traceback.print_exception(exc, /, [value, tb,] limit=None, file=None, chain=True):
"if tb is not None, it prints a header Traceback (most recent call last):"
"it prints the exception type and value after the stack trace"

Ou seja: o cabecalho Traceback (most recent call last) e o rastro de chamadas; a ultima linha traz tipo e valor da excecao. Um SyntaxError, detectado na analise, nao produz esse cabecalho.
