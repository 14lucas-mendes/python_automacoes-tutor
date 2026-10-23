# Diagrama: De onde vem o esperado?

- **Arquivos:** `esperado-vs-obtido.excalidraw` (editável, tema escuro, estilo Excalidraw) e `esperado-vs-obtido.svg` (prévia escura, abre em qualquer navegador).
- **Papel:** complementar ao quiz (`quiz.html` / `quiz.json`, que é o artefato principal).
- **Ponto fraco:** `weak_verificacao-valor-esperado`.
- **Fontes:** `source_python-assert`, `source_python-datastructures`.

## Contribuição própria

O quiz testa, pergunta por pergunta, se você distingue a fonte certa do esperado. O diagrama mostra o **caminho inteiro de uma vez**, no espaço:

- duas fontes independentes, a regra e o código;
- as duas se encontram num único `assert`;
- a seta tracejada da armadilha liga o obtido ao esperado e fecha um círculo. É ela que torna o teste inútil.

Essa relação espacial não aparece numa pergunta de múltipla escolha.

## Texto alternativo

Diagrama em tema escuro, com o título "De onde vem o esperado?" e o subtítulo "Um assert só prova algo quando ESPERADO e OBTIDO vêm de lugares diferentes".

No alto há duas caixas azuis lado a lado:
- à esquerda, "① REGRA, antes de rodar": "Card vence 09/10. Hoje é 09/10. Vence hoje → precisa revisar. Conta 1". Uma seta desce até a caixa `esperado = 1`;
- à direita, "② CÓDIGO, a função", com a chamada `contar_vencidos([{"due_at": "2026-10-09"}], "2026-10-09")`. Uma seta desce até a caixa `obtido = ?`.

Entre as duas caixas de baixo, uma seta vermelha tracejada vai de `obtido` para `esperado`, com o rótulo "✗ NÃO copie".

As duas caixas apontam para o centro, `assert obtido == esperado`, que se divide em dois resultados:
- verde, "✓ Iguais: o código segue a regra";
- laranja, "✗ AssertionError: investigue o CÓDIGO. O esperado só muda se a própria regra estiver errada".

Embaixo, uma faixa vermelha tracejada, "⚠ Armadilha: tirar o esperado rodando o código", diz:
- "rodar → ver 0 → escrever == 0 ⇒ o teste confere o código com ele mesmo: sempre verde";
- "É como perguntar ao caixa qual é o troco certo e conferir o troco dele com a resposta dele";
- nota: "Em 11/10, o caso 'vence hoje' ganhou == 0 assim; pela regra é 1".

O significado não depende só da cor: cada resultado traz um símbolo (✓, ✗, ⚠) e um texto.

## Verificação

- `"2026-10-09" >= "2026-10-09"` é `True`, e `"2026-10-09" > "2026-10-09"` é `False`. Conferido por execução em Python 3.11, em 11/10/2026.
- O `assert` com o esperado diferente do obtido levanta `AssertionError` (`source_python-assert`).
- O diagrama **não** mostra a correção do `contar_vencidos` (a estrutura para "sem data" × "venceu"). Essa decisão continua sendo sua, na próxima sessão.
