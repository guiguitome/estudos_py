blocos = int(input("quantos blocos tem a pirâmide: "))
altura = 0
blocos_colocados = 1

while blocos >= blocos_colocados:
    blocos -= blocos_colocados
    blocos_colocados += 1
    altura += 1

print("Altura da pirâmide: ", altura)



