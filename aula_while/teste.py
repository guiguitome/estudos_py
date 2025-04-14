"""
• Existem situacoes em que e necessario repetir o
trecho de um programa um determinado numero de
vezes, o que pode ser conseguido de duas formas.
    • Na primeira sera escrito o mesmo trecho tantas vezes quanto
    necessario, bastante trabalhoso;
"""
#contando do 0 até 10:
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print('\n')
...
# Essa forma é nem um pouco otimizada e é muito trabalhosa
# e se eu tivesse que contar até 100, teria que escrever print(n) até lá

"""
• Na segunda forma podem ser utilizados lacos de repeticao,
conhecidos tambem como loopings ou estruturas de repeticao.

• A vantagem em utilizar estrutura de repetição
é que o programa passa a ser menor e seu
processamento aumentado sem alterar o tamanho do
codigo de programacao. Desta forma é possivel
determinar repeticoes com numeros variados de
vezes.
"""

# while (enquanto) - loop condicional
# while é executado ENQUANTO algo for verdadeiro

"""
sintaxe:
while <condição>:
    <tarefa>
"""

#contando de 0 até 10

contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1


# OBS - a ordem importa:

contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)


#exercício - fazer em ordem decescente (10 até 0)

"""
exercício - Elaborar um programa que solicite
cinco vezes dois numeros para calcular e
apresentacao de uma adicao.
"""

"""
boletim escolar:
faça um programa que peça 4 notas e mostre
a média (float e while)
"""