#if | elif | else
#se | senão se | senão

# 1 - Peça ao usuário um número e informe se ele é positivo, negativo ou zero.
# numero = int(input("Digite um número: "))

# if numero > 0:
#     print(f"{numero} é positivo.")
# elif numero < 0:
#     print(f"{numero} é negativo.")
# else:
#     print("esse número é zero")

# 2 - Peça três lados e informe se eles podem formar um triângulo.
A = int(input("Digite o tamanho do primeiro lado "))
B = int(input("Digite o tamanho do segundo lado "))
C = int(input("Digite o tamanho do terceiro lado "))

if (A + B) > C and (A + C) > B and (B + C) > A:
    print("Esse triangulo existe")
else:
    print("esse triangulo não existe")