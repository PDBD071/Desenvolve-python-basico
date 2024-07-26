def calcular_digito_verificador(digitos, multiplicadores):
    soma = sum(d * m for d, m in zip(digitos, multiplicadores))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return "Inválido"

    digitos = list(map(int, cpf[:9]))
    primeiro_digito = calcular_digito_verificador(digitos, range(10, 1, -1))
    segundo_digito = calcular_digito_verificador(digitos + [primeiro_digito], range(11, 1, -1))

    if cpf == f"{cpf[:9]}{primeiro_digito}{segundo_digito}":
        return "Válido"
    else:
        return "Inválido"

# Saída
cpf_input = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")
resultado = validar_cpf(cpf_input)
print(resultado)
