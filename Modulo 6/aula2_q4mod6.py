# Função para ler uma lista de números do usuário
def ler_lista(nome_lista):
    quantidade = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    lista = []
    print(f"Digite os {quantidade} elementos da {nome_lista}:")
    for _ in range(quantidade):
        elemento = int(input())
        lista.append(elemento)
    return lista

# Função para combinar duas listas de forma alternada
def combinar_listas(lista1, lista2):
    lista_combinada = []
    tamanho_minimo = min(len(lista1), len(lista2))

    # Intercalar elementos das duas listas
    for i in range(tamanho_minimo):
        lista_combinada.append(lista1[i])
        lista_combinada.append(lista2[i])

    # Adicionar elementos restantes da lista maior
    if len(lista1) > len(lista2):
        lista_combinada.extend(lista1[tamanho_minimo:])
    else:
        lista_combinada.extend(lista2[tamanho_minimo:])

    return lista_combinada

# Programa principal
def main():
    lista1 = ler_lista("lista 1")
    lista2 = ler_lista("lista 2")
    
    lista_intercalada = combinar_listas(lista1, lista2)
    
    print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))

if __name__ == "__main__":
    main()
