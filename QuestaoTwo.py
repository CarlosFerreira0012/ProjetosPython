#Funçao para criar de forma alinhada as colunas e linhas.

def borda_caracteres(texto, textoBife, textoFile, textoP, textoM, textoG, ValorOne, ValorTwo, ValorTree, ValorOneF, ValorTwoF, ValorTreeF,  caracter=''):
    tamanho_Word = max(len(texto), len(textoP), len(textoBife), len(textoFile),len(textoM), len(textoG))
    tamanho_Value = max(len(ValorOne), len(ValorTwo), len(ValorTree), len(ValorOneF), len(ValorTwoF), len(ValorTreeF))
    tamanho = max(tamanho_Word, tamanho_Value) + 3  
    linha_borda = caracter * tamanho
    
    print('Bem-Vindos a Loja de Marmitas do Carlos Ferreira')
    print('Cardapio')
    print('-' + '-' * (tamanho+17) + '-' + '-' * (tamanho+17) + '-')
    print('|' + f" {texto.center(tamanho)} " + '|', '|' + f" {textoBife.center(tamanho)} "  + '|','|' + f" {textoFile.center(tamanho)} " + '|',)
    print('|' + f" {textoP.center(tamanho)} " +'|', '|' + f" {ValorOne.center(tamanho)} "   + '|','|' + f" {ValorOneF.center(tamanho)} " + '|',)
    print('|' + f" {textoM.center(tamanho)} " +'|', '|' + f" {ValorTwo.center(tamanho)} "   + '|','|' + f" {ValorTwoF.center(tamanho)} " + '|',)
    print('|' + f" {textoG.center(tamanho)} " +'|', '|' + f" {ValorTree.center(tamanho)} "  + '|','|' + f" {ValorTreeF.center(tamanho)} "+ '|',)
    print('-' + '-' * (tamanho+17) + '-', '-' + '-' * (tamanho +17) + '-', )


#Função: Importante pois sem ela nao seria possivel retornar caso erre Sabor;

# Função para validar sabor. Acertou ela break e vai para o loop .
def validar_sabor():
    while True:
        sabor = input('Entre com o sabor (BA/FF): ')
        if sabor == 'BA' or sabor == 'FF':
            return sabor
        else:
            print('Sabor Inválido. Tente Novamente')

# Função para validar tamanho. Acertou ela break e vai para o loop .
def validar_tamanho():
    while True:
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
            return tamanho
        else:
            print('Tamanho Inválido. Tente Novamente')


#Especificand/ craiando as variaveis para cada iten da funçao borda_caractere
texto = "Tamanho"
textoBife = 'Bife Acebolado (BA)'
textoFile = 'Filé de Frango(FF)'
textoP = "P"
textoM = 'M'
textoG = 'G'
ValorOne ='R$ 16.00'
ValorTwo ='R$ 18.00'
ValorTree ='R$ 22.00'
ValorOneF='R$ 15.00'
ValorTwoF='R$ 17.00'
ValorTreeF='R$ 21.00'
borda_caracteres(texto, textoBife, textoFile, textoP, textoM, textoG, ValorOne, ValorTwo, ValorTree, ValorOneF, ValorTwoF, ValorTreeF)




# Parte 1: Principal para o usuario realizar pedidos
#Acumulador iniciado antes do loop contando pedidos igual a zero. Começara a iterar de acordo com  a escolha do cliente
acumulador = 0


while True:
    # Chamando a Função que validou sabor/tamanho. Digitado no input desce para passar pelo loop
    sabor = validar_sabor()
    tamanho = validar_tamanho()

    # Resultado da função passara pelo loop e aqui sera realizado o calculo do pedido
    if sabor == 'BA' and tamanho == 'P':
        preço = 16.00
        print("Você pediu Bife Acebolado no tamanho P: R$16.00" )

    elif sabor == 'FF' and tamanho == 'P':
        preço = 15.00 
        print('Você pediu Filé de Frango no tamanho P: R$15.00')

    elif sabor =='BA' and tamanho == 'M':
        preço = 18.00
        print('Você pediu Bife Acebolado no tamanho M: R$18.00')

    elif sabor =='FF' and tamanho == 'M':
        preço = 17.00
        print('Você pediu Filé de Frango no tamanho M: R$17.00')

    elif sabor =='BA' and tamanho == 'G':
        preço = 22.00
        print('Você pediu Bife Acebolado no tamanho G: R$22.00')

    elif sabor =='FF' and tamanho == 'G':
        preço = 21.00
        print('Você pediu Filé de Frango no tamanho G: R$21.00')

    else:
        print('Opção inválida. Por favor, escolha novamente.')
        continue

    #No final do loop esta o parametro do acumulador. Acumula de preço em preço.(Preço anterior + preço atual)
    acumulador += preço

    # Pergunta se deseja fazer outro pedido
    novoPedido = input('Deseja pedir mais alguma coisa (S/N)?: ')

    if novoPedido.upper() != 'S':
        break

# Apresentar o valor total dos pedidos
#Retorna o valor do pedido convertido em Float
print(f'O valor do(s) pedido(s): R${acumulador:.2f}')
print('Obrigado! Volte Sempre!')
