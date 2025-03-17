nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not nome or not idade:
    print("Desculpe, você deixou campos vazios.")
else: 
    print(f"Seu nome é {nome}")
    print(f"seu nome invertido é {nome[::-1]}")
    if ' ' in nome:
        print("Seu nome contem espaços")
    else:
        print("seu nome não contem espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")

