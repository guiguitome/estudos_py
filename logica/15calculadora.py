while True:
    num1 = input("Digite um número: ")
    num2 = input("Digite um número: ")
    op = input("Digite o operador (+-*/): ")

    #valid = None #flag
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        #valid = True
    except:
        #if valid is None:
            print("Um ou ambos os números são inválidos")
            continue
    
    op_valid = '+-/*'

    if op not in op_valid:
        print("Operador inválido")
        continue

    if len(op) > 1: #se for digitador mais que um operador
        print("mais de um operador digitado")
        continue

    if op == '+':
        print(f"{num1} {op} {num2} = {num1_float + num2_float}")
    
    elif op == '-':
        print(f"{num1} {op} {num2} = {num1_float - num2_float}")
    
    elif op == '*':
        print(f"{num1} {op} {num2} = {num1_float * num2_float}")

    else:
        try:
            print(f"{num1} {op} {num2} = {num1_float / num2_float}")
        except ZeroDivisionError:
            print("Não é possível dividir por 0.")

    sair = input("Desejas sair? (digite 's')").lower().startswith('s')

    if sair:
        break