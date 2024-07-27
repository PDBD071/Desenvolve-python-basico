import string

def limpar_frase(frase):
    # Remove os caracteres não alfabéticos e converte para minúsculas
    return ''.join(char.lower() for char in frase if char.isalnum())

def verificar_palindromo(frase):
    frase_limpa = limpar_frase(frase)
    return frase_limpa == frase_limpa[::-1]

while True:
    frase = input("Digite uma frase (ou 'Fim' para sair): ")
    if frase.lower() == 'fim':
        break
    
    if verificar_palindromo(frase):
        print("A frase é um palíndromo.")
    else:
        print("A frase não é um palíndromo.")
