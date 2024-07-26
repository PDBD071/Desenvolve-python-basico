horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25

pagamentos = [
    (ganho_por_hora * hora if hora <= 40 else ganho_por_hora * 40 + hora_extra * (hora - 40))
    for hora in horas_trabalhadas
]

print(pagamentos)
