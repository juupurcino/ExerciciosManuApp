matricula = []
achou = 0

for i in range(5):
    num = int(input("DIGITE O NÚMERO PARA CADASTRO DE MATRÍCULA: "))
    matricula.append(num)

consulta = int(input("INFORME O NÚMERO PARA CONSULTA: "))

matricula.sort()

for j in matricula:
    if(consulta == matricula[j]):
        achou = 1
        
if achou == 1:
    ("Encontrada!")
else:
    ("Não encontrado")

