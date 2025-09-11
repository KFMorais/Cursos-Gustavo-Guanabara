'''
#Estratégia 1
def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols not in '12345678910':
        gols = 0    
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

#Programa Principal
ficha (input('Nome do Jogador: '), input('Numero de Gols: '))

#Estratégia 2
def ficha(nome='', gols=''):
    if nome.strip() == '':
        nome = '<desconhecido>'
      
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

#Programa Principal
print('-'*40)
n = input('Nome do Jogador: ')
g = input('Numero de Gols: ')
if g.isnumeric():
    int(g)
else:
    g = 0
ficha (n, g)
'''

#Estratégia 3

def ficha(nome='', gols=''):
    if nome.strip() == '':
        nome = '<desconhecido>'
    
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')



print('-'*40)
n = input('Digite o nome do Jogador: ')
g = input('Digite a quantidade de gols: ')
ficha(n, g)


