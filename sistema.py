from funcoes_programa.produtos import cadastrar_produtos, lista_produtos , editar_produto, excluir_produto
from funcoes_programa.tratamento import input_int, cls
from funcoes_programa.menu import menu, cabecalho
from funcoes_programa.login import login


usuario = {}
produtos = []
lista = []

login(usuario)

menu(lista)

while True:
    opc = input_int('digite a opção: ')
    
    if opc == 1:
        cadastrar_produtos(produtos)
        

            
    elif opc == 2:
        lista_produtos(produtos)
        

    elif opc == 3:
        editar_produto(produtos)
        

    elif opc == 4:
        excluir_produto(produtos)
        

    elif opc == 5:
        print('saindo...')
        break
    else:
        print("Valor invalido, Tente novamente")
    menu(lista)
