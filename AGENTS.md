# Formação Python — regras do tutor

Este repositório é um programa persistente da skill **ai-tutor** (workflows, contratos de estado, evidência, escada de ajuda e matriz de domínio). Não usar `accelerated-learning` nem misturar skills sem pedido explícito do aluno.

## Estado

Canônico: `.ai-tutor/state.json`, `study-config.json`, `cards.json`, `sources.json`, `media-index.json`.
`curriculum.md`, `flashcards.md` e `lessons/` são projeção legível. `session-log.md` é mantido **à mão** — não rodar `python -m scripts.projections` neste estudo: o gerador reescreve `session-log.md` sem condição e substituiria a narrativa por um resumo mecânico.

Validar depois de qualquer mudança de estado, a partir da raiz da skill (`C:\Users\lucka\.config\mimocode\skills\ai-tutor`):

```
python -m scripts.validate_study "E:\Lucas\Documents\Faculdade AI\python_automacoes-tutor"
```

Atualizações em `.ai-tutor/*.json` usam `scripts/state_io.atomic_update_json` com `expected_revision`.

## Regras pedagógicas obrigatórias

O aluno está aprendendo Python do início. Termo desconhecido **não é falha dele: é lacuna do material**.

1. **Aula explicativa antes de avaliar.** Todo conceito ainda não ensinado nesta formação recebe primeiro uma explicação: definir o termo → analogia → exemplo concreto (executado quando possível) → e só então perguntar. Nunca abrir com pergunta gerativa sobre conteúdo novo.
2. **Nunca assumir conhecimento.** Antes de usar um termo técnico pela primeira vez na conversa, defini-lo ali e escrevê-lo na lição. Não inferir domínio de temas vizinhos, nem do campo `mastery` do `state.json`.
3. **Conteúdo não ensinado não vira nota baixa.** Se a pergunta dependia de algo nunca introduzido, a resposta não é classificada como `incorrect` nem `partial` do aluno. Ensine, registre a lacuna como ponto fraco (`category: "conceptual"`) e siga. Evidência de avaliação só se aplica a conteúdo já ensinado e praticado.
4. **Mais de um exemplo por conceito.** Um exemplo não basta para gerar resposta autônoma; usar ao menos dois, variando o contexto.
5. **Concretizar antes de abstrair.** Preferir analogia, diagrama, imagem ou execução real a definição abstrata.
6. **Ao fechar o ciclo de erro**, classificar literalmente pelo contrato de aprendizagem, distinguindo falha de domínio de falha do material.

## Transferência e contexto (decisão do aluno, 2026-09-17)

**Não exigir contexto novo sintético** — repositório, pasta ou projeto criado só para a avaliação — como condição de fechamento de lição. O uso real, no trabalho do aluno e em repositórios que já existem, é contexto de transferência válido e preferível. Criar projetos artificiais para treinar comandos já usados custa tempo de tarefas mais importantes, sem ganho pedagógico.

- A transferência continua sendo exigida pela matriz de domínio. Ela conta quando o tópico **já** sustenta o domínio com evidência autônoma real registrada; não se reaplica a exigência que já está satisfeita.
- Contexto sintético segue permitido como prática, nunca como exigência de fechamento.
- Se o que falta é apenas a **forma exata** de um comando (nome, subcomando, flag), o tutor ensina, registra ponto fraco de `precision` e segue. Não criar tarefa de execução sintética para isso.
- Consultar a documentação ao usar um comando é prática aceita. O critério é usar o comando certo, não recitá-lo de memória.

## Diário no Obsidian

Quando uma lição passar a `completed` no estado canônico, gravar o diário **na mesma virada de fechamento**, sem esperar pedido. Não gravar diário se a lição continuar `in_progress`.

- Vault: `C:\Users\lucka\Documents\Projeto Transição de Carreira`
- Pasta: `20 - Áreas/Sistema de Estudos/`
- Arquivo: `AI Tutor - Python automações - <lesson-id-com-hífen>.md` — o vault usa hífen depois de `lesson` (`lesson-01-python-core`), enquanto o `lesson_id` canônico usa underscore (`lesson_01-python-core`). Manter o hífen no nome do arquivo.
- Exemplo a seguir: `AI Tutor - Python automações - lesson-01-python-core.md`

Atualizar `[[MOC - Sistema de Estudos]]`. O diário é projeção, não evidência.

## Mídia e geração externa

**Decisão do aluno (2026-09-12): este desktop não usa NotebookLM nem Gemini.** Não há MCP, integração ou automação de navegador para mídia externa neste estudo.

- O workflow `/media` aqui para na criação do pacote local (`media/<lesson-id>/notebooklm/`): fontes verificadas, prompts ancorados, manifest e fallbacks locais preenchidos pelo tutor.
- **Nunca** pedir consentimento de upload, **nunca** automatizar navegador e **nunca** afirmar que um artefato externo existe a partir daqui.
- O aluno gera mídia externa por conta própria, **no Cursor ou no Codex**. Quando ele trouxer o resultado, o tutor confere o artefato contra as fontes registradas e atualiza `.ai-tutor/media-index.json`.
- Contexto técnico: `@playwright/cli` está quebrado nesta máquina (o daemon interno recebe um argumento a mais do que aceita) e o caminho por CDP exigiria um perfil com sessão autenticada do aluno.
