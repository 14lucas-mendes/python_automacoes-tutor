# Roteiro de áudio — modelo de dois tempos do Python

Duração alvo: cerca de 2 minutos. Idioma: pt-BR. Este arquivo é o **transcript** exigido para qualquer áudio gerado a partir dele. Nada de áudio foi sintetizado ainda.

---

**Narração**

O Python olha para o seu código em dois momentos diferentes, e confundir os dois é a causa da maior parte dos diagnósticos errados.

O primeiro momento é a análise. Antes de executar qualquer linha, o Python lê o arquivo inteiro e confere a forma: as palavras existem, a gramática fecha. Se a forma está errada, o programa nem começa. Você vê um `SyntaxError`, e o mais importante: não aparece o cabeçalho `Traceback`. Isso não é detalhe de estilo. É a prova de que nada rodou.

O segundo momento é a execução. Só depois que a análise passa é que o Python roda o código, de cima para baixo. Aqui os valores existem, e é aqui que aparecem as exceções: `NameError`, `TypeError`, `ZeroDivisionError`. Essas vêm com `Traceback`, porque o programa já estava trabalhando e o rastro mostra por onde ele passou.

Agora a diferença entre os dois nomes mais confundidos. `NameError` quer dizer que o nome não existe naquele ponto: você usou algo que nunca foi definido. `TypeError` quer dizer que o nome existe, mas o valor não serve para a operação.

E existe uma origem de `TypeError` que passa despercebida: a função que termina sem `return`. O cálculo acontece, o resultado fica dentro da função, e quem chamou recebe `None`. `None` é um valor, do tipo `NoneType` — não é uma variável vazia. Quando esse `None` entra numa soma ou numa concatenação, o programa quebra.

Por isso, ao ler um erro, faça duas perguntas. Primeira: tem `Traceback`? Se não tem, o problema é de forma e nada rodou. Segunda: a linha apontada é a causa, ou é só onde a operação falhou? No caso que praticamos, o erro apareceu numa função e a causa estava em outra.

---

## Notas de produção

- Gerar somente depois de decidir o provedor; o áudio continua sendo mídia, não evidência.
- Se sintetizado localmente, concatenar os blocos e registrar o caminho do arquivo aqui.
