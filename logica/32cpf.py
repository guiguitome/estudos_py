# Coletar a soma dos 9 primeiros digitos do CPF, multiplicando cada um dos valores por uma contagem regressiva começando em 10
cpf = input("")

cont = 10
soma = 0
cpf_tratado = []
for digito in cpf:
    if digito == '.':
        continue
    elif digito == '-':
        break
    else:
        digito = int(digito)
        cpf_tratado.append(digito)
        mult = digito * cont
        soma = soma + mult
        cont -= 1

resto = (soma*10)%11
primeiro_digito = 0 if resto > 9 else resto  
print(f'O primeiro dígito do cpf é {primeiro_digito}')








