altura = float(input("Qual a altura da pessoa: "))

num_pessoas = 0

while altura != 0:
    
    sexo = input("Qual o sexo da pessoa?(M)Homens/(F)Mulheres: ")
    
    num_pessoas = num_pessoas + 1
    
    if sexo == "M":
        resp =(72.7 * altura) - 58
    else:
        resp =(62.1 * altura) - 44.7
    
    print(f"Seu peso ideal é {round(resp)} kg")
    
    altura = float(input("Qual a altura da pessoa: "))
    
    
print(f"{num_pessoas} Participantes")
    
