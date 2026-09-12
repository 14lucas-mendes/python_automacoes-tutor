# Formação oficial: Automação e Integração de Sistemas com Python

## Objetivo profissional

Formação de transição de carreira de nove meses para atuar em Automação e Integração de Sistemas com Python. O foco é transformar experiência em manutenção, sistemas críticos, diagnóstico de falhas, processos operacionais e documentação em autonomia técnica demonstrável.

O programa tem 13 ciclos de 21 dias. Dias protegidos: segunda, terça, quinta, sexta e domingo. Em dia de trabalho, a sessão dura até 1h30; em dia de folga, até 2h. A distribuição semanal é: segunda (conceito e prática guiada), terça (recriação independente), quinta (aplicação no projeto), sexta (lógica, debugging ou teste técnico) e domingo (projeto e revisão).

## Regra de avanço e uso de IA

Uma competência só avança com evidência demonstrada: explicação autônoma, implementação de uma variação e diagnóstico de um erro relacionado. A IA atua primeiro como tutora: pergunta, oferece pistas, explica, conduz debugging e revisa código. Implementação central fornecida antes da tentativa é prática guiada, não evidência autônoma.

O núcleo não introduz FastAPI, Docker, n8n, cloud, MCP, agentes, RAG, frameworks de IA, frontend ou outras stacks. Esses temas permanecem no backlog pós-transição e não alteram o percurso sem mudança explícita de roadmap ou oportunidade profissional concreta.

## Ciclos de 21 dias

| Ciclo | Foco | Lição canônica | Marco observável |
|---|---|---|---|
| 1 | Lógica, decomposição e Python core | `lesson-01-python-core` | Resolver entradas, regras e saídas com funções e testes simples. Concluído por evidência prévia válida. |
| 2 | Debugging sistemático | `lesson-03-testes-git` | Formular hipóteses, isolar uma falha e verificar a correção. |
| 3 | Git e GitHub | `lesson-04-descoberta-processo` | Histórico legível e remoto quando aplicável. |
| 4 | Arquivos, CSV e JSON | `lesson-02-arquivos-erros` | Ler arquivos completos, tratar erros e modularizar. |
| 5 | SQL relacional | `lesson-05-automacao-confiavel` | Consultar dados operacionais com filtros, joins e agregações. |
| 6 | HTTP e APIs REST | `lesson-06-http-apis` | Cliente de API pelo terminal com falhas tratadas. |
| 7 | Integração de sistemas | `lesson-07-fastapi-dados` | Conectar fontes simuladas e registrar falhas do fluxo. |
| 8 | Selenium | `lesson-08-llm-estruturado` | Automatizar navegação controlada com dados fictícios. |
| 9 | Demo: dados e regras | `lesson-09-seguranca-custo` | Modelar falhas, reincidências e atividades de manutenção. |
| 10 | Demo: coleta e processamento | `lesson-10-agente-ferramentas` | Importar e validar registros operacionais. |
| 11 | Demo: relatórios e integração | `lesson-11-agente-controle` | Gerar relatório de reincidências e integrar fonte simulada. |
| 12 | Qualidade | `lesson-12-docker-ci` | pytest, debugging e refatoração comprovados. |
| 13 | GitHub e processos seletivos | `lesson-13-deploy-portfolio` | Repositório legível, explicação técnica e testes de entrada. |

## Projeto principal

`project-automacao-processo-real` é agora o **Sistema de Automação de Manutenção — Demo**. Ele será construído progressivamente, nunca entregue pronto pela IA, usando somente dados fictícios ou anonimizados. O domínio inclui registros de falhas, reincidências, atividades de manutenção, relatórios, informações operacionais e integração simulada entre sistemas.

O cliente de API pelo terminal já planejado foi preservado em `project-api-llm-servico` e reposicionado para o Ciclo 6, após os fundamentos necessários. Não será excluído nem antecipado.

## Estado inicial no novo currículo

- Competência validada: lógica, decomposição e Python core — domínio 80.
- Competência validada: Git, testes básicos e fluxo profissional — domínio 80.
- Trabalho preservado e reposicionado: CSV/JSON tem tentativas e explicações válidas, mas a leitura de um CSV real com retorno completo ainda precisa ser demonstrada no Ciclo 4.
- Pontos fracos preservados: lista literal em testes e fluxo de acumulação/retorno em CSV.
- Ciclo atual: 2, debugging sistemático. A próxima lição é `lesson-03-testes-git`.

<!-- IDs, evidências, sessões e critérios canônicos estão em .ai-tutor/state.json. -->
