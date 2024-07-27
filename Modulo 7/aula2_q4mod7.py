def validador_senha():
    senha = input("Digite a senha: ")
    
    if len(senha) < 8:
        return False
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_caractere_especial = False
    
    caracteres_especiais = "@#$"
    
    i = 0
    while i < len(senha):
        char = senha[i]
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in caracteres_especiais:
            tem_caractere_especial = True
        i += 1
    
    return tem_maiuscula and tem_minuscula and tem_numero and tem_caractere_especial

# Saída
if validador_senha():
    print("True")
else:
    print("False")
