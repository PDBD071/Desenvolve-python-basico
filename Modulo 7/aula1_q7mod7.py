# Entrada de dados
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave_aleatoria = 5

def encrypt(strings, key):
    def shift_char(c, n):
        code = ord(c)
        new_code = ((code - 33 + n) % 94) + 33
        return chr(new_code)
    
    
    encrypted_strings = []
    for s in strings:
        encrypted_string = ''.join(shift_char(c, key) for c in s)
        encrypted_strings.append(encrypted_string)
    
    return encrypted_strings

# Saída
nomes_criptografados = encrypt(nomes, chave_aleatoria)
print("Nomes criptografados:", nomes_criptografados)
print("Chave de criptografia:", chave_aleatoria)