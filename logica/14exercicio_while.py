"""
iterando strings com while
"""

nome = "Guilherme" #iterável
tamanho_nome = len(nome)
contador = 0
nome_asterisco = ''

while contador < tamanho_nome:
    asterisco = f"*{nome[contador]}*"
    nome_asterisco += asterisco
    contador += 1

print(nome_asterisco)