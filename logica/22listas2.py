# valor de um item da lista em uma variável
lista = [1, 2, 3, 4]
# variável "numero" possue o valor que está no índice 3 na lista
numero = lista[3]
#printa o valor que está no índice três
print(numero)

# CRUD - Create Read Update Delete

# deletando
#del lista[1]
# todos os itens que estão na frente do item deletado tomarão o índice n - 1, sendo n o valor atual

# adicionando item no final da lista (o parâmetro é o valor que será adicionado)
lista.append(5)

#deletando o ultimo item da lista (sem parâmetro)
lista.pop()

# deletando indice especifico
lista.pop(2)

ultimo_valor = lista.pop()
print(lista, "Removido = ", ultimo_valor)

# lista.clear() - limpa a lista

# insert - adicionar elemento na lista no indice selecionado
# sintaxe - variavel.insert(num do indice, item adicionado)

lista.insert(0, 0)

# concatenar listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# forma 1
lista_c = lista_a + lista_b
print(lista_c)

# forma 2
lista_a.extend(lista_b)
print(lista_a)
