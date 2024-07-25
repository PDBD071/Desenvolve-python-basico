# Função para solicitar números inteiros ao usuário e armazená-los em uma lista
def obter_numeros():
    numeros = []
    print("Digite pelo menos 4 números inteiros. Digite 'fim' para terminar a entrada.")
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            if len(numeros) < 4:
                print("Por favor, digite pelo menos 4 números.")
            else:
                break
        else:
            try:
                numero = int(entrada)
                numeros.append(numero)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
    return numeros

# Função principal
def main():
    lista = obter_numeros()
    
    print("\nLista original:")
    print(lista)
    
    print("\nOs 3 primeiros elementos:")
    print(lista[:3])
    
    print("\nOs 2 últimos elementos:")
    print(lista[-2:])
    
    print("\nLista invertida:")
    print(lista[::-1])
    
    print("\nElementos de índice par:")
    print(lista[::2])
    
    print("\nElementos de índice ímpar:")
    print(lista[1::2])

if __name__ == "__main__":
    main()
