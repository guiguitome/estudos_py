# Split - divide uma string
frase = "ai que num sei oq, num sei oq lá"
# sem paramentro, o split divide as palavras pelos whitespaces (\n, espaço, tab)
lista_palavras = frase.split() #será feito uma lista das palavras separadas
print(lista_palavras)

lista_frases = frase.split(',') #o paramentro dita em qual caractere será feito a divisão
print(lista_frases)

