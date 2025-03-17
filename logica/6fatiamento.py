#fatiamento de strings
nome = "catavento"
# fatiamento [início:fim:passo]
print(nome[4:]) # pega a partir do indice 4 e vai até o final da string (quando é "omitido" o final, o python encara que o fim da fatiada é o final da sting)

print(nome[:len(nome)]) # len é uma função que retorna o tamanho de uma string (nesse caso, 8)

print(nome[::3]) 