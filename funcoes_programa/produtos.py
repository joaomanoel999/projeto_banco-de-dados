import os 
import time
from funcoes_programa.menu import cabecalho , linha
        
from funcoes_programa.tratamento import input_int , cls

produtos = []
def cadastrar_produtos(produtos):
        
        cabecalho('Adicionando um novo cadastro!')
        nome = str(input('digite nome do produto: '))
        valor = input_int('digite o valor do produto: ')

        dicio_produto = {
                'nome': nome,
                'valor': valor
             }
        produtos.append(dicio_produto)
        print('Produto cadastrado com sucesso!...')
        cls()


def lista_produtos(produtos):
        if len(produtos) == 0:
            print('nenhum produto cadastrado!')
            cls()
                    
        else:
            cabecalho('LISTA DE PRODUTOS')
            linha()
            for i, dicio_produtos in enumerate(produtos):
                print(f"{i+1}- Nome: {dicio_produtos['nome']} \t Valor: {dicio_produtos['valor']}")
            linha()

                
def editar_produto(produtos):
    if len(produtos) == 0:
        print('Nenhum produto existente!')
        cls()
        return
    
    lista_produtos(produtos) # Função q está armazenada os produtos cadastrados
    cabecalho('Editar um produto existente!')
    nome = str(input('Digite o nome do produto que deseja editar: '))
    while True:
        produto_existente = False 

        for produto in produtos:  # um 'FOR' para percorrer a lista pra encontrar nome igual
            if produto['nome'] == nome:
                produto_existente = True
                print(f"Produto encontrado: {produto['nome']} - Valor: {produto['valor']}")
                novo_nome = str(input('Digite o novo nome do produto: ')).strip()
                novo_valor = input_int('Digite o novo valor do produto: ')
                
                # Atualiza os valores apenas se o usuário fornecer algo novo
                if novo_nome:
                    produto['nome'] = novo_nome
                if novo_valor:
                    produto['valor'] = (novo_valor)
                    print(f"Produto atualizado: {produto['nome']} - Valor: {produto['valor']}")
                    time.sleep(3)
                    os.system('cls')
        if produto_existente:
            break            
        else:
            print('Este produto não existe!')
            lista_produtos(produtos)
            nome = str(input('Digite o nome do produto que deseja editar: ')).strip()
                


def excluir_produto(produtos):
    while True:
        if len(produtos) == 0:
            print('Nenhum produto existente!')
            break

        produto_existente = False      
        lista_produtos(produtos)
        cabecalho('excluir produto existente!')
        nome = str(input('Digite o nome do produto que deseja excluir: ')).strip()
        
        for produto in produtos:
            if produto['nome'] == nome:
                produto_existente = True
                print(f"Produto encontrado: {produto['nome']} - Valor: {produto['valor']}")
                produtos.remove(produto)
                print('produto excluido com sucesso')
                cls()
                
        if produto_existente:
                break
        else:
            print('Este produto não existe!')
            lista_produtos(produtos)
            nome = str(input('Digite o nome do produto que deseja Excluir: ')).strip()
            
                

