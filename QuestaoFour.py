
print( '---------Bem-vindo a empresa do Carlos Ferreira---------')

#Definição da lista e id global que partirá do meu ID 
lista_funcionarios = []
id_global = 4681480

#Funcao de cadastro dos funcionario
def cadastrar_funcionario(id):
   
   nome = input('Digite o nome do Funcionário: ')
   setor = input('Digite o setor do Funcionario: ')
   salario = float(input('Digite o salário do Funcionario: '))

   #dicionario: armazena dados do funcionario.
   cadastro = {'id':id,'\n' 'nome':nome,'\n' 'setor':setor,'\n' 'salario': salario}
   
   #fazer um copy do dicionario para a lista_funcionarios
   lista_funcionarios.append(cadastro)

#Função para consultar dados
def consultar_funcionarios():

 opcao = int(input(' Qual opção deseja: \n 1 - Consultar Todos \n 2 - Consultar por Id \n 3 - Consultar por Setor \n 4 - Retornar ao menu \n >>>>: '))

 if opcao == 1:
   for cadastro in lista_funcionarios:
     print(cadastro) 

 elif opcao == 2:
   consulta_id = int(input('Digite o Id do Funcionário: '))
   for cadastro in lista_funcionarios:
     if cadastro['id'] == consulta_id:
        print(cadastro)
        break
     
 elif opcao == 3:
   consulta_setor = (input('Digite o setor do Funcionário: '))
   for cadastro in lista_funcionarios:
     if cadastro['setor'] == consulta_setor:
        print(cadastro)

 elif opcao == 4:
   return
 
 else:
   print('Opção inválida')


# Funçao remover cadastro de funcionario

def remover_funcionario():
    remover_id = int(input('Qual é o Id do funcionário a ser removido: ') )
    for i,cadastro in enumerate(lista_funcionarios):
      if cadastro['id'] == remover_id :
         lista_funcionarios.remove(cadastro)
         print('Funcionário removido da base de dados')
         break
    else:
         print('Id inválido')


#Menu fora das outras funçoes
print('------------------ MENU Principal ------------------ ')

def main():
  global id_global #declarando variavel 
  while True:
    opcao = int(input('Qual opção deseja:\n \n 1 - Cadastrar Funcionário \n 2 - Consultar Funcionário \n 3 - Remover Funcionário \n 4 - Encerrar Programa \n >>>'))
        
    if opcao == 1 :
      id_global += 1
      cadastrar_funcionario(id_global) # passando o id para o cadastro global
    
    elif opcao == 2 :
      consultar_funcionarios()

    elif opcao == 3 :
      remover_funcionario()

    elif opcao == 4 :
      print('Programa Encerrado !')
      break

    else:
      print('Opção inválida')
      

#principal: chama a função main iniciadora do programa para saber se ela esta funcionando\ser executada primeiro


if __name__ == '__main__':
  main()



   







   

