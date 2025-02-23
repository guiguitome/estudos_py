# ulilização dos métodos append() e insert()

#append() - usado para adicionar um novo elemento na lista criando um ultima posição
#sintaxe - variavel.append(valor)

lista = [1, 2, 3, 4, 5]
print("tamanho da lista:", len(lista))
print(lista)

lista.append(6)

print("\ntamanho da lista:", len(lista))
print(lista)

#insert() - adiciona um novo elemento a lista em uma posição especifica
#sintaxe: variavel.insert(posição, valor)
numeros = [89, 67, 50, 32, 67]
print("tamanho da lista:", len(numeros))
print(numeros)

numeros.insert(4, 44) #todos os numeros a direita vão "pular" uma posição, até mesmo o que está na posição que sera inserido um novo elemento

print("tamanho da lista:", len(numeros))
print(numeros)


