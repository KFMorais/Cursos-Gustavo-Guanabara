from random import randint   ###########
from time import sleep



def sorteia(opcao):  ## ATENÇÃO ##
    '''
    1- Foi criada para estudo da aula 100. Serve para acrescentar 5 números aleatórios (de 0 a 10) numa lista
        
    '''
    
    
    print('Sorteando 5 valores para a lista:', end=' ') ###########
    for i in range(5): ###########
        num = randint(1,10) ###########
        opcao.append(num) ## ATENÇÃO ##
        print(num, end =' ', flush = True) ###########
        sleep(0.5) ###########
    print('PRONTO!')
    
        
def somapar(opcao):
    soma = 0
    for j in opcao:
        if j % 2 == 0:
            soma += j
    print(f'Somando os valores pares de {opcao}, temos {soma}')




numeros = []   ###########
sorteia(numeros) ## ATENÇÃO ##
somapar(numeros) ## ATENÇÃO ##

help(sorteia)

#Programa principal