# Tipo list - mutável, pode ser alterada
# é como se fosse o array em outras linguagem

# lista = list() #forma não comum
lista_2 = [] #forma mais usada / lista vazia

print(bool(lista_2)) #lista vazia -> falsy

#assim como string, possue índices
#         0   1      2            3    4
#        -5  -4     -3           -2   -1
lista = [123, True, "Guilherme", 1.2, []] # suporta quaisquer tipos

print(lista)

# alterando índices
lista[-3] = 'Isadora'

print(lista)