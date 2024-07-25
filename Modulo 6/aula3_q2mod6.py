# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Cria uma lista para armazenar os nomes dos domínios
dominios = []

# Percorre cada URL na lista
for url in urls:
    # Remove o prefixo "www." e o sufixo ".com"
    dominio = url[4:-4]
    # Adiciona o nome do domínio à lista
    dominios.append(dominio)

# Exibe a lista dos domínios
print(dominios)
