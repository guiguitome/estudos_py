"""
Laços de repetição:
While (enquanto)
é um loop condicionak, ou seja, funciona ENQUANTO a condição for verdadeira
"""
# condicao = True

# while condicao: #loop infinito
#     print("oi")

#     break #quebra o loop em que ele está 

contador = 1

# while contador < 10:
#     contador += 1
#     print(contador)

while contador <= 10:
    if contador % 2 == 0:
        contador += 1
        continue #vai pular pro proximo laço

    print(contador)
    contador += 1
