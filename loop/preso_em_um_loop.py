# A declaração break é usada para sair/encerrar um loop.

# Projete um programa que use um loop while e solicite continuamente que o usuário insira uma palavra, a menos que o usuário insira "chupacabra" como a palavra de saída secreta, caso em que a mensagem "Você saiu do loop com sucesso". Deve ser impresso na tela, e o loop deve terminar.

# Não imprima nenhuma das palavras inseridas pelo usuário. Use o conceito de execução condicional e a declaração break.
while True:
    palavra = input("Insira uma palavra: ")

    if palavra == "Chupacabra":
        break

print("Você saiu do loop com sucesso")