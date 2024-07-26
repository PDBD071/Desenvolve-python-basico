# Entrada de dados
input_string = input("Digite uma frase: ").lower()
target_word = input("Digite a palavra objetivo: ").lower()

# Remove os espaços da string de entrada
input_string = input_string.replace(" ", "")
word_length = len(target_word)
anagrams = []

# Percorre a string com uma janela do tamanho da palavra objetivo
for i in range(len(input_string) - word_length + 1):
    substring = input_string[i:i + word_length]
    # Verifica se a substring é um anagrama da palavra objetivo
    if sorted(substring) == sorted(target_word):
        anagrams.append(substring)

# Saída
print("Anagramas:", anagrams)
