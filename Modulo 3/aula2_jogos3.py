# Entrada de dados
idade = int(input("Digite sua idade: "))

# Processamento
jogou_pelo_menos_3_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True ou False): ").strip().lower() == 'true'
quantidade_vitorias = int(input("Quantos jogos já venceu? "))
pode_ingressar = (16 <= idade <= 18) and jogou_pelo_menos_3_jogos and (quantidade_vitorias >= 1)

# Saída
print(f"Apto para ingressar no clube de jogos de tabuleiro: {pode_ingressar}")

