tempo = int(input("Informe o tempo de fidelidade"))
valor = int(input("Informe o valor gasto na compra"))

if tempo >= 5:
    if valor > 5000:
        print("20%")
    elif valor > 1000:
        print("10%")
    else:
        print("Sem desconto")
else:
    print("Sem desconto")