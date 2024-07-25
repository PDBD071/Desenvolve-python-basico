# Entrada de dados
import random
numero_secreto = random.randint(1, 10)
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 10.")

while True:
  palpite = int(input("Digite seu palpite: "))
  tentativas += 1

  if palpite < numero_secreto:
    print("O número secreto é maior.")
  elif palpite > numero_secreto:
    print("O número secreto é menor.")
  else:
    print(f"Parabéns! Você acertou em {tentativas} tentativas.")
    break
