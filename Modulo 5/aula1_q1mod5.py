# Entrada
# Solicita ao usuário para inserir dois números decimais
numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))

# Calcula a diferença absoluta entre os dois números
diferenca = abs(numero1 - numero2)

# Arredonda a diferença para duas casas decimais
diferenca_arredondada = round(diferenca, 2)

# Saída
print(f"A diferença absoluta entre {numero1} e {numero2} é {diferenca_arredondada}.")
