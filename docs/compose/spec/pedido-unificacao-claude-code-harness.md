# Pedido de mudança: unificar Claude Code e Harness Engineering nesta formação

Status: **registrado em 2026-10-23, aguardando avaliação no fecho da `lesson_16-estruturas-dados`.**

Este pedido segue a regra de formação fechada ([`formacao-fechada.md`](formacao-fechada.md), seção 6, e `AGENTS.md`):
1. o tutor cita a regra e registra o pedido;
2. o pedido **não é aplicado nesta conversa**;
3. ele é avaliado no fecho da lição atual, com justificativa escrita;
4. só é aceito diante de um bloqueio real, ou, como no pedido de 15/10, se não tocar nenhum item congelado.

## 1. O pedido

Nas palavras do aluno (2026-10-23): "eu quero unificar todas as formações que eu tenho numa só. Então, inclua a do Claude Code e inclua também a do Harness Engineer. Eu quero deixar tudo numa formação só. Como eu não tenho tempo para conclusão, eu vou estudando as lições conforme eu for avançando nas etapas. Então, não tem problema ficar tudo num contexto só."

- **Claude Code:** sair da condição de formação separada, decidida em 15/10, e entrar nesta formação.
- **Harness Engineering:** hoje já é material de referência da trilha de agentes prevista para depois da `lesson_13` (decisão de 2026-10-23). O pedido é que o conteúdo dela faça **parte** desta formação, e não fique só como referência.

## 2. Situação em 2026-10-23

| | `formacao-claude` (`formacao_claude-code`) | `harnnes-engeniring` |
|---|---|---|
| Estado | 26 tópicos, todos em 0; 0 lições; 0 evidências | 4 fases; sem sessões; `state` revisão 2 |
| Sessões | 1, de 02/10, interrompida e retomada em 09/10 | nenhuma |
| Git | remoto `14lucas-mendes/formacao-claude`, trabalho na branch `claude/formacao-profissional-empreendedora-np6j6r` | não é repositório Git |
| Carga planejada | 4 h/semana (104 h), prazo 2027-03-31 | até 2 h/semana, sem prazo |
| Conteúdo | ambiente, modelo mental, contexto, planejamento, debugging, Git/PR, custos, skills, MCP, hooks, subagentes, worktrees, CI | anatomia do harness, modelo × harness, desenho, versão própria, avaliação e melhoria |

**Sobreposição com esta formação:**
- **Git, PR e CI:** `lesson_14` e `lesson_12`.
- **Testes e debugging:** `lesson_03`, `lesson_17` e `lesson_12`.
- **Agentes, MCP, ferramentas e avaliação:** `lesson_20` a `lesson_22`.
- **Subagentes e orquestração:** a trilha de agentes depois da `lesson_13`.
- **Exclusivo do Claude Code como ferramenta:** setup, contexto e sessões, custos, skills, hooks, worktrees e execução não interativa.

## 3. Pontos a avaliar no fecho da `lesson_16`

1. **Itens congelados:** incluir o Claude Code pode exigir lições ou tópicos novos, e isso é congelado até a `lesson_13`. Verificar se cabe como **conteúdo dentro das lições existentes**, como na unificação de 15/10, ou só como uma trilha depois da `lesson_13`.
2. **Carga:** somar as 4 h + 2 h planejadas às 10 h congeladas não é possível sem mudar a carga. Numa formação só, a meta continua uma só. O aluno declarou que não tem prazo e que vai avançar por etapas.
3. **Critérios de domínio:** estão congelados até a `lesson_17`. Nenhum critério das outras formações é importado.
4. **Evidências:** não há nada a migrar. As duas formações estão com domínio 0.
5. **Histórico:** antes de arquivar o `formacao-claude`, conferir a branch de trabalho e o estado no remoto.

**Nota prévia do tutor, que ainda não é a decisão:** há sobreposição real, e as duas formações estão paradas, o que favorece unificar. O ponto sensível é **onde** o conteúdo exclusivo de Claude Code entra sem criar lição antes da `lesson_13`. Uma saída possível é usar o Claude Code como lente em lições existentes (`lesson_14`, `lesson_12` e `lesson_22`) e deixar o resto na trilha pós-MVP, ao lado do harness. A avaliação fica para o fecho da `lesson_16`.
