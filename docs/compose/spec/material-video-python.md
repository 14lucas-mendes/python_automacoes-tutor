# Material em vídeo da formação Python

Decisão do aluno em 2026-11-12. A Formação Cod3r (escola.formacao.dev: Formação DEV e Formação AI) e o curso de Python do Gustavo Guanabara (Curso em Vídeo) deixam de ser formações paralelas. Viram **biblioteca de vídeos** da formação Python, encaixada nas lições que já existem. A Faculdade e a formação ICC continuam independentes.

## Regras

1. **Vídeo é aquecimento ou revisão.** Cada lição lista os vídeos dela. O aluno assiste antes da teoria (aquecimento) ou depois (revisão).
2. **Não substitui a teoria escrita.** Tema novo continua com a aula completa do tutor (`theory_first`). Vídeo assistido antes não encurta a teoria nem conta como domínio.
3. **Não é evidência.** Assistir um vídeo não muda `mastery`. A evidência continua vindo das tarefas, do Feynman e da transferência.
4. **Vídeo com solução vem depois da tentativa.** Os vídeos de exercício e de desafio do Guanabara mostram a solução. Assistir antes de tentar transforma a tarefa em prática guiada. A ordem é: decompor, codar, conferir, e só então ver a correção.
5. **Sem transcrições.** O mapeamento usa títulos e ordem das aulas. Ingestão de transcrições do YouTube fica para depois da `lesson_17`, por PR na skill, só com o aluno pedindo. A Cod3r exige login, e o tutor não extrai conteúdo dela.
6. **Não muda a estrutura.** Encaixar material nas lições existentes é adaptar a aula. Criar lição ou tópico por causa de um vídeo continua sendo mudança estrutural (regra da formação fechada).
7. **O progresso nas plataformas fica nelas.** O tutor não marca aula como vista nem lê o progresso como evidência.

## Fontes

- **Guanabara:** playlist "Curso em vídeo - Python" (175 vídeos, montada por terceiro com vídeos do canal Curso em Vídeo): <https://www.youtube.com/playlist?list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0>. Blocos: aulas #01 a #23 (Mundos 1 a 3), exercícios #001 a #115 e Curso Python POO (aulas 1 a 12 e desafios 16 a 33).
- **Cod3r, Formação AI › Programação:** Python (aluno em 75% em 2026-11-12), API da OpenAI com Python (21%), MCP para Programadores (1%).
- **Cod3r, Formação AI › Apps e Sistemas e Mentoria 360:** cursos de agentes e engenharia de contexto.
- **Cod3r, Formação DEV:** Git, terminal, SQL, Docker, deploy, TypeScript, React e carreira (stack JavaScript; vale pelo conceito).

## Mapa por lição (na ordem da formação)

