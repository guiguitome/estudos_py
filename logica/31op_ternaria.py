# operação ternária (condicional em uma linha)
# <valor> if <condição> else <outro valor>

# exemplo: verificador de impar e par
num = int(input("Digite um número: "))

resposta = "par" if num%2 == 0 else "ímpar"
print(resposta)
