from random import shuffle

alunos = list()

for i in range (4):
    alunos.append(input('digite o nome do aluno: '))

shuffle(alunos)

print(alunos)








'''
import random

opcoes = ['Pedra', 'Papel', 'Tesoura']
pontosu = 0
pontosc = 0

for i in range(3):
    usuario = (input('digite sua escolha (pedra, papel ou tesoura): ')).capitalize()
    cpu = random.choice(opcoes)
    print(cpu)
    if(usuario == opcoes[0]):
        if (cpu == opcoes[2]):
            print('Venceu!')
            pontosu += 1
        elif (cpu == opcoes[1]):
            print('Perdeu!')
            pontosc += 1
        elif (cpu == opcoes[0]):
            print('Empate!')
            pontosc = 0
    if(usuario == opcoes[1]):
        if (cpu == opcoes[0]):
            print('Venceu!')
            pontosu += 1
        elif (cpu == opcoes[2]):
            print('Perdeu!')
            pontosc = 0
        elif (cpu == opcoes[1]):
            print('Empate!')
    if(usuario == opcoes[2]):
        if (cpu == opcoes[1]):
            print('Venceu!')
            pontosu += 1
        elif (cpu == opcoes[0]):
            print('Perdeu!')
            pontosc = 0
        elif (cpu == opcoes[2]):
            print('Empate!')

if (pontosu > pontosc):
    print('Parabéns, você venceu a disputa')
elif (pontosu < pontosc):
    print('Deu Águia!!!')
elif (pontosu == pontosc):
    print('Emparou, tenta novamente!!!')
'''