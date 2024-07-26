from datetime import datetime

# Lista com os nomes dos meses
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Solicita a data de nascimento ao usuário
data_str = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Converte a string para um objeto datetime
data = datetime.strptime(data_str, "%d/%m/%Y")

# Obtém o dia, mês e ano da data
dia = data.day
mes = data.month
ano = data.year

# Saída
print(f"Você nasceu em {dia} de {meses[mes - 1]} de {ano}.")
