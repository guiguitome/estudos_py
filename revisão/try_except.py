# 1) divisão por zero
# num1 = int(input("Digite o 1° numero: "))
# num2 = int(input("Digite o 2° numero: "))

# try:
#     print(f"{num1} / {num2} = {num1/num2}")
# except ZeroDivisionError:
#     print("Erro: divisão por zero não é permitida")

# 2) conversão de tipos
# idade = input("Digite sua idade: ")

# try:
#     idade = int(idade)
#     print(f'Sua idade é {idade}')
# except ValueError:
#     print("Digite apenas números inteiros.")

# 3) lista fora de faixa
# numeros = [10, 20, 30]
# indice = int(input('Digite o índice do elemento que deseja: '))

# try:
#     print(f' no indice {indice} tem {numeros[indice]}')
# except IndexError:
#     print("índice fora da lista")

# 4) tratamento múltiplo
# try:
#     num1 = float(input("Digite o primeiro numero: "))
#     num2 = float(input("digite o segundo numéro: "))
#     print(f"{num1} / {num2} = {num1/num2}")
# except ValueError:
#     print("Erro: Digite um numero válido")
# except ZeroDivisionError:
#     print("Erro: não é possivel fazer uma divisão por zero")

# 5) finally
try: 
    f = open('dados.txt')
except:
    print('Arquivo não encontrado.')
finally:
    print('Execução encerrada')