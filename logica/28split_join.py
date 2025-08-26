#split
frase = "ai qie num sei oq, num sei oq la"
lista_frase = frase.split()
print(lista_frase)

#com parâmetro
lista_frase = frase.split(',')
print(lista_frase)

# manipulando a lista e strip
lista_frase_corrigida = []
for i, frase in enumerate(lista_frase):
    lista_frase_corrigida.append(lista_frase[i].strip())

print(lista_frase_corrigida)

#join
frase_unida = " ".join(lista_frase_corrigida)
print(frase_unida)