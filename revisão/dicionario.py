# dicionarios são usados pra guardar dados em atributo:valor
# são ordenados e alteráveis
dicio = {
    "Nome": "Guilherme",
    "Idade": 19,
    "Curso": "Computação"
}
print(dicio)

#printando apenas um dos itens
print(dicio["Nome"])

#seus itens não podem ser duplicados
dicio1 = {
    "Nome": "Isadora",
    "Idade": 20,
    "Idade": 76
}
#o que está por último irá sobrescrever o primeiro
print(dicio1)

# aceita qualquer tipo de dado

# construtor diferente:
thisdict = dict(nome = "Socorro", idade = 50, altura = 1.50)
print(thisdict)