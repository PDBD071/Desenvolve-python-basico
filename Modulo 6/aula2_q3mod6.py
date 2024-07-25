import random

# Função para gerar uma lista de valores inteiros aleatórios
def gerar_lista(tamanho, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(tamanho)]

# Preenchendo as listas com valores aleatórios
lista1 = gerar_lista(20, 0, 50)
lista2 = gerar_lista(20, 0, 50)

# Contando a quantidade de vezes que cada elemento aparece nas listas
contagem_lista1 = {}
contagem_lista2 = {}

for valor in lista1:
    if valor in contagem_lista1:
        contagem_lista1[valor] += 1
    else:
        contagem_lista1[valor] = 1

for valor in lista2:
    if valor in contagem_lista2:
        contagem_lista2[valor] += 1
    else:
        contagem_lista2[valor] = 1

# Encontrando a interseção sem duplicatas
interseccao = []
for elemento in contagem_lista1:
    if elemento in contagem_lista2:
        interseccao.append(elemento)

interseccao.sort()

# Exibindo os resultados
print("lista1 -", lista1)
print("lista2 -", lista2)
print("Interseccao -", interseccao)

print("Contagem")
for elemento in interseccao:
    contagem1 = contagem_lista1.get(elemento, 0)
    contagem2 = contagem_lista2.get(elemento, 0)
    print(f"{elemento}: (lista1={contagem1}, lista2={contagem2})")


