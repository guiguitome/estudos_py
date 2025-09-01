# Para acessar o elemento de uma lista que está dentro de outra:
cadeiras = [
    ["Intro. Programação", "Eletronica Digital", "Logica matematica", "Calculo I"],

    ["POO", "Calculo II", "matematica discreta", "eletronica analogica", "fisica"]
]

print(f'cadeiras do S1: {cadeiras[0]}') #variavel[numero da lista][numero do conteudo da lista][por ai vai]
print(f'Uma cadeira do S2: {cadeiras[1][3]}')
#obs: vale pra tupla

for semestre in cadeiras:
    for cadeira in semestre:
        print(cadeira)