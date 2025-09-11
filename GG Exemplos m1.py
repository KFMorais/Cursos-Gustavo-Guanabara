'''
nome = input("digite seu nome: ")
sobrenome = input("digite seu nome: ")

print(f'Seu nome é: {nome:=^20}!', end =' ### ')
print(f'Seu nome é: {nome:=^20}!')
print(f'Seu nome é: {nome:<20}!')
print(f'Seu nome é: {nome:^20}!')
print(f'Seu nome é: {nome:>20}!')
print(f'Seu nome é: {nome:^20}\ne sobrenome {sobrenome}!')


#print (nome.istitle()) - primeira letra maiuscula
    #OBS: capitalize ... numa frase só vale p primeira palavra
#print (nome.isupper()) - tudo maiusculo
#print (nome.islower()) - tudo minusculo
#print (nome.isalnum())
#print(nome.isalpha())
#print(nome.isnumeric())
#Ordem de Precedência: () ** * / // % + - 

#pow (2,2) = 2 ao quadrado
#\n e end = ''
'''

######## Bibliotecas ########

#import math
#from math import ceil
#from math import ceil, floor

### math ###
#ceil, arredonda para cima
#floor, arredonda para baixo
#sqrt, raiz quadrada
#trunc, deixa apenas o número inteiro
#pow, exponenciação
#factorial, fatorial
#etc, entre outas
'''
import math

num = int(input('digite um número: '))

raiz = math.sqrt(num)
raiz2 = int(num**(1/2))
print(math.ceil(raiz))
print(raiz2)

from math import sqrt, floor

entrada = int(input('digite um valor: '))

raiz = sqrt(entrada)

print(floor(raiz))

import random

#num = random.random()
num = random.randint(1, 10)

print(num)

import emoji
print(emoji.emojize('Ola :pile_of_poo:'))
'''

#Fatiamento
''''
print(frase[9]) #indice
print(frase[9:13]) #o ultimo não entra
print(frase[9:21:2]) #pulando de 2 em 2
print(frase[:5]) #do 0 ao 5
print(frase[15:]) #do 15 até o final
'''
#Análise find() e count()
'''
print(len(frase)) #len(variável)
print(frase.count('o')) #O.count('iten a ser contado')                                          ###### interessante
print(frase.count('o', 0, 13)) #mesma lógica da situação anterior porém limitado a um intervalo ###### interessante
print(frase.upper().count('O')) #combinação de ideias

print(frase.find('deo'))                                                                        ###### interessante
print(frase.find('Android'))                                                                    ###### interessante
teste = 'Curso' in frase                                                                        ###### interessante
print(teste)
'''
#Transformação replace() strip()
'''
print(frase.replace('Python', 'Android'))                                                       ###### interessante
print(frase)

strip = '   aprenda python   '

print(strip.strip())                                                                            ###### interessante
print(strip.rstrip())                                                                           ###### interessante
print(strip.lstrip())                                                                           ###### interessante
'''
#Divisão split() 
'''
print(frase.split())                                                                            ###### interessante
'''
#Junção '-'.join()
'''
print('-'.join(frase.split()))                                                                  ###### interessante
'''

##################################################################################################################

#Resumo:
#Fatiamento: XXX
#Transformação: .strip() .replace()
#Análise: '' in variável  .find() .count()
#Divisão: .split()
#Junção: ''.join(variável)

##################################################################################################################
'''
frase = "Curso em Video Python"

print(frase)

print(' '.join(frase)) # junta o que esta dentro de '' a variável

print(frase.find('Vi'))
print(frase.count('P'))

nome = '99'

novo = ('00'.join(nome))

print(novo)
##################################################################################################################

# \033[ ;  ;  m

#Style 0 1 4 7
#Text 30 31 32 33 34 35 36 37
#Back 40 41 42 43 44 45 46 47

nome = 'Klewerton Morais'
#Dicionário
cores = {
    'limpa': '\033[m', 
    'azul': '\033[34m',
    'preto': '\033[7;40m'
}

print(f'Muito prazer {cores['preto']}{nome}{cores['limpa']} !!!')

print(f'Muito prazer \033[35m{nome}\033[m !!!')

#print('''#\033[4;32;43mMenu\033[m'''
#\033[4;32m1) Cadastro
#\033[4;32m2) Visualização
#\033[4;32m3) Excluir\033[m
#      ''')
#valorescolhido = input('\033[4;35mEscolha uma das opções: ')

#ATENÇÃO:

#lista = ['a', 'b', 'c']
#print(*lista,sep='')