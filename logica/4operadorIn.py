#in (está entre) e not in (não está entre)

#strings são iteráveis (navegáveis item por item)
#Ex
nome = 'Guilherme'
print(nome[0]) #mostra o índice 0 da string "Guilherme" (G)

#com isso, podemos ver se determinados elementos estão dentro de outros
print('h' in nome) #mostra se 'h' está dentro da variável nome (True)
print('a' in nome) #mostra se 'a' está dentro da variável (False)

print('h' not in nome) #mostra se 'h' NÃO está dentro da variável nome (false)
print('a' not in nome) #True

#Descobrindo se o nome do país tem 'a' no nome:
pais = input("Digite um país: ")

if 'a' not in pais or 'A' not in pais:
    print(f"{pais} não tem 'A'")
else:
    print(f"{pais} tem 'A'")
