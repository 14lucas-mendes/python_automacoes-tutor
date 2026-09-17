def tempo_medio(registros):
    """Media de minutos parados por falha."""
    total = 0
    for registro in registros:
        total = total + registro["minutos"]
    media = total / len(registros)


def relatorio(registros):
    media = tempo_medio(registros)
    return "Tempo medio: " + media + " min"


falhas = [
    {"falha": "Bomba 1", "minutos": 30},
    {"falha": "Prensa 2", "minutos": 90},
]

print(relatorio(falhas))
