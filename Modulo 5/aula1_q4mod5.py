from datetime import datetime

# Obtém a data e hora atuais
now = datetime.now()

# Formata a data e hora como string no formato desejado
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Saída
print(formatted_time)