| Lição | Guanabara | Cod3r | Uso |
|---|---|---|---|
| `lesson_17` algoritmos e debugging (atual) | Exercícios #046 a #071 (laços) só como extra | — | revisão opcional |
| `lesson_19` Python intermediário | **Curso Python POO:** aulas 1 a 5 (classes, objetos, atributos), aulas 7 a 9 (herança, abstração), aulas 10 a 12 (encapsulamento, `@property`); aula #22 (módulos e pacotes); aula extra Rich | AI › Python (terminar os 25% restantes); DEV › Aulas ao Vivo › Programação Orientada a Objetos e Introdução aos Paradigmas; DEV › Design › Modelagem de Domínio | aquecimento e revisão; desafios POO 16 a 33 só depois da tentativa |
| `lesson_14` Git profissional | — | DEV › Git & Github (Básico, Branches, Markdown, README de Projeto); DEV › Terminal Windows e Linux | aquecimento |
| `lesson_05` SQL e PostgreSQL | — | DEV › Banco de Dados › Banco Relacional (revisão) e SQL (aluno em 14%) | aquecimento e revisão |
| `lesson_06` HTTP e APIs | Exercício #114 (site está acessível?) | DEV › API com Express JS, só o conceito de REST | revisão |
| `lesson_18` Docker e deploy | — | DEV › Dominando Docker; Express › Deploy em Produção | aquecimento |
| `lesson_08` automação | Exercício #115 a/b/c (menu e arquivos) | AI › Automação com Agentes de IA, só o conceito | revisão |
| `lesson_20` LLM estruturado | — | AI › Fundamentos de IA, Engenharia de Prompt, API da OpenAI com Python (conceito: o app usa a Claude API) | aquecimento |
| `lesson_21` contexto e RAG | — | AI › Agents, Skills & Eng. de Contexto; Mentoria 360 › Engenharia de Contexto (Skills e SDD) | aquecimento |
| `lesson_22` agente e MCP | — | AI › MCP para Programadores, Ferramentas Agênticas, Arquitetura de Engenharia Agêntica, Projeto - Usando MCP, Skills e Spec | aquecimento |
| `lesson_10` e `lesson_11` React + TS | — | DEV › Iniciando com TypeScript (74%); React & Next (Fundamentos, Tailwind, Hooks, Gerenciamento de Estado) | aquecimento (não conta como domínio; rodar o `/diagnostic` previsto) |
| `lesson_12` qualidade e CI | — | DEV › Testes em TypeScript com Jest (parte do front) | aquecimento |
| `lesson_13` portfólio | — | DEV › README de Perfil; Carreira › LinkedIn e O Lado do Recrutador | aquecimento |

### Revisão do que já foi concluído

As aulas #01 a #23 do Guanabara cobrem temas em que o aluno já tem domínio 80. Servem só de revisão, quando um card ou uma prática mostrar esquecimento:

- `lesson_01` (tipos, fluxo, coleções, funções): aulas #06, #07, #09, #10, #12, #13, #14, #15, #16, #17, #19, #20 e #21;
- `lesson_02` (arquivos e exceções): aulas #22 e #23 e exercício #115b;
- `lesson_03` (debugging): aula #23.

### Lógica em espiral (depois do bloco de lógica)

Os exercícios do Guanabara viram o banco do exercício semanal de lógica, sempre com decomposição antes do código e a correção do vídeo só depois da tentativa:

| Faixa | Assunto |
|---|---|
| #028 a #045 | condições |
| #046 a #071 | laços `for` e `while` |
| #072 a #095 | tuplas, listas e dicionários |
| #096 a #106 | funções |
| #107 a #115 | módulos, exceções e arquivos |

## Ponte para a formação ICC

Vídeos que servem às duas formações: DEV › Terminal Linux e Windows (ICC 6.3 e 6.4), DEV › Dominando Docker (ICC 7.1 e 7.2, contêiner × máquina virtual), Express › Deploy em Produção (ICC 6.5) e DEV › Design › Casos de Uso e Modelagem de Domínio (ICC 4.1 e 4.2). Redes, PLC/SCADA, normas ferroviárias e monitoramento não estão na Cod3r e continuam só na ICC.

## Fora da formação

Java, React Native, NoSQL/MongoDB/GraphQL, Firebase/AWS/Terraform, RabbitMQ, os projetos em JavaScript, n8n e low-code, Negócios e Carreira da Formação AI, HTML/CSS/JS básicos e a Formação Express (repete as outras trilhas). Clube do Livro e Método PARA servem ao cofre, não à formação.

## A skill `ai-tutor-video`

Fork de `14lucas-mendes/ai-tutor-skill` (Kadu1992/ai-tutor-video), avaliado em 2026-11-12 e **não instalado**: instalaria por cima da cópia única da skill, está 14 commits atrás e 8 à frente (com mudanças em `state-contract` e `validate_study`, que esbarram nos critérios congelados) e o `fetch_transcript.py` roda `pip install` sem confirmação. Se a ingestão de transcrições do YouTube for pedida depois da `lesson_17`, ela entra na skill própria por PR, com testes, e as transcrições ficam fora do Git.
