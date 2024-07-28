import re

# Nome dos arquivos
arquivo_original = "frase.txt"
novo_arquivo = "palavras.txt"

# Lê o conteúdo do arquivo original
with open(arquivo_original, "r") as arquivo:
    frase = arquivo.read()

# Remove espaços em branco e caracteres não alfabéticos
frase_limpa = re.sub(r'[^a-zA-Z\s]', '', frase)

# Separa a frase em palavras
palavras = frase_limpa.split()

# Salva as palavras em um novo arquivo, cada uma em uma linha
with open(novo_arquivo, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

# Imprime o conteúdo do novo arquivo
with open(novo_arquivo, "r") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo do arquivo 'palavras.txt':")
print(conteudo)
