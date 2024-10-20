
print('Bem-Vindo a fabrica de camisetas do Carlos Ferreira')

#Função escolha do modelo
def modelo_camisa():
    while True:
        modelo = input('Entre com o modelo desejado: \n (MCS) - Camiseta Manga Curta Simples \n (MLS) - Camiseta Manga Longa Simples \n (MCE) - Camiseta Manga Curta Com Estampa \n (MLE) - Camiseta Manga Longa Com Estampa \n >> ' )
        
        if modelo == "MCS":
            return 1.80
    
        elif modelo == 'MLS':
            return 2.10
     
        elif modelo == 'MCE':
            return 2.90

        elif modelo == 'MLE':
            return 3.20 

        else:
           print('Escolha inválida, entre com o modelo novamente')



#Escolher Quantidade de camisa
def num_camisa():
 while True:

    try:
        num = int(input("Entre com o número de camisetas: "))
    
        if num >= 20000:
            print('Não aceitamos tantas camisetas de uma vez.')
            continue

        if num < 20:
            return num,0 
    
        elif   20 <= num < 200:
            return num,0.05
    
        elif 200 <= num < 2000:
            return num,0.07
    
        elif 2000 <= num <= 20000:
            return num,0.12
        
        else:
            print('Não aceitamos tantas camisetas de uma vez.')
    
    except ValueError:
      print('Por Favor, entre com o número de camisetas novamente ')



#Escolher Frete
def Valor_frete():
    while True:
        frete=input('Escolha o tipo de Frete:\n 1 - Frete por Transportadora - R$ 100.00 \n 2 - Frete por Sedex - R$ 200.00 \n 3 - Retirar pedido na Fábrica - R$ 0.00 \n >>>')
        if frete == '1':
            return 100
        elif frete == '2':
            return 200
        elif frete == '3':
            return 0
        else:
            print('Opção inválida. Por Favor, Digite uma das opções acima.')


#Principal 
if __name__ == '__main__':
    modelo = modelo_camisa()
    num_camisetas, desconto = num_camisa()
    frete = Valor_frete()

    total_sem_desconto = modelo * num_camisetas

    num_camisetas_com_desconto = num_camisetas - (num_camisetas * desconto)

    total_com_desconto = total_sem_desconto - (total_sem_desconto * desconto)
    
    total = total_com_desconto + frete

#Saída

print(f'Total a pagar: R${total:.2f} - (modelo: {modelo} * Quantidade(com desconto): {num_camisetas_com_desconto} + frete: {frete})')

