# Entrada de dados
import random, math

n = int(input("Digite a quantidade  de valores: "))

soma = 0

for i in range(n):
    
    soma += random.randint(0, 100)

# Saéda
print("A raiz quadrada da soma é", math.sqrt(soma) )
