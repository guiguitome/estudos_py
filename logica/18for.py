texto = 'Python'

for letra in texto: #cara cada 'letra' em 'texto'
    print(letra)

"""
for + range
range -> range(start, stop, step)
"""

num = range(5, 10) #um parâmetro define o fim do "alcance"
#rum = range(5, 10) #dois defininem o começo e o fim
num = range(5, 10, 2) #o ultimo parametro define o "passo", de quanto em quanto será mostrado um numero

for numero in num:
    print(numero)
