# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Define as vogais
vogais = "aeiouAEIOU"

# Utiliza compreensão de listas para filtrar e ordenar as vogais
lista_vogais = sorted([char for char in frase if char in vogais])

# Utiliza compreensão de listas para filtrar as consoantes
lista_consoantes = [char for char in frase if char.isalpha() and char not in vogais]

# Saída
print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)

