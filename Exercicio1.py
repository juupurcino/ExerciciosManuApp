def soma(num1, num2):
    return round(num1 + num2)

def sub(num1, num2):
    return round(num1 - num2)

def div(num1, num2):
    return round(num1/num2)

def mult(num1, num2):
    return round(num1*num2)


op = input("INFORME QUAL OPERAÇÃO DESEJA REALIZAR\nS - SOMA / U - SUBTRAÇÃO / X - MULTIPLICAÇÃO / D - DIVISÃO\nOu digite # para sair do sistema\n")

while op != "#":
    
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    match op:
        case "S":
            print("Soma: ", soma(num1, num2))
        case "U":
            print("Subtração: ", sub(num1, num2))
        case "X":
            print("Multiplicação: ", mult(num1, num2))
        case "D":
            print("Divisão: ", div(num1, num2))

    op = input("INFORME QUAL OPERAÇÃO DESEJA REALIZAR\nS - SOMA / U - SUBTRAÇÃO / X - MULTIPLICAÇÃO / D - DIVISÃO\nOu digite # para sair do sistema\n")
