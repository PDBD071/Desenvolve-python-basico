# Frase: Meu amor mora em Roma e me deu um ramo de flores

def contar_vogais_e_indices(frase):
    vogais = "aeiou"
    indices_vogais = []
    total_vogais = 0
    
    for i in range(len(frase)):
        if frase[i].lower() in vogais:
            indices_vogais.append(i)
            total_vogais += 1
    
    return total_vogais, indices_vogais

# Leitura da string do usuário
frase = input("Digite uma frase: ")

# Contar as vogais e seus índices
total_vogais, indices_vogais = contar_vogais_e_indices(frase)

# Saída
print(f"Total de vogais: {total_vogais}")
print(f"Índices das vogais: {indices_vogais}")
