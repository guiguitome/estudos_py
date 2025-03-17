# Operadores logicos
# and - todas as condições precisam ser verdadeiras 
# qualquer valor que for falso na expressão fará que todo resto seja falso
# 0 | 0.0 | '' | None -> Falsy
entrada = input("E para entrar, [S] para sair")
senha_digit = input("senha: ")

senha_permit = "goiaba"

if entrada == 'E' and senha_digit == senha_permit:
    print("Bem-vindo")
else:
    print("sair")

#or - faz com que a expressão seja verdadeira bastando apenas uma das condições ser verdade

entrada = input("E para entrar, [S] para sair")
senha_digit = input("senha: ")

senha_permit = "goiaba"

if (entrada == 'E' or entrada == 'e') and senha_digit == senha_permit:
    print("Bem-vindo")
else:
    print("sair")

#se em alguma condição tiver uma string sendo a primeira condição a ser verdadeira, será retornado essa string

nome = 0 or 'Guilherme' or False
print(nome)

senha = input('Digite sua senha: ') or 'Sem senha'
print(senha) # caso nada seja digitado, será retornado "sem senha", pois uma string vazia ('') é um falsy 

# not - inverte valor lógico
# not true = false
# not false = true

nome = input("Digite seu nome: ")

if not nome:
    print("Você digitou nenhum nome.")
else:
    print(f"Olá, {nome}")