# Leitura de dados (entrada)
temperatura_f = int(input("Digite a temperatura em Fahrenheit: "))

# Processamento
temperatura_c = (temperatura_f - 32) * 5 / 9

# Converte Celsius para inteiro
temperatura_c_int = int(temperatura_c)

# Impressão de dados(saída)
print(f"{temperatura_f} graus Fahrenheit são {temperatura_c_int} graus Celsius.")
