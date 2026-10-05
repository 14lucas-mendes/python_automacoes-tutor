# Storyboard e transcrição: Condições passo a passo

O "vídeo" deste pacote é local e interativo: `condicionais-passo-a-passo.html`. Cada clique avança uma linha do código. Este arquivo é a **transcrição equivalente**, para estudar sem tela ou para usar como roteiro se um vídeo for gerado no NotebookLM (pelo Cursor, com consentimento).

| Cena | Visual | Narração (resumo) |
| --- | --- | --- |
| 1. Uma porta só | `if chovendo / elif sol_forte / else` | O Python testa as portas de cima para baixo. A primeira verdadeira roda e o resto é pulado. Sai "Levar boné", e o `else` não roda. |
| 2. Ifs separados | dois `if` (café, pão) | Cada `if` solto é testado. As duas linhas aparecem. Na versão de 01/10, o `if` do arquivo ausente era solto, e o código continuava descendo. |
| 3. Sobreposição (errado) | `if nota >= 5` antes de `elif nota >= 9` | A condição geral "engole" a específica. Com 9.5, sai "Aprovado", e o louvor nunca aparece. |
| 4. Sobreposição (certo) | `>= 9`, depois `>= 5`, depois `else` | A mais específica vem primeiro. Sai "Aprovado com louvor". |
| 5. Sem guarda | `if fila[0] == "Ana"` com `fila = []` | `IndexError: list index out of range`. O programa para na hora, que nem o `ordens[0]`. |
| 6. Com guarda | `len(fila) > 0 and fila[0] == ...` | O `and` para no primeiro falso (curto-circuito), e `fila[0]` nunca é lido. Sai "Ninguém para chamar". |
| 7. Gravar cedo | `open("w")` antes do `if` | O `"w"` apaga o arquivo na hora. O boletim bom vira `[]`, e o aviso chega tarde. |
| 8. Verificar, depois gravar | `if` vazio, depois avisa; `else` grava | O arquivo bom é mantido. A ordem segura é: falhas → trabalho → verificar → gravar. |
| 9. `match` e `case _` | `"ok"` contra `case "ok!"` | O texto precisa ser idêntico. O `case _` pega o resto e fica por último. No meio, dá `SyntaxError`. |

Saídas conferidas executando os exemplos em Python 3.11.15, em 01/10/2026.
