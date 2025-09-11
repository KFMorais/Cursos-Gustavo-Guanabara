from random import randint
from time import sleep

cores = {
'limpa':'\033[m', 
'vermelho':'\033[1;31;43m',
'amarelo':'\033[1;33m',
'famarelo':'\033[43m',
'azul':'\033[1;34m',
'verde':'\033[1;32m'
}

print(f'Olá, vamos brincar de advinhação?? :)')
sleep(2)
print(f'Tente advinhar o número escolhido pelo computador. {cores['vermelho']}Atencão: Este número será entre 0 a 5{cores['limpa']}')
sleep(2)
CPU = randint(0,5)
usuario = int(input('Digite o número escolhido: ').strip())

print(f'Será que você acertou???') 
sleep(2)
print(f'{cores['famarelo']}O Computador escolheu o número{cores['limpa']} {cores["vermelho"]}({CPU}){cores['limpa']}')
sleep(1)
if(usuario == CPU):
    print(f'{cores['verde']}Acertou!!!{cores['limpa']}')
else:
    print(f'{cores["vermelho"]}Errou, tente novamente!!!{cores['limpa']}')

#jngidjfitdutidiggkgjgjdkdlodoeijrjdfkjkgfjfktufofijhijijgfigift
