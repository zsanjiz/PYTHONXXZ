import time
from random import randint
def linha(msg):
    print('-='*30)
def tempo(msg):
    time.sleep(1)
def tapa(msg):
    for c in range(1 , 7):
        time.sleep(1)
        print(f'{c}')
while True:
    dadoa = 0
    print('SIMULADOR DE DADOS :')
    linha(dadoa)
    dado = str (input('JOGUE O DADO [ direita(d) ou esquerda(e) ] =')).upper()
    if dado == 'D':
        print('direita>>>>>')
    elif dado == 'E':
        print('<<<<<<<esquerda ')

    linha(dadoa)
    sim = str(input(' DIGITE OK [ para jogar ] = ')).upper()
    if sim == 'OK':
        print(' jogando dado  ......')
        tapa(dadoa)
        aba = randint(1 , 6)
        print(f' boa! numero do dado {aba}  ')
    else:
        break