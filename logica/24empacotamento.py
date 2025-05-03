# Introdução desempacotamento

# nome = ['João', 'Roberto', 'Gabriel']
# nome1, nome2, nome3 = nome

# desempacotamento:
# nome1, nome2, nome3 = ['João', 'Roberto', 'Gabriel'] # cada variável foi atribuida na ordem dos itens
# print(nome2) # sera printado "Roberto"

# # se tiver mais variáveis que valores dará erro:
# nome1, nome2, nome3, nome4 = ['João', 'Roberto', 'Gabriel'] # cada variável foi atribuida na ordem dos itens
# print(nome2)

# # a mesma coisa se tiver mais valores do que variáveis
# nome1, nome2 = ['João', 'Roberto', 'Gabriel'] # cada variável foi atribuida na ordem dos itens
# print(nome2)

# se eu quiser pegar apenas um valor de uma lista
nome1, *resto = ['João', 'Roberto', 'Gabriel']
# variável 'nome1' pega o primeiro valor da lista, e a variável 'resto', com um asterisco na frente,
# empacota o restante
print(nome1, resto)

# convenção mais utilizada, indicando que a variável não será usada
nome1, *_ = ['João', 'Roberto', 'Gabriel']
print(nome1)

# se eu quiser o segundo valor?
_, nome2, *_ = ['João', 'Roberto', 'Gabriel']
print(nome2)

# terceiro valor
_, _, nome3, *_ = ['João', 'Roberto', 'Gabriel']
print(nome3)

