import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 5:
            return palavra  # Palavra muito curta para embaralhar
        
        primeira_letra = palavra[0]
        ultima_letra = palavra[-1]
        letras_internas = list(palavra[1:-1])
        random.shuffle(letras_internas)  # Embaralha as letras internas
        palavra_embaralhada = primeira_letra + ''.join(letras_internas) + ultima_letra
        return palavra_embaralhada
    
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)

# Exemplo de uso
frase = input("Digite uma frase: ")
resultado = embaralhar_palavras(frase)
print(resultado)





