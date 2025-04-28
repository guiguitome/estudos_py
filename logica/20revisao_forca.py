tentativas = 0
letras_acertadas = ''
palavra_secreta = 'abacaxi'

while True:
    letra_chutada = input("Digite uma letra: ")

    if len(letra_chutada) > 1:
        print("Digite apenas uma letra.")
        tentativas += 1
        continue

    if letra_chutada in palavra_secreta:
        letras_acertadas += letra_chutada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    tentativas += 1

    if palavra_formada == palavra_secreta:
        print(f"Parabéns, a palavra secreta era {palavra_secreta}! \nTentativas: {tentativas}")
        letras_acertadas = ''
        tentativas = 0