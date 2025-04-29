# valor de um item da lista em uma variável
lista = [1, 2, 3, 4]
numero = lista[3]
print(numero)

# CRUD - Create Read Update Delete
# deletando
del lista[1]
# todos os itens que estão na frente do item deletado tomarão o índice n - 1, sendo n o valor atual

# adicionando item no final da lista
lista.append(5)

#deletando o ultimo item da lista
lista.pop()

# deletando indice especifico
lista.pop(2)