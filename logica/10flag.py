# Flag -> marcar um local
# None -> sem valor
# Is/Is Not -> é ou não é

condicao = True 
passou_no_if = None #declarando variável sem valor

if condicao:
    passou_no_if = True #marcou o local (flag)
    print("Faça algo")
else:
    print("Não faça algo")

print(passou_no_if, passou_no_if is None) #is é parecido com '==', porem é mais indicado usar o 'is' ou 'is not'

# conclusão: a variável "passou_no_if" é declarada sem valor pois se fosse declarada dentro do 'if',
# dependendo da condição, poderia dar erro no código

if passou_no_if is None:
    print("Não passou no if")
else:
    print("Passou no if")