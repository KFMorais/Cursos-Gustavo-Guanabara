from random import randint
cpu = randint(0,10)
#print(cpu)
usuario = int(input('digite um número, entre 0 e 10, que vc acha que foi o escolhido pelo computador: ').strip())
tentativas = 1

'''
while usuario != cpu:
    usuario = int(input('Errou, tente novamente: ').strip())
    tentativas +=1
'''

while usuario != cpu:
    if usuario < cpu:
        usuario = int(input('Errou, tente novamente (escolha um número maior): ').strip())
    elif usuario > cpu:
        usuario = int(input('Errou, tente novamente (escolha um número menor): ').strip())

    tentativas +=1

print(f'O Computador escolhou o número {cpu}')
if tentativas == 1:
    print('Acertou!!! Vc conseguiu de primeira!!!')
else:
    print(f'Acertou!!! Vc precisou de {tentativas} tentativas')
