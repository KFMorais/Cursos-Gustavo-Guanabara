'''
#for i, e in enumerate(minha_lista): ///um lembrete!!!
#sorted(lista) /// para ordenar uma lista
#tupla.index(itemaserlocalizado)  /// 
 
exemplo = ('bode', 'zebu', 'cavalo', 'poico')
tupla = (1, 3, 5, 7, 3) 
print(tupla[0]) 
print(tupla[1:3])
print(exemplo[0])

print(sorted(exemplo))
print(exemplo.index('cavalo'))
print(tupla.index(3)) ##### Atenção #####
print(tupla.index(3,2)) ##### Atenção 2 #####

#Variáveis compostas: tuplas, listas e discionários (conceito)

lanche = () - Tuplas
lanche = [] - Listas
lanche = {} - Dicionários

OBS: Lembrar que em fatiamento o ultimo elemento não é considerado 
Exemplo:
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1:3])
Vai imprimir não vai imprimir pudim

'''
#TUPLAS (Imutáveis)

#Linha de raciocínio 1

#lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

#print(lanche[-2:])
#lanche[1] = 'refrigerante' ====> Errado porque tuplas são imutáveis!!!

#for comida in lanche:
#    print(comida)

#for i in range(len(lanche)):
#    print(lanche[i])

#for e, i in enumerate(lanche):
#    print(i, e)

#print(sorted(lanche))

#Linha de raciocínio 2

#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = (b+a)
#print(c)
#print(len(c))
#print(c.count(5))
#print(c.index(4))
#print(c.index(5,1))                    # Novidade <=== Deslocamento

#Linha de raciocínio 3

#pessoa = ('Klewerton', 39, 'M', 100.88)
#print(pessoa)
#del(pessoa)                  # Novidade <=== uso de delete (del) - só pode deletar a tupla complete // não parcial
#print(pessoa)

'''
#LISTAS []
lanche = ['feijao', 'arroz']
#Inserção de item
lanche.insert(0,'batata')   #inserindo um item numa posição específica
                            #o append insere item no final, diferente o insert que eu posso escolher a
                            #posição da minha inserção
print(lanche)

#Exclusão de item
#por índice
lanche.pop(3) 
lanche.pop() 
dellanche[3]
#por conteúdo
lanche.remove('feijao') -- 1º ocorrência

#INTERESSANTÍSSIMO:
#Para fazer uma lista de números crescentes eu estava fazerndo um for e dando o comando append dentro dele...
#Posso fazer isso diretamente na variável
numeros = list(range(1,100))  #INTERESSANTÍSSIMO // #INTERESSANTÍSSIMO // #INTERESSANTÍSSIMO
print(numeros)

num = [2, 6, 4, 9]
num.sort()                #é assim que usa... antes do print da variável
print(num)
print(num.sort(reverse=True))


valores = [] #// valores - list()

valores.append(5)
valores.append(9)
valores.append(4)

for i, valor in enumerate(valores):
    print(f'O índice é {i} e o valor é {valor}...')
print('Cheguei ao final da lista')
'''

#INTERESSANTÍSSIMO // #INTERESSANTÍSSIMO // #INTERESSANTÍSSIMO
'''
a = [1, 2, 3 , 5, 6 ]
#b = a      # aqui faz uma vinculação com 'a'. SE ALTERAR 'b' altera 'a' TAMBÉM (ASSIM b[2] = 4)
b = a[:]    # aqui faz uma cópia de 'a'
b[2] = 4   
print(a)
print(b)


'''
# insert, pop, remove, sort, sort/reverse, del E COPIAR UMA LISTA

'''
teste = list()
teste.append('Klewerton')
teste.append('39')
print(teste)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

#galera = [['Maria', 19], ['Claudio', 60], ['Henzo', 4], ['Nicoly', 52]]
#print(galera[0][0])

#for w in galera:
#    print(w)

#for X in galera:
#    print(X[0])


#for h in galera:
#    print(f'{h[0]} tem {h[1]} anos de idade')

'''

galera = list()
dado = list()

