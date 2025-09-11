from random import randint
from time import sleep
import os

cont = 0
while True:
    op_jogador = str(input('Par ou Impar? ').strip().upper()[0])
    while op_jogador not in 'PI':                                           #validação das opções par ou impar
        op_jogador = str(input('Opção inválida. Escolha entre Par ou Impar? ').strip().upper()[0])
    os.system('cls')
    if op_jogador == 'P':
        print('''Jogador escolheu a opção Par
CPU fica com a opção Impar''')
    else:
        print('''Jogador escolheu a opção Impar
CPU fica com a opção Par''')
    sleep(2)
    print()
    for i in range (3,0,-1):
        print(f'{i}...')
        sleep(1)
    print('Já...')
    print()
    cpu = randint(0,10)
    Jogador = int(input('digite um número: ').strip())
    print(f'O CPU escolheu o número {cpu}')
    soma = cpu + Jogador
    if soma % 2 == 0: #identificando se a soma dos números informados é par
        analise = 'P'        
    else:
        analise = 'I'    
    if analise == op_jogador:
        print('Jogador Venceu!!!')
    else:
        print('Jogador Perdeu!!!')
        break
    cont += 1
    sleep(2)
    print('Vamos para a próxima rodada')
    sleep(2)
    os.system('cls')

print('Se quiser jogar novamente, reinicie o jogo!!!')
if cont == 1: 
    print(f'Voce venceu {cont} partida')
else:
    print(f'Voce venceu {cont} partidas consecutivas')
    