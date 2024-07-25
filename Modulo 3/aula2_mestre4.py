# Entrada
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()
forca = int(input("Digite os pontos de força (de 1 a 20): ").strip())
magia = int(input("Digite os pontos de magia (de 1 a 20): ").strip())
# Processamento
validadores = {
    "guerreiro": (forca >= 15) and (magia <= 10),
    "mago": (forca <= 10) and (magia >= 15),
    "arqueiro": (5 < forca <= 15) and (5 < magia <= 15)
}

# Verifica se a classe é válida e aplica a regra de validação
# Se a classe não for válida, o resultado será False
resultado = validadores.get(classe, False)

# Saída
print(f"Pontos de atributo consistentes com a classe escolhida: {resultado}")


