import emoji

# Função para listar emojis disponíveis com seus códigos
def listar_emojis():
    emojis = {
        '❤️': ':red_heart:',
        '👍': ':thumbs_up:',
        '🤔': ':thinking_face:',
        '🥳': ':partying_face:'
    }
    print("Emojis disponíveis:")
    for emoji_unicode, emoji_code in emojis.items():
        print(f"{emoji_unicode} - {emoji_code}")

# Função para emojizar uma frase com base nos códigos
def emojizar_frase(frase):
    frase_emojizada = emoji.emojize(frase)
    return frase_emojizada

# Exibir lista de emojis disponíveis
listar_emojis()

# Solicitar frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada (use os códigos como :red_heart:, :thumbs_up:, etc.):\n")

# Emojizar a frase
frase_emojizada = emojizar_frase(frase_codificada)

# Exibir frase emojizada
print("\nFrase emojizada:")
print(frase_emojizada)
