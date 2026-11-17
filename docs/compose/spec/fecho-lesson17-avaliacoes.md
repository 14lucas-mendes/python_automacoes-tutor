# Fecho da `lesson_17`: avaliações previstas

Feitas em 2026-11-17, no fechamento da `lesson_17-algoritmos-debugging` (`session_2026-11-17-lesson17-transferencia-01`). A lição fechou o bloco de lógica (lições 15 a 17). Skill em uso: `d7e71ef`.

Três avaliações estavam marcadas para este fecho: o domínio 100 do tópico, os critérios de domínio congelados e o pedido de carga livre.

## 1. `topic_logica-algoritmos`: 80 → 100

**Regra** (`learning-contract.md`, matriz de domínio): o 100 pede o desempenho do 80 repetido em pelo menos duas sessões e dois contextos, com detecção de limites ou autocorreção.

**Evidência:**

| Evidência | Sessão | Contexto | Resultado |
|---|---|---|---|
| `evidence_logica-transferencia-filas-01` | 2026-10-22 | ordens de serviço (filas) | correta, autônoma, transferência |
| `evidence_logica-transferencia-campeonato-01` | 2026-10-31 | tabela de um campeonato | correta, autônoma, transferência |
| `evidence_logica-debugging-transferencia-01` | 2026-11-17 | tentativas de recuperação | correta na primeira versão, sem ajuda, transferência |

- **Repetição:** três sessões e três contextos diferentes, todos com aplicação padrão autônoma e correta.
- **Detecção de limite:** na transferência de 17/11, o aluno localizou sozinho onde e por que o código falhava (um `or` no lugar de um `and`), com hipótese e previsão escritas antes de rodar.
- **Autocorreção:** a Tarefa 3, o Defeito 1 e o Defeito 2 foram corrigidos só com a conferência genérica, sem devolutiva.

**Decisão:** 80 → 100 (`mastered`).

**Ressalva de retenção, que não muda o domínio:** em 13/11 e 16/11, a teoria da sessão anterior só voltou com pista. Em 17/11, os nomes dos quatro passos voltaram sem pista. A lógica em espiral (um exercício curto por semana) e os cards cuidam disso.

## 2. Critérios de domínio congelados (desde 2026-10-22)

**O que estava congelado:** a matriz 20/40/60/80/100, a aplicação padrão e a evidência de apoio, a escada de ajuda com os tetos, a conferência antes da devolutiva, a transferência para o 80 e a regra de avanço.

**Como as regras rodaram no período** (16 sessões, de 22/10 a 17/11):

- três lições fecharam com elas: `lesson_15` (23/10), `lesson_16` (31/10) e `lesson_17` (17/11);
- 23 evidências do tópico: 10 aplicações corretas e 4 parciais, mais 6 de apoio e 3 Feynman;
- **conferência genérica:** citada em 7 evidências. Em todas, a versão seguinte saiu correta sem outra ajuda. Ela fez o papel previsto: o aluno acha a lacuna sozinho e a correção conta como autônoma;
- **transferência:** nenhuma ficou pendente por mais de 3 sessões ou 2 semanas. Esse era o "bloqueio real" que permitiria mudar as regras antes do fecho, e ele não aconteceu;
- **nenhum pedido de mudança de critério** foi registrado no período. A objeção de 10/11 (Feynman dos custos) foi um erro de classificação corrigido pelas próprias regras, não um pedido de mudança.

**Decisão:** manter os critérios **como estão**. O congelamento termina hoje. Uma mudança futura segue o fluxo normal: branch e PR na skill, com o CI verde, a pedido do aluno.

## 3. Pedido de carga livre (registrado em 2026-11-10)

**O pedido:** tirar a meta de 10 h por semana e deixar o tempo de estudo livre. Ver `pedido-carga-livre.md`.

**A regra** (`AGENTS.md`, "Formação fechada"): a carga está congelada até a `lesson_13-portfolio`. Um pedido estrutural só é aceito diante de um bloqueio real: o estágio exigir outra stack, uma tecnologia ser descontinuada ou a evidência mostrar que falta um pré-requisito.

**Avaliação:**

- **O pedido não se encaixa em nenhum dos três bloqueios.** Pela letra da regra, ele não é aceito.
- **Os dados mostram que a meta não está sendo cumprida, e isso não trava nada.** Desde 21/09, nenhuma semana chegou a 10 h; nas últimas três, foram 2,6 h, 3,8 h e 1,1 h. Mesmo assim, três lições fecharam com evidência, porque o avanço depende de evidência e não de horas.
- **A meta não sustenta nenhuma data**, porque o plano não tem prazo desde 2026-10-15.
- **O cofre já decidiu o contrário** em 2026-11-11 ("Formações em tempo livre", `80 - Decisões/2026-11.md`), e há uma pendência aberta para registrar isso nos tutores. Hoje o cofre e o tutor estão em conflito.
- **O congelamento existe para proteger escopo, ordem e stack contra mudanças repetidas.** A carga não muda nenhuma lição, nenhuma ordem e nenhum critério. Ela só muda o KPI de horas do painel e o texto da meta.

**Decisão do tutor:** pela regra, o pedido **não é aceito**. A carga de 10 h continua como referência até a `lesson_13`.

**A autoridade final é do aluno.** Se ele quiser passar por cima da regra, a mudança é aplicada numa **conversa nova**, como a regra exige, nos arquivos já listados em `pedido-carga-livre.md`: `study-config.json`, `AGENTS.md`, `curriculum.md`, `formacao-fechada.md` e o KPI do painel. Isso também resolveria o conflito com o cofre.
