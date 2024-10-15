import os
import time

def input_int(texto):
    while True:
        try:
            valor = int(input(texto))
            return valor  # Retorna o valor apenas quando a conversão for bem-sucedida
        except ValueError:
            print('Valor inválido, digite um valor inteiro.')

def cls():
    time.sleep(3)
    os.system('cls')