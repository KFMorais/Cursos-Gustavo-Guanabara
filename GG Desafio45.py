import random
import os
from time import sleep

opcoes = ['Pedra', 'Papel', 'Tesoura']

print('''\033[7m
######     #      #####      ###   
    #     # #     #    #   #     # 
   #     #   #    ####    #       #
  #     # # # #   #    #  #       #
 #     #       #  #    #   #     # 
##### #         # #####      ###   
             
GAMES       ======>       APRESENTA                    \033[m''')
sleep(5)
os.system('cls')

print(f'''\033[31m{'  Jokenpô  ':#^40}\033[m

\033[33m{'## Pedra ':#<40}\033[m
\033[33m{'  Papel  ':#^40}\033[m
\033[33m{' Tesoura ##':#>40}\033[m
''')

sleep(1)

print(f''' Vamos Jogar!!!

        [1] {opcoes[0]}
        [2] {opcoes[1]}
        [3] {opcoes[2]}
''')

usuario = int(input('Escolha sua opção: ').strip())      
cpu = random.choice(opcoes)

print('Jo')
sleep(0.5)
print('ken')
sleep(0.5)
print('Pô')
sleep(0.5)
print('''
''')
if usuario == 1: #Pedra
    print (opcoes[usuario-1])
    print(cpu)
    if cpu == 'Pedra':
        print('Empate')    
    elif cpu == 'Papel':
        print('Perdeu')
    elif cpu == 'Tesoura':
        print('Ganhou')
elif usuario == 2: #Papel
    print (opcoes[usuario-1])
    print(cpu)
    if cpu == 'Pedra':
        print('Ganhou')    
    elif cpu == 'Papel':
        print('Empate')
    elif cpu == 'Tesoura':
        print('Perdeu')
elif usuario == 3: #Tesoura
    print (opcoes[usuario-1])
    print(cpu)
    if cpu == 'Pedra':
        print('Perdeu')    
    elif cpu == 'Papel':
        print('Ganhou')
    elif cpu == 'Tesoura':
        print('Empate')
else:
    print('opção inválida')
