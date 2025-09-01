# desempacotar em chamdas de funções e metodos
familia = ['Guilherme', "Sara", "Socorro", "Jesus"]

# forma 1
for pessoa in familia:
    print(pessoa, end=' ') #esse end determina como vai acabar a linha, no caso aqui sendo so espaçado em vez de quebrar a linha

print('\n--------------------')
# forma 2
print(*familia)