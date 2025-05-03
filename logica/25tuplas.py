# Tuplas - lista imutável

# criando uma tupla: (repare que ela não leva colchetes, ao contrário das listas)
nomes = 'Guilherme', 'Isadora', 'Gilberto'

# colocando entre parênteses, cria uma tupla
nomes = ('Guilherme', 'Isadora', 'Gilberto')

#printando item (mesma forma da lista)
print(nomes[0]) #printa 'Guilherme'

# transformando tupla em lista e vice-versa
    # tupla -> lista
nomes = list(nomes)
    # lista -> tupla
nomes = tuple(nomes)


