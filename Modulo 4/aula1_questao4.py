# Entrada de dados
n = int(input("Digite o valor de n: "))

# Inicialize maior como 0
maior = 0

while n > 0:
    # Leia x
    x = int(input("Digite o valor de x: "))

    # Verifique se x é maior que maior
    if x > maior:
        # Atualize maior
        maior = x

    n -= 1

# Saída
print("O maior valor é:", maior)

