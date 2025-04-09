# """
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# """
# # num = int(input("Digite um número inteiro: "))

# # if num:      
# #     if num % 2 == 0:
# #         print("Par")
# #     else: 
# #         print("ímpar")
# # else:
# #     print("Isso não é um número inteiro")


# try: # tentar rodar o seguinte código:
#     num = int(input("Digite um número: "))
#     if num % 2 == 0:
#         print("Par")
#     else:
#         print("Ímpar")
# except: #caso dê erro, acontece isso:
#     print("isso não é um número")

# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """
# horas = int(input("Digite as horas (apenas HH): "))

# if horas >= 0 and horas <= 11:
#     print("Bom dia!")

# elif horas >= 12 and horas <= 17:
#     print("Boa tarde!")

# else:
#     print("Boa noite!")

# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
# """

# nome = input("Digite se nome: ")

# tamanho_nome = len(nome)

# if tamanho_nome <= 4:
#     print("seu nome é curto!")
# elif tamanho_nome >= 5 and tamanho_nome <= 6:
#     print("Seu nome é normal.")
# else:
#     print("Seu nome é muito grande.")

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    num = int(input("Digite um número inteiro: "))

    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")
    
except ValueError:
    print("Isso não é um número inteiro.")

"""
 Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
 descrito, exiba a saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#horas = input("Digite as horas (apenas HH): ")


# if horas >= "0" and horas <= "11":
#     print(f"Bom dia, são {horas} horas da manhã.")

# elif horas >= "12" and horas <= "17":
#     print(f"Boa tarde, são {horas} horas da tarde.")

# elif horas >= "18" and horas <= "23":
#     print(f"Boa noite! Já são {horas} horas da noite.")

# else:
#     print("Entrada inválida. Digite que horas são.")

try:
    horas = int(input("Digite as horas (em HH): "))

    if horas >= 0 and horas <= 11:
        print(f"Bom dia!")
    
    elif horas >= 12 and horas <= 17:
        print(f"Boa tarde!")

    elif horas >= 18 and horas <= 23:
        print(f"Boa noite!")
    
    else:
        print("Entrada inválida. Digite horas entre 0 e 23")

except ValueError:
    print("Entrada inválida. Digite horas entre 0 e 23")

"""
 Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
 menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
 "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é curto")

# elif tamanho_nome == 5 or tamanho_nome == 6:
#     print("Seu nome é normal")

elif 5 <= tamanho_nome <= 6:
    print("Seu nome é normal")

else:
    print("Seu nome é grande") 