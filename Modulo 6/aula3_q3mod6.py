import random

# Passo 1: Gerar a lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Passo 2: Identificar o intervalo com a maior quantidade de números negativos
def find_max_negative_interval(lst):
    max_count = 0
    current_count = 0
    start_index = 0
    max_start = max_end = 0
    
    for i in range(len(lst)):
        if lst[i] < 0:
            if current_count == 0:
                start_index = i
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_start = start_index
                max_end = i
            current_count = 0
    
    if current_count > max_count:
        max_start = start_index
        max_end = len(lst)

    return max_start, max_end

# Encontrar o intervalo com a maior quantidade de números negativos
start, end = find_max_negative_interval(lista)

# Passo 3: Deletar o intervalo da lista
del lista[start:end]

# Passo 4: Imprimir a lista antes e depois da deleção
print("Editada:", lista)

