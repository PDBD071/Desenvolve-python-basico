# Leitura de dados (entrada)
nome_produto1 = input("Digite o nome do produto 1: ")
preco_unitario1 = float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))

nome_produto2 = input("Digite o nome do produto 2: ")
preco_unitario2 = float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))

nome_produto3 = input("Digite o nome do produto 3: ")
preco_unitario3 = float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))

# Processamento
total_produto1 = preco_unitario1 * quantidade1
total_produto2 = preco_unitario2 * quantidade2
total_produto3 = preco_unitario3 * quantidade3

preco_total = total_produto1 + total_produto2 + total_produto3

# Impressão de dados (saída)
print(f"Total: R${preco_total:,.2f}")



