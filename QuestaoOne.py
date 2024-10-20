#Chamei a funçaõ juros para definir como ficara os descontos
def juros(parcelas):
    if parcelas < 4:
        juros = 0.0  
    elif parcelas >= 4 and parcelas < 6:
        juros = 0.04  
    elif parcelas >= 6 and parcelas < 9:
        juros = 0.08  
    elif parcelas >= 9 and parcelas < 13:
        juros = 0.16  
    else:
        juros = 0.32  
    return juros


print("Bem-vindos a loja do Carlos Ferreira!")

#Definindo as variaveis de valor e quantidade de parcelas. Que tera as parcelas chamada pela função.
valorDoPedido = float(input("Entre com o valor do pedido: "))
QuantDasParcelas = int(input("Entre com o quantidade de parcelas: "))

#Definindo as variaveis para realizar o calculo das parcelas 
jurosLoja = juros(QuantDasParcelas)
ValorDasParcelas = valorDoPedido * (1 + jurosLoja) / QuantDasParcelas

#CalcuTotalParcelado
ValorTotalparcelado = ValorDasParcelas * QuantDasParcelas

#Saida( f formatou em string)
print(f"O valor de cada parcela é de: R$ {ValorDasParcelas:.2f}")
print(f"O valor total parcelado é de: R$ {ValorTotalparcelado:.2f}")












