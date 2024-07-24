# Entrada de dados
N = int(input("Digite o número de respondentes: "))

soma_idades = 0

contador = 0

# Processando laço while para ler as idades
while contador < N:
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    soma_idades += idade
    contador += 1

media_idades = soma_idades / N

# Saída
print(f"A média das idades é: {media_idades}")
