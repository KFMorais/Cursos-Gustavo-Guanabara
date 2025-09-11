'''
import random

aluno1 = input('digite o nome do aluno: ')
aluno2 = input('digite o nome do aluno: ')
aluno3 = input('digite o nome do aluno: ')
aluno4 = input('digite o nome do aluno: ')

num = random.randint(1,4)
print(num)

if num == 1:
    print(aluno1)
elif num == 2:
    print(aluno2)
elif num == 3:
    print(aluno3)
elif num == 4:
    print(aluno4)


import random
alunos = list()

aluno1 = alunos.append(input('digite o nome do aluno: '))
aluno2 = alunos.append(input('digite o nome do aluno: '))
aluno3 = alunos.append(input('digite o nome do aluno: '))
aluno4 = alunos.append(input('digite o nome do aluno: '))

for i in range(4):
    alunos.append(input('digite o nome do aluno: '))

selecionado = random.randint(0,3)

print(selecionado)

print(alunos[selecionado])


import random
alunos = list()

for i in range(4):
    alunos.append(input('digite o nome do lavador: '))

selecionado = random.choice(alunos)

print(f'O Patrão será: {selecionado}')
'''
