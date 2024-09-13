list = []
achou = 0

for i in range(10):
    valor = int(input(f"Informe o {i+1}º valor: "))
    list.append(valor)

busca = int(input("\n Informe um valor pra ser procurado: "))

for j in list:
    if(busca == list[j]):
        achou = achou + 1

print(f"O número foi achado {achou} vezes.")