from random import randint
from time import sleep

from operator import itemgetter    ########### Novidade ###########
ranking = list()  ###

star = input()
cadastro = {'Jogador 1':randint(1,6),               
            'Jogador 2':randint(1,6), 
            'Jogador 3':randint(1,6), 
            'Jogador 4':randint(1,6),          
            }

print('Valores sorteados:')    
print()
for c, v in cadastro.items():
    sleep(0.5)
    print(f'    O {c} tirou {v}')
print()

####################################################################################################

ranking = sorted(cadastro.items(), key=itemgetter(1), reverse=True) ########### Novidade ###########

#print(ranking)                              ########### Gera uma lista ###########

print('Melhores resultados em ordem decrescente')
print()
classificacao = 1
for z in ranking:
    print(f'{classificacao}º lugar: {z[0]} com {z[1]}.')
    classificacao += 1
print()
