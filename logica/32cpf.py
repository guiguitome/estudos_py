# Coletar a soma dos 9 primeiros digitos do CPF, multiplicando cada um dos valores por uma contagem regressiva começando em 10
import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))
cont = 10
soma = 0
for digito in nove_digitos:
    digito = int(digito)
    mult = digito * cont
    soma = soma + mult
    cont -= 1

resto_1 = (soma*10)%11
primeiro_digito = 0 if resto_1 > 9 else resto_1  
print(f'O primeiro dígito do cpf é {primeiro_digito}')

cont = 11
soma = 0
for digito in nove_digitos + str(primeiro_digito):
    soma += (int(digito) * cont)
    cont -= 1

resto_2 = (soma * 10)%11
segundo_digito = 0 if resto_2 > 9 else resto_2
print(f"O segundo dígito do cpf é {segundo_digito}")

print(f'{nove_digitos}-{primeiro_digito}{segundo_digito}')