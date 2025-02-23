# Escreva um programa que reflita essas mudanças e permita praticar com o conceito de listas. Sua tarefa:

# etapa 1: criar uma lista vazia chamada beatles;
# etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison;
# etapa 3: Use o loop for e o método append() para solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;
# etapa 4: use a instrução del para remover Stu Sutcliffe e Pete Best da lista;
# etapa 5: Use o método insert() para adicionar Ringo Starr ao início da lista.

#Etapa 1 
beatles = []
print("Etapa 1:", beatles)

#Etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Etapa 2:", beatles)

#Etapa 3
for i in range(2):
    nome = input("Digite o nome de Stu Sutcliffe ou Pete Best: ")
    beatles.append(nome)

print("etapa 3", beatles)

#Etapa 4
del beatles[4]
del beatles[3]

#forma mais eficaz:
# for nome in ["Stu Sutcliffe", "Pete Best"]:
#     if nome in beatles:
#         beatles.remove(nome)

print("Etapa 4:", beatles)

#etapa 5
beatles.insert(0, "Ringo Starr")

print("Etapa 5:", beatles)