for i in range(3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for j in galera:
    if j[1] >= 21:
        print(f'{j[0]} tem {j[1]} anos')
    else:
        print(f'{j[0]} tem menos de 21 anos de idade')
    
'''

#DICIONÁRIOS
# dados = {}
# dados = dict()
#chaves, valor e itens
#keys, values e items

#dados['DN'] = 'M'
#deldados['DN']


'''
pessoas = {
          'Nome': 'Klewerton',
          'Sexo': 'M',
          'Idade': 39
          }

'''
#pessoas['Peso'] = 48.5             ############## Lógica diferente!!! ##############
#pessoas['Nome'] = 'Roberto'
#del pessoas['Sexo']

#print(pessoas['Idade'])
#print(f'{pessoas['Nome']}')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#for i in pessoas.keys():
#    print(i)

#for j in pessoas.values():
#   print(j)

#for k, m in pessoas.items():
#   print(k, m)
'''
Brasil = []

estado1 = {'uf':'Rio de Janeiro','sigla':'RJ',}
estado2 = {'uf':'São Paulo','sigla':'SP',}

Brasil.append(estado1)
Brasil.append(estado2)


print(Brasil)


estado = dict()
brasil = list()
for i in range(3):
    estado['uf'] = input('Unidade Federativa ')
    estado['sigla'] = input('Sigla do Estado ') 
    brasil.append(estado.copy()) #INTERESSANTÍSSIMO // #INTERESSANTÍSSIMO // #INTERESSANTÍSSIMO
print(brasil)


produtos = {'feijão': 12, 
            'arroz': 4,
            'carne': 58,
            'cuzcuz': 2,
            'frios': 60
            }

print(produtos['feijão'])

print(produtos.items())

for i in produtos.items():
    print(i)
'''



dic_produtos = {'ipad': 7000, 
                'iphone': 5000, 
                'airpod': 2000,
                'macbook': 12000 
                } 




'''
produto_buscado = input('Digite o nome do produto: ').strip().lower()

if produto_buscado in dic_produtos:             ######## Lembrar que no 'in' não precisa de for... facilita
    print('Produto encontrado')
    preco = dic_produtos[produto_buscado]
    print(preco)
else:
    print('Produto não existente')


    
cont_estoque = input('digite um item que zerou o estoque: ')
dic_produtos.pop(cont_estoque)
print(dic_produtos)

                                                    ################### INTERESSANTE ##################
                                                    #     ESTRATÉGIA PARA TRATAMENTO DE ERRO ???      #                                                    
print(dic_produtos.get('macbook'))
print(dic_produtos.get('pão'))
print(dic_produtos.get('pão', 'Valor inexistente'))


#for i in dic_produtos: ## Padrão dicionário reconhece keys. Nesse caso é desnecessário colocar o .keys()
#    print(i)
#for j in dic_produtos.values():
#    print(j)
#for e, j in dic_produtos.items():
#    print(e, j)


turma = {}

for i in range(2):
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite o nota1 do aluno: '))
    nota2 = float(input('Digite o nota2 do aluno: '))
    turma[nome] = nota1, nota2

for i, j in turma.items():
    print(i, (j[0] + j[1])/2)


'''


pessoa = {
    'nome': 'Klewerton',
    'idade': 39,
    'profissão': 'Serv. Público',
    'interesses': ['Python', 'Programação', 'Notebooks'],
    'Pet': {
        'nome': 'Lunex',
        'idade': 10,
        'peso': 4
    }
}

#print(pessoa)

#print(pessoa.get('nome'))

#print(pessoa['interesses'][0])
#print(pessoa.get('interesses'))

#print(pessoa['Pet'])
#print(pessoa.get('Pet')['nome'])

#pessoa['nascimento'] = 1986

#print(pessoa)


'''
#Desafio 90

cadastro = {}

cadastro['nome'] = input('Nome: ')
cadastro['média'] = float(input('Média: '))
if 7 <= cadastro['média'] <= 10:
    cadastro['situação'] = 'Aprovado'
elif 5 <= cadastro['média'] < 7:
    cadastro['situação'] = 'Final'
elif 0 <= cadastro['média'] < 5:
    cadastro['situação'] = 'Reprovado' 
else:
    cadastro['situação'] = 'Valor inválido'

for i,j in cadastro.items():
    print(f'{i} é igual á {j}')

#Desafio 91

from random import randint
from operator import itemgetter
from time import sleep

start = input('Pressione "Enter"')

cadastro = {'jogador1': randint(1,6),
            'jogador2': randint(1,6),            
            'jogador3': randint(1,6),
            'jogador4': randint(1,6)
            }

print(cadastro)

print('Resultados Sorteados: ')
for i,j in cadastro.items():
    print(f'{i} tirou {j}')
    sleep(0.5)

ranking = ()
ranking = sorted(cadastro.items(), key=itemgetter(1), reverse=True) 
print(ranking)

print('Ranking dos Jogadores')
for k, l in enumerate(ranking):
    print(f'{k+1}º lugar: {l[0]} com {l[1]}.')

#Desafio 92

from datetime import date
ano = 2018#date.today().year

Segurado = {}

Segurado['Nome'] = input('Digite o nome do Segurado: ')
idade = int(input('Digire o ano de nascimento '))
Segurado['Idade'] = ano - idade

Segurado['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if Segurado['CTPS'] != 0:
    Segurado['Ano_Contratação'] = int(input('Ano de contratação: '))
    Segurado['Salário'] = float(input('Salário: R$ '))
    Segurado['Aposentadoria'] = (Segurado['Ano_Contratação'] + 35) - idade

print(Segurado)

for i, j in Segurado.items():
    print(f'{i} tem o valor {j}')

#Desafio 93

jogador = {}

jogador['Nome'] = input('Nome do Jogador: ')

partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou: '))
gols = []
soma = 0
for i in range(partidas):
    temp = int(input(f'Quantos gols na partida {i+1}? '))
    gols.append(temp)
    soma += temp
    
jogador['gols'] = gols
jogador['total'] = soma

print(f'-='*20) 
print(jogador)
print(partidas)
print(f'-='*20) 

for x, z in jogador.items():
    print(f'O campo {x} tem o valor {z}.')

print(f'O jogador {jogador['Nome']} jogou {partidas} partidas')

for k, t in enumerate(jogador['gols']):
    print(f'   ==> Na partida {k+1}, fez {t} gols.')
print(f'Foi um total de {jogador['total']} gols.')

#Desafio 94

cadastro = []
soma = 0
while True:
    temp = {}
    temp['nome'] = input('Nome: ')
    
    while True:
        temp['sexo'] = input('Sexo: [M/F] ').lower()[0]
        if temp['sexo'] in 'fm':
            break
        print('Erro! digite um valor válido')
    
    temp['idade'] = int(input('Idade: '))
    soma += temp['idade']
    cadastro.append(temp.copy())

    val = input('Quer continuar: [S/N] ').strip().lower()[0]
    while val not in 'sn':
        print('Erro! digite um valor válido')
        val = input('Quer continuar: [S/N] ').strip().lower()[0]
    if val == 'n':
        break
   
print(cadastro)

print(f'A) Foram cadastradas {len(cadastro)} pessoas')

media = soma/len(cadastro)
print(f'B) A média de idade do grupo é {media} anos')

acimamedia = []
print('C) As mulheres cadastradas foram:', end=' ')
for w in cadastro:
    if w['sexo'] == 'f':
        print(f'[{w['nome']}]', end=' ')
    if w['idade'] >= media:
        acimamedia.append(w)
        
print()

print(f'D) Lista das pessoas que estão acima da média:')
for y in acimamedia:
    for g,r in y.items():
        print(f'{g} = {r};', end=' ')
    print()

print('== Encerrando ==')

#Desafio 95

cadastro = []

while True:
    jogador = {}

    jogador['Nome'] = input('Nome do Jogador: ')

    partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou: '))
    gols = []
    soma = 0
    for i in range(partidas):
        temp = int(input(f'Quantos gols na partida {i+1}? '))
        gols.append(temp)
        soma += temp
        
    jogador['gols'] = gols
    jogador['total'] = soma

    cadastro.append(jogador)

    val = input('Deseja continuar? [S/N] ').lower()[0]
    while val not in 'sn':
        print('Erro! Digite um valor válido')
        val = input('Deseja continuar? [S/N] ').lower()[0]
    if val == 'n':
        break

print('-='*30)

print(f'{'cod':<3} {'nome':<20} {'gols':<20} {'total':<5}')
print('-'*51)

for w, z in enumerate(cadastro): 
    print(f'{w:>3}', end=' ')
    #for f, g in z.items():
        #print(f'{str(g):<20}', end=' ')

    for g in z.values():
        print(f'{str(g):<20}', end=' ')

    print()

print('-'*51)

while True:
    res = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if res == 999:
        break
    if res >= len(cadastro):
        print(f'Erro: Não existe jogador com o código {res}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {cadastro[res]['Nome']}:')
        for o, p in enumerate(cadastro[res]['gols']):
            print(f'No jogo {o+1} fez {p} gols.')

print('== Encerrando ==')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    soma = a+b
    print(f'A soma de A + B = {soma}')

soma(b=3, a=5)

def contador (*num):   ########################## aqui transforma em uma tupla. Assim trabalhamos como tal...
    for valor in num:
        print(valor)

contador(5, 7, 9, 11)

def dobra(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]*2
        
num = [2, 6, 16]
dobra(num)
print(num)

'''

#Interactive Help
    #help()
    #print(input.__doc__)
#Docstrings
    #Na prática
'''
from random import randint  
from time import sleep

def sorteia(opcao): 
    """
    1- Foi criada para estudo da aula 100. Serve para acrescentar 5 números aleatórios (de 0 a 10) numa lista
        
    """
    print('Sorteando 5 valores para a lista:', end=' ') 
    for i in range(5): 
        num = randint(1,10) 
        opcao.append(num) 
        print(num, end =' ', flush = True) 
        sleep(0.5) 
    print('PRONTO!')
   
        
def somapar(opcao):
    soma = 0
    for j in opcao:
        if j % 2 == 0:
            soma += j
    print(f'Somando os valores pares de {opcao}, temos {soma}')

#numeros = []   
#sorteia(numeros) 
#somapar(numeros) 

help(sorteia)
#Parâmetros opcionais
    #Na prática
def somar(a=0, b=0, c=0):  ### Poderia ser tb  def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
somar(3,5,3)
somar(1,3)
somar()

#Escopo de Variáveis
    #Na prática

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5
teste(a)
print(f'A fora vale {a}')

#Retorno de valores   ############### return ###############
    #Na prática

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

#resp = somar(3, 2, 5)
#print(resp)

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Resultados das somas: {r1}, {r2} e {r3}')

def par(num = 0):
    if num % 2 == 0:
        return True
    else:
        return False
    
n = int(input('Digite um número '))
if par(n):
    print('é par')
else:
    print('impar')


def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f*=c
    return f

num = int(input('Digite um valor '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
'''




#print(x)

#n = int(input('numero: '))
#print(f'Voce digitou o número {n}')

''' 

#Orientação Inicial#

try:
    a = int(input('Numerador: '))
    b = int(input('Deniminador: '))
    r = a/b
except:
    print('infelizmente tivemos um problema :(')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre!!!')

#Aprofundando#

try:
    a = int(input('Numerador: '))
    b = int(input('Deniminador: '))
    r = a/b
except Exception as erro: ###### Aqui a primeira diferença
    print(f'Problema encontrado foi {erro.__class__}') ###### Aqui a segunda diferença
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre!!!')

#Aprofundando2#

try:
    a = int(input('Numerador: '))
    b = int(input('Deniminador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Tivemos problema com os tipos de dados que voce informou')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre!!!')
'''



try:
    n = int(input('Digite um valor: '))
except ValueError:
    print('Erro: Digite um valor válido')
else:
    print(f'Voce digitou o valor {n}')

