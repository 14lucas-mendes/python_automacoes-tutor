# Verified Source Pack

## csv - CSV File Reading and Writing (Biblioteca padrao)

- Source ID: `source_python-csv-module`
- URL: https://docs.python.org/3/library/csv.html

Excertos literais da documentacao oficial (Python 3.14.7, consultada em 2026-09-18).

Sobre os dois leitores:
"The csv module's reader and writer objects read and write sequences. Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes."

Sobre csv.reader:
"Each row read from the csv file is returned as a list of strings. No automatic data type conversion is performed unless the QUOTE_NONNUMERIC format option is specified (in which case unquoted fields are transformed into floats)."
"If csvfile is a file object, it should be opened with newline=''."

Sobre DictReader:
"Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter."
"If fieldnames is omitted, the values in the first row of file f will be used as the fieldnames and will be omitted from the results."
"Regardless of how the fieldnames are determined, the dictionary preserves their original ordering."
"If a row has more fields than fieldnames, the remaining data is put in a list and stored with the fieldname specified by restkey (which defaults to None). If a non-blank row has fewer fields than fieldnames, the missing values are filled-in with the value of restval (which defaults to None)."
"DictReader.fieldnames: If not passed as a parameter when creating the object, this attribute is initialized upon first access or when the first record is read from the file."
"csvreader.__next__(): Return the next row of the reader's iterable object as a list (if the object was returned from reader()) or a dict (if it is a DictReader instance), parsed according to the current Dialect. Usually you should call this as next(reader)."

O que estes trechos NAO cobrem: qual leitor escolher para cada necessidade e o que a funcao deve devolver. Essa decisao e de projeto, nao da documentacao, e pertence ao escopo do tutor.

## 6. Modules (The Python Tutorial)

- Source ID: `source_python-modules`
- URL: https://docs.python.org/3/tutorial/modules.html

Excertos literais da documentacao oficial (Python 3.14.7, consultada em 2026-09-18).

"A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module's name (as a string) is available as the value of the global variable __name__."

Sobre executar como script (6.1.1 Executing modules as scripts):
"When you run a Python module with python fibo.py <arguments>, the code in the module will be executed, just as if you imported it, but with the __name__ set to \"__main__\"."
O trecho oficial do tutorial:
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
"you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the \"main\" file"
"If the module is imported, the code is not run"

Sobre statements de modulo:
"A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement."

O que estes trechos NAO cobrem: o efeito de um import em cadeia dentro de outro programa. Isso foi observado por execucao real na sessao, nao esta citado aqui.

## 5. Data Structures - More on Lists (The Python Tutorial)

- Source ID: `source_python-datastructures`
- URL: https://docs.python.org/3/tutorial/datastructures.html

Excertos literais da documentacao oficial (Python 3.14.7, consultada em 2026-09-18).

Sobre pop:
"list.pop(index=-1, /): Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range."

Sobre metodos que so modificam a lista nao devolverem valor:
"You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed - they return the default None. This is a design principle for all mutable data structures in Python."

Sobre fatiar criar uma copia:
"list.copy(): Return a shallow copy of the list. Similar to a[:]."
"list.append(value, /): Add an item to the end of the list. Similar to a[len(a):] = [x]."

O que estes trechos NAO cobrem: o custo de remover do inicio da lista. O tutorial trata isso em 5.1.2 (Using Lists as Queues), que aponta collections.deque para esse uso; nao foi citado aqui porque nao e o objetivo da licao.

## Built-in Functions - next()

- Source ID: `source_python-builtins`
- URL: https://docs.python.org/3/library/functions.html

Excerto literal da documentacao oficial (Python 3.14.7, consultada em 2026-09-18).

"next(iterator, default, /): Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised."

O que este trecho NAO cobre: que um leitor de CSV e um iterador e que, por isso, next() nele avanca uma linha. A ligacao esta na pagina do modulo csv (source_python-csv-module), que registra: "Usually you should call this as next(reader)".
