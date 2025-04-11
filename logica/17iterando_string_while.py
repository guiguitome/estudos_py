frase = 'O Python é uma linguagem de programação'\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'.upper()

i = 0
qtd_letras = 0
letra_mais = ''

while i < len(frase):
    if frase[i] == ' ':
        i += 1
        continue

    if frase.count(frase[i]) > qtd_letras:
        letra_mais = frase[i]
        qtd_letras = frase.count(frase[i])

    i += 1 

print(f"A letra que mais apareceu foi '{letra_mais}', {qtd_letras} vezes")   
