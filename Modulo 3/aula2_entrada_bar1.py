# Entrada de dados
# Idade de Juliana
# Idade de Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Processamento
# True se ambos forem maior de idade
# <exp1> Juliana é maior de idade
# <exp2> Cris é maior de idade
# <exp1> and <exp2>
# Em qualquer outro caso
pode_entrar =  idade_juliana >= 18 and idade_cris >= 18

# Saída
print(pode_entrar)
