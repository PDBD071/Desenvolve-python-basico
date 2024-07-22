# Dadas duas variáveis v1 = 10 e v2 = 20
v1 = 10
v2 = 20

# Utilize uma terceira variável para trocar os valores entre as duas variáveis
aux = v1  # A variável auxiliar armazena o valor de v1
v1 = v2   # v1 recebe o valor de v2
v2 = aux  # v2 recebe o valor armazenado na variável auxiliar

# Imprime os valores de v1 e v2 após a troca
print("v1:", v1)  # v1: 20
print("v2:", v2)  # v2: 10
