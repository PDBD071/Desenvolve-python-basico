# Entrada
distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))

# Processamento
if distancia < 0 or peso < 0:
    print("Distância e peso devem ser valores positivos.")
else:
    if distancia <= 100:
        custo_por_kg = 1.0
    elif distancia <= 300:
        custo_por_kg = 1.5
    else:
        custo_por_kg = 2.0

    frete = custo_por_kg * peso

    # Taxa adicional se o peso for superior a 10 kg
    if peso > 10:
        frete += 10

    # Saída
    print(f"O valor do frete é: R${frete:.2f}")
