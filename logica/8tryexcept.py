#try/except
#try -> tenta executar o código
#except -> quando ocorre um erro no código

numero_str = input("Digite um número")

try: #ele TENTA executar o código
    numero_int = int(numero_str)
    print(f"O dobro de {numero_str} é {numero_int * 2}")
except: #caso ocorra um erro (exceção), ele executa aqui
    print("Isso não é um número")
