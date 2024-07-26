# Entrada
frase = input("Digite uma frase: ")

# Processando
vogais = "aeiouAEIOU"

frase_substituida = ''.join('*' if char in vogais else char for char in frase)

# Saída
print("Frase com vogais substituídas:", frase_substituida)
