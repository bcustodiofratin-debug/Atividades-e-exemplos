from random import randint
from time import time
from os import system
def play():
    num_sorteado = randint(0,100)
    tentativas = 0
    inicio = time()

    system('cls')
    while True:
        chute = int(input('Digite um numero inteiro: '))
        tentativas += 1
        
        if chute < num_sorteado:
            print('😒o numero sorteado é maior')
        elif chute > num_sorteado:
            print('😢o numero sorteado e menor')
        else:
            fim = time()
            tempo = fim - inicio
            print(f'Parabens 😁 Você acerto em {tentativas} tentativas')
            print(f'Tempo gasto {tempo:.2f} segundos')
            input('Enter para encerrar...')
            break
    
    while True:
        play()
        resp = input('Deseja jogar novamente?')
        if resp in'nN' : break

