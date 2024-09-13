valorInicial = float(input("Digite o valor inicial: "))
debitos = float(input("Qual os débitos: "))
creditos = float(input("Qual os créditos: "))

resp = valorInicial + creditos
resp = resp - debitos

if resp > 0:
        print(f"Saldo Positivo em R${resp}")
elif resp < 0:
        print(f"Saldo Negativo em R${resp}")
else:
        print("Saldo zerado")
