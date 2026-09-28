# Audio Script — lesson_02-arquivos-erros

Roteiro de revisão para ouvir longe da tela. **Nenhum áudio foi sintetizado neste desktop**; este arquivo é o transcript completo. Duração aproximada de leitura: 3 minutos.

---

**Bloco 1 — por que existem dois leitores**

Quando você abre um arquivo tabular em Python com o módulo `csv`, você escolhe como quer ler. O `csv.reader` devolve cada linha como uma lista. O acesso passa a depender da posição: o e-mail é sempre o item de índice um. Isso funciona, mas te obriga a contar colunas e a lembrar da ordem.

O `csv.DictReader` devolve cada linha como um dicionário. Aí o acesso é pelo nome: `registro["email"]`. Você para de contar colunas.

**Bloco 2 — onde o cabeçalho vai parar**

A diferença de fundo é o que acontece com a primeira linha do arquivo.

No `csv.reader`, o cabeçalho entra nos resultados como se fosse mais um registro. Ele ocupa a linha zero, e é por isso que uma função que devolve tudo o que leu acaba devolvendo o cabeçalho junto com os dados. Isso foi observado na prática: `[['nome', 'email', 'telefone'], ['Ana', ...]]`.

No `DictReader`, o cabeçalho vira as chaves de cada dicionário e é omitido dos resultados. Repare: omitido quer dizer que ele não aparece como registro. Ele ainda está disponível, no atributo `fieldnames` do leitor — e vale a pena guardar esta diferença: num arquivo totalmente vazio, `fieldnames` é `None`; num arquivo que só tem cabeçalho, é a lista dos nomes.

**Bloco 3 — o que você não deve esperar**

Nada de conversão automática. A documentação é explícita: cada linha do arquivo é devolvida como lista de strings, e nenhuma conversão de tipo é feita. Se a coluna traz `4.5`, você recebe `'4.5'`, entre aspas. Somar exige `float()`.

E as linhas irregulares não geram erro. Uma linha com menos células que o cabeçalho recebe `None` na chave que ficou sem valor — esse é o `restval` padrão. Uma linha com mais células que o cabeçalho joga o excedente numa chave literalmente chamada `None` — esse é o `restkey` padrão. Silêncio, dos dois lados. É por isso que validar entrada é uma decisão sua, não do leitor.

**Bloco 4 — se você preferir tirar o cabeçalho à mão**

Três mecanismos, três comportamentos diferentes.

`next(leitor)` puxa a próxima linha do leitor e avança uma posição. Ele pula o cabeçalho e o laço já começa nos registros. Cuidado com dois detalhes: chamar `next` duas vezes come um registro de verdade; e, num arquivo vazio, `next` sem segundo argumento levanta `StopIteration`, que **não** é capturada por um `except FileNotFoundError`. A saída é dar um valor padrão: `next(leitor, None)` devolve `None` em vez de quebrar.

Fatiar com `result[1:]` devolve uma lista nova, do índice um até o fim, e deixa a lista original inteira. `pop(0)` faz outra coisa: remove o primeiro item da lista original e devolve o item retirado. Fatiar copia; `pop` modifica.

**Bloco 5 — o arquivo como ferramenta de outro programa**

Se você deixa uma chamada solta no fim do arquivo, ela roda sempre que o arquivo roda. Isso inclui quando ele é importado. Para separar as duas situações existe a guarda `if __name__ == "__main__"`: rodado direto, o bloco abaixo dela executa; importado, não executa. É o que permite que outro programa use a sua função sem disparar o trabalho dela.

**Fecho**

Antes de considerar a tarefa pronta, confira os três desfechos com arquivo de várias linhas: arquivo com dados devolve os registros; arquivo ausente é distinguível; arquivo só com cabeçalho devolve zero registros e continua distinguível de arquivo vazio. E importe o seu arquivo em outro — se algo aparecer na tela sem você pedir, a guarda está faltando.
