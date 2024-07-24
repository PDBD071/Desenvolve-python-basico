# Entrada de dados
m = 0

# Leia n1, n2, n3
n1 = float(input("Digite a primeira nota (n1): "))
n2 = float(input("Digite a segunda nota (n2): "))
n3 = float(input("Digite a terceira nota (n3): "))

# Processamento
m = (n1 + n2 + n3) / 3

# Saída
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

