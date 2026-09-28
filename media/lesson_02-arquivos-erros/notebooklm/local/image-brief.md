# Didactic Image Brief — lesson_02-arquivos-erros

## Objetivo pedagógico

Mostrar, numa só imagem, a diferença central entre os dois leitores de CSV (`csv.reader` por posição e `csv.DictReader` por nome), o destino do cabeçalho em cada um, e a fronteira entre script e módulo decidida pela guarda `__name__ == "__main__"`.

## Prompt (para regeneração)

> Diagrama técnico em fundo claro, sem decoração. À esquerda, um arquivo `dados.csv` com três linhas: `nome,email,telefone` seguido de duas linhas de dados. Duas setas saem dele. A de cima entra num bloco `csv.reader`, que aponta para uma caixa com listas entre colchetes e a legenda "listas · por posição" e o complemento "cabeçalho = linha 0". A de baixo entra num bloco `csv.DictReader`, que aponta para uma caixa com dicionários de chaves nomeadas, legenda "dicionários · por nome" e o complemento "cabeçalho virou as chaves / cabeçalho omitido dos resultados". Na base, uma faixa tracejada com o código `if __name__ == "__main__":` e dois resultados lado a lado: "rodado direto — o bloco roda" e "importado — o bloco NÃO roda". Paleta: azul para o leitor posicional, âmbar para o leitor por nome e para o caso em que o bloco não roda, cinza para legendas. Texto em português do Brasil, sem marcas de fabricante.

## Alt text (obrigatório para acessibilidade)

Diagrama de três partes. À esquerda, um arquivo chamado dados.csv com o cabeçalho nome,email,telefone na primeira linha e dois registros nas linhas seguintes; uma nota indica que a primeira linha é o cabeçalho, o nome das colunas, e não um registro, e outra nota informa que todo valor chega como texto. Duas setas partem desse arquivo. A seta de cima entra no bloco csv.reader, que gera listas em que o acesso é feito por posição, com o cabeçalho ocupando a linha zero. A seta de baixo entra no bloco csv.DictReader, que gera dicionários em que o acesso é feito pelo nome da coluna, porque o cabeçalho virou as chaves e foi omitido dos resultados. Na parte inferior, uma faixa tracejada mostra a guarda if __name__ igual a __main__ e dois desfechos: quando o arquivo é rodado direto, o bloco roda; quando é importado, o bloco não roda.

## Arquivos

- `didactic-image.svg` — forma canônica local, vetorial, texto selecionável.
- Nenhuma imagem foi gerada por serviço externo neste desktop (ver `AGENTS.md`).

## Verificação

Rótulos conferidos contra `source_python-csv-module` (chaves vindas da primeira linha, linha omitida dos resultados) e `source_python-modules` (a guarda `__name__ == "__main__"`). Nenhuma afirmação do diagrama vem de fora dessas duas fontes.
