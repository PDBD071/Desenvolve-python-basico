import re

def formatar_telefone(telefone):
    # Remove todos os caracteres não numéricos
    telefone = re.sub(r'\D', '', telefone)
    
    # Verifica o número de dígitos
    if len(telefone) == 8:
        telefone = '9' + telefone
    elif len(telefone) == 9:
        if telefone[0] != '9':
            raise ValueError("Número de 9 dígitos deve começar com 9")
    else:
        raise ValueError("Número deve ter 8 ou 9 dígitos")
    
    # Formata o número no formato XXXXX-XXXX
    telefone_formatado = f"{telefone[:5]}-{telefone[5:]}"
    return telefone_formatado

# Função para leitura e validação do número de telefone
def ler_telefone():
    while True:
        telefone = input("Digite o número de celular: ")
        try:
            telefone_formatado = formatar_telefone(telefone)
            print("Número formatado:", telefone_formatado)
            break
        except ValueError as e:
            print(e)
            print("Tente novamente.")

# Chama a função de leitura
ler_telefone()

