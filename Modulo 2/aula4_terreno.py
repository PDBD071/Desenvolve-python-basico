# Entrada
comprimento = int(input("Digite o comprimento: "))
largura = int(input("Digite a largura: "))
preco_m2 = float(input("valor do m2: "))

# Fórmulas:
area = comprimento * largura #m2
preco_total = area *preco_m2

# Imprime o resultado com a formatação solicitada
print(f"O terreno possui{area}m2 e custa R${preco_total:,.2f}")
