codigo = int(input("Qual seu código: "))

while codigo > 0:
    
    dep = int(input("Quantos dependentes você tem: "))
    renda = float(input("Qual sua renda mensal: "))
    
    print(f"\nA renda Mensal Informada é de: R$ {round(renda)}")
    
    if renda <= 1399.12:
        valorinss = renda * 0.08
        print(f"Valor do INSS mensal: R${round(valorinss)}")
        
    elif renda >= 1399.12 and renda <= 2331.88:
        valorinss = renda*0.09
        print(f"Valor do INSS mensal: R${round(valorinss)}")
        
    elif renda >= 2331.89 and renda < 4663.75:
        valorinss = renda*0.11
        print(f"Valor do INSS mensal: R${round(valorinss)}")
        
    else:
        valorinss = renda+513.01
        print(f"Valor do INSS mensal: R${round(valorinss)}")

    valorfinal = renda - valorinss

    valorcalculoIR = valorfinal - (dep * 189.59)
    
    if valorcalculoIR <= 1903.98:
        print("\nValor do IR: R$ 0,0 .\nSalário liquido sem dedução por dependente: R$ %.2f", valorfinal)
    elif valorcalculoIR >= 1903.99 and valorcalculoIR <=2826.65:
        valorimposto = (valorcalculoIR*0.075) - 142.80
        valorfinal = valorfinal - valorimposto

# 	if(valorcalculoIR <= 1903.98){
# 		valorfinal = valorfinalinss;
# 		printf("\nValor do IR: R$ 0,0 .");
# 		printf("\nSal�rio liquido sem dedu��o por dependente: R$ %.2f",valorfinal);
# 	}
# 	else{
# 		if(valorcalculoIR >= 1903.99 && valorcalculoIR <=2826.65){
			
# 			valorimposto = (valorcalculoIR*0.075) - 142.80;
# 			valorfinal = valorfinalinss - valorimposto;
# 			printf("\nValor do IR mensal: R$ %.2f .",valorimposto);
# 			printf("\nSal�rio liquido sem dedu��o por dependente: R$ %.2f",valorfinal);
# 		}
# 		else{
# 			if(valorcalculoIR >= 2826.66 && valorcalculoIR <= 3751.05){
				
# 				valorimposto = (valorcalculoIR*0.15) - 354.80;;
# 				valorfinal = valorfinalinss - valorimposto;
# 				printf("\nValor do IR mensal: R$ %.2f .",valorimposto);
# 				printf("\nSal�rio liquido sem dedu��o por dependente: R$ %.2f",valorfinal);
# 			}
# 			else{
# 				if(valorcalculoIR >= 3751.06 && valorcalculoIR <= 4664.68){
					
# 					valorimposto = (valorcalculoIR*0.225) - 636.13;
# 					valorfinal = valorfinalinss - valorimposto;
# 					printf("\nValor do IR mensal: R$ %.2f .",valorimposto);
# 					printf("\nSal�rio liquido sem dedu��o por dependente: R$ %.2f",valorfinal);
# 				}
# 				else{
# 					if(valorcalculoIR > 4664.68){
						
# 						valorimposto = (valorcalculoIR*0.275) - 869.36;
# 						valorfinal = valorfinalinss - valorimposto;
# 						printf("\nValor do IR mensal: R$ %.2f .",valorimposto);
# 						printf("\nSal�rio liquido sem dedu��o por dependente: R$ %.2f",valorfinal);
# 					}
# 				}
# 			}
# 		}
# 	}
# 	inssanual = valorinss * 12;
# 	iranual = valorimposto * 12;
# 	printf("\nINSS anual: R$ %.2f .\n",inssanual);
# 	printf("IR anual: R$ %.2f .\n",iranual);
	

# 	printf("\n %d� funcion�rio calculado.",func);
	
# 	printf("\n\n\n");
# 	printf("QUAL SEU C�DIGO:\n");
# 	fflush(stdin);
# 	scanf("%d",&cod);

# }

# 	system("pause");
# 	return 0;
# }