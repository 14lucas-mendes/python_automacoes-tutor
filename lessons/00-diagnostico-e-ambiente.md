# Lição `lesson_00-diagnostico`

## Objetivo observável

Medir a autonomia atual para criar, executar, testar e versionar um projeto Python mínimo.

## Pré-requisitos

Nenhum. Esta é a avaliação inicial do programa.

## Fontes verificadas

- Python Documentation — [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html), acesso em 2026-08-31.
- Pro Git — [Getting a Git Repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository), acesso em 2026-08-31.

## Ideia central

Um projeto Python profissional precisa separar o código do ambiente que o executa. Um ambiente virtual evita que as dependências de um projeto contaminem outros. Git registra mudanças como uma sequência recuperável de versões. O diagnóstico verifica se o estudante consegue explicar e executar esse fluxo, e não apenas repetir comandos.

## Exemplo concreto

Um fluxo possível no Windows é: criar a pasta do projeto, criar `.venv`, ativá-lo, executar um arquivo `.py`, instalar uma dependência quando necessário, rodar testes e registrar uma mudança em Git. Os comandos exatos serão avaliados pela justificativa e pelo resultado, não por memorização literal. Omitir uma cautela ou um nome de comando que o objetivo não tornou explícito não rebaixa a resposta; o tutor pode apontar o limite como refinamento.

## Prática guiada

Depois da tentativa autônoma, revisar apenas os pontos que impedirem a execução: diferença entre interpretador global e ambiente virtual, localização do arquivo, instalação de dependências e estado do repositório.

## Tarefa autônoma

Sem consultar IA, descreva como você criaria uma pasta de projeto, um ambiente virtual e executaria `hello.py`. Inclua os comandos que usaria e explique o que o ambiente virtual resolve. Se já souber, inclua também como faria o primeiro commit Git.

## Erros esperados

- Confundir `python` global com o interpretador do ambiente virtual.
- Ativar um ambiente em uma pasta diferente da do projeto.
- Usar `pip` sem saber qual interpretador receberá a instalação.
- Fazer commit sem verificar o estado ou sem uma mensagem significativa.

## Critérios de evidência

- Aplicação autônoma do fluxo em um projeto mínimo.
- Transferência para uma pequena alteração ou novo projeto.
- Execução e testes registrados no log da sessão.
- Classificação **correta** quando ideia central, contexto e justificativa forem materialmente adequados; **parcial** só se faltar um elemento que impeça cumprir o objetivo com segurança.

Uma solução explicada pelo tutor permanece material de estudo e não conta como evidência autônoma.

## Atualização de estado

Ao fechar a sessão, registrar a tentativa, o resultado, a retenção percebida, eventuais pontos fracos e o próximo foco em `.ai-tutor/state.json`; validar o estudo antes de concluir.
