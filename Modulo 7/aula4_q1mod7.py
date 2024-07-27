import os

# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Nome do arquivo
nome_arquivo = "frase.txt"

# Abre o arquivo no modo de escrita e salva a frase
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(frase)

# Obtém o caminho absoluto do arquivo
caminho_completo = os.path.abspath(nome_arquivo)

# Imprime o caminho completo do arquivo salvo
print(f"Frase salva em {caminho_completo}")
