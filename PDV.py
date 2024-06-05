#importando as funções
from cadastro_cliente import *
from cadastro_vendedor import *


# Tela inicial
print("Bem vindo ao VENDEX, seu app preferido de vendas!")

while True:
    print('''Selecione uma das opções:

    [1] Login
    [2] Cadastrar
          
          ''')

    menu_inicial = input('Selecione a opção>>')
    

    if menu_inicial == '1':
        username = input('Usuário: ')
        password = input("Senha: ")
        login_vendedor(username, password)
        if login_vendedor := True:
            break

    elif menu_inicial == '2':
        while True:
          username = input('Novo nome de usuário: ')
          password = input('Nova senha: ')
          registro_vendedor(username, password)

        
    else:
        print('Opção inválida, tente novamente')


#Ambiente do vendedor
print('''O que gostaria de fazer?
      
      
      [1] Cadastrar Cliente
      [2] Buscar/Adicionar Produto
      [3] Carrinho
      [4] Relatório de vendas
      
      ''')
choice = input('Opção: ')

if choice == '1':
    username = input('Nome de usuário: ')
    passsword = input('Senha: ')
    register_user(username, password)