import random

def carrega_palavras(arquivo):
    with open(arquivo, 'r') as f:
        palavras = f.read().splitlines()
    return palavras

def escolhe_palavra(palavras):
    return random.choice(palavras)

def carrega_estagios(arquivo):
    with open(arquivo, 'r') as f:
        estagios = f.read().splitlines()
    return estagios

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogo_da_forca():
    palavras = carrega_palavras('gabarito_forca.txt')
    palavra = escolhe_palavra(palavras)
    estagios = carrega_estagios('gabarito_enforcado.txt')
    
    letras_adivinhadas = ['_'] * len(palavra)
    tentativas = 6
    erros = 0
    letras_erradas = []

    print("Bem-vindo ao jogo da forca!")
    print(" ".join(letras_adivinhadas))

    while erros < tentativas and '_' in letras_adivinhadas:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_adivinhadas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_adivinhadas[i] = letra
            print(" ".join(letras_adivinhadas))
        else:
            erros += 1
            letras_erradas.append(letra)
            imprime_enforcado(erros, estagios)
            print(" ".join(letras_adivinhadas))
            print(f"Letras erradas: {', '.join(letras_erradas)}")
        
    if '_' not in letras_adivinhadas:
        print("Parabéns! Você adivinhou a palavra!")
    else:
        print(f"Você perdeu! A palavra era '{palavra}'.")

if __name__ == "__main__":
    jogo_da_forca()
