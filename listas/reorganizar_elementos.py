var1 = 1
var2 = 2

temp = var1
var1 = var2
var2 = temp

print(f"var1 = {var1}, var2 = {var2}")

#jeito mais simples
var1 = 1
var2 = 2
var1, var2 = var2, var1

print(f"\nvar1 = {var1}, var2 = {var2}")

#da pra fazer o mesmo com listas
#colocando em ordem decrescente utilizando for
lista = [1, 2, 3, 4, 5]
tamanho = len(lista)

#logica - dessa forma, troca o primeiro pelo ultimo, segundo pelo penultimo...

for i in range(tamanho // 2):
    lista[i], lista[tamanho - i - 1] = lista[tamanho - i - 1], lista[i]

print(lista) 
