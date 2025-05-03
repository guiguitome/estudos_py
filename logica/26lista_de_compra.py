"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:
    print("LISTA DE COMPRAS!")
    opcao = input('I - Inserir item \nA - Apagar item \nL - Listar item \n').upper()

    if opcao == 'I':
        novo_item = input('Digite o item: ')
        lista.append(novo_item)
    
    elif opcao == 'A':
        try:
            item_apagado = int(input('Digite o número do item que deseja apagar: '))
            lista.pop(item_apagado)
        except:
            print("Índice inválido, digite um número válido.")
    
    elif opcao == 'L':
        if len(lista) > 0:
            for indice, item in enumerate(lista):
                print(indice, '-', item)
        else: 
            print("Ainda não tem itens na lista.")
        
    else:
        print("Opção inválida, digite novamente.")