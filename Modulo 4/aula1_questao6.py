
# Entrada
n = int(input("Digite a quantidade de experimentos: "))  # quantidade de experimentos
cont = 0

# Inicializar as variáveis resultado e controle
soma_sapo, soma_rato, soma_coelho = 0, 0, 0

# Iterações
while cont < n:
    quantia = int(input("Digite a quantidade de cobaias: "))
    tipo = input("Digite o tipo de cobaia (S para sapo, R para rato, C para coelho): ").upper()

    if tipo == 'S':
        soma_sapo += quantia
    elif tipo == 'R':
        soma_rato += quantia
    elif tipo == 'C':
        soma_coelho += quantia
    else:
        print(f"Tipo {tipo} não reconhecido")

    cont += 1

# Calcular totais e percentuais
total_cobaias = soma_sapo + soma_rato + soma_coelho
percentual_sapo = (soma_sapo / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_rato = (soma_rato / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_coelho = (soma_coelho / total_cobaias) * 100 if total_cobaias > 0 else 0

# Saídas
print("\nResultados:")
print("Total de cobaias:", total_cobaias)
print("Total de sapos:", soma_sapo)
print("Total de ratos:", soma_rato)
print("Total de coelhos:", soma_coelho)
print("Percentual de sapos: {:.2f} %".format(percentual_sapo))
print("Percentual de ratos: {:.2f} %".format(percentual_rato))
print("Percentual de coelhos: {:.2f} %".format(percentual_coelho))

