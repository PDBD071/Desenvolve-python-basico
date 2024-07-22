# Variáveis iniciais
juros = 1.01
saldo = 500.0

# Calcular o acúmulo de juros por três meses
saldo *= juros  # Primeiro mês
saldo *= juros  # Segundo mês
saldo *= juros  # Terceiro mês

# Imprimir o resultado
print("Após 3 meses meu novo saldo é")
print(saldo)
