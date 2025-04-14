import os

palavra_secreta = 'python'
letras_acertadas = ''
chances = 0

while True:
    tentativa = input("Digite uma letra: ")

    if len(tentativa) > 1:
        print("Apenas uma letra.")
        continue

    if tentativa in palavra_secreta:
        letras_acertadas += tentativa

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    chances += 1       
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f"Parabens! A palavra era {palavra_secreta}")
        print("Número de tentativas: ", chances)
        letras_acertadas = ''
        chances = 0