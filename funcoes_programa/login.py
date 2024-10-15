import time
import os
from funcoes_programa.menu import cabecalho

usuarios = {}

def login(usuarios):
    usuarios= { 
        'email': '1234',
        'senha': '1234'
    }
    cabecalho('LOGIN')
    email2 = input('digite seu email: ')
    senha2 = input('digite sua senha: ')
    
    while True:
        if usuarios['email'] == email2 and usuarios['senha'] == senha2:
            print('logado com sucesso!')
            break
        else:
            print('email ou senha incorreta!')
            time.sleep(2)
            os.system('cls')
            cabecalho('LOGIN')
            email2 = input('digite seu email: ')
            senha2 = input('digite sua senha: ')
            

