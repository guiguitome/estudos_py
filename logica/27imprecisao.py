"""
imprecisão de ponto flutuante
"""
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)

# formatar:
print(f'{numero_3:.2f}')

#usando uma função
print(round(numero_3, 2)) #round(variavel, numero de casas decimais) (se for zeros, ele corta)

# usando modulo decimal
numero_1 = decimal.Decimal('0.7')
numero_2 = decimal.Decimal('0.1')
num3 = numero_1 + numero_2
print(num3)