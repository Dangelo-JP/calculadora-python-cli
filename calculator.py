while True:

    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")
    op = input("Escolha um operador entre os seguintes: Soma(+) ; Subtração(-); Multiplicação(*); Divisão(/): ")

    n1_valido = False
    n2_valido = False
    n1_float = 0
    n2_float = 0

    op_permitidos = ["+","-","*","/"]

    try:
        n1_float = float(n1)
        n1_valido = True

    except:
        n1_valido = False

    if n1_valido is False: 
        print("O primeiro número digitado é inválido !")
        continue

    try: 
        n2_float = float(n2)
        n2_valido = True

    except:
        n2_valido = False
    
    if n2_valido is False: 
        print("O segundo número digitado é inválido !")
        continue

    if op not in op_permitidos:
        print("Operador inválido !")
        continue
    
    if len(op) > 1: 
        print("Digite apenas um operador !")
        continue
    
    if op == "+":
        print(f'{n1_float} + {n2_float} = ', n1_float + n2_float)
    elif op == "-":
        print(f'{n1_float} - {n2_float} = ', n1_float - n2_float)
    elif op == "*":
        print(f'{n1_float} * {n2_float} = ', n1_float * n2_float)
    elif op == "/":
        print(f'{n1_float} / {n2_float} = ', n1_float / n2_float)

    sair = input("Deseja sair? [s/n]: ").lower()
    
    if sair == "s":
        print("Encerrando a calculadora...")
        break
    elif sair == 'n':
        print("Reiniciando a calculadora !")
        continue