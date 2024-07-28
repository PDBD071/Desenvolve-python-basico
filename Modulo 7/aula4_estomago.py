import re

def process_script(filename):
    # Abrir o arquivo para leitura com encoding 'latin-1'
    with open(filename, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    # 1. Texto das primeiras 25 linhas
    first_25_lines = lines[:25]
    print("Primeiras 25 linhas do texto:")
    for line in first_25_lines:
        print(line.strip())

    # 2. Número de linhas no arquivo
    total_lines = len(lines)
    print("\nNúmero total de linhas no arquivo:", total_lines)

    # 3. Linha com maior número de caracteres
    max_length_line = max(lines, key=len)
    print("\nLinha com maior número de caracteres:")
    print(max_length_line.strip())

    # 4. Número de menções aos personagens "Nonato" e "Íria"
    nonato_count = sum(len(re.findall(r'\bNonato\b', line, re.IGNORECASE)) for line in lines)
    iria_count = sum(len(re.findall(r'\bÍria\b', line, re.IGNORECASE)) for line in lines)
    
    print("\nNúmero de menções ao personagem 'Nonato':", nonato_count)
    print("Número de menções ao personagem 'Íria':", iria_count)

# Nome do arquivo
filename = "estomago.txt"

# Chamar a função para processar o script
process_script(filename)
