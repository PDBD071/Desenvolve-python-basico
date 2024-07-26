# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Itera sobre cada letra do nome, imprimindo uma linha para cada letra
for i in range(1, len(nome) + 1):
    print(nome[:i])
