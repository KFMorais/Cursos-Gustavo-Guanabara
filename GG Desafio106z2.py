from time import sleep

cores = (
'\033[m',  #limpa  / 0
'\033[0;30;44m', #azul / 1 
'\033[0;30;43m', #amarelo / 2
'\033[0;30;41m', #vermelho / 3
'\033[0;30;42m', #verde / 4
'\033[7;30m'  #branco  / 5
)


def formatacao(msn, cor=0):
    tam = len(msn)+4
    print(cores[cor],end='')
    print('~'*tam)
    print(f'  {msn}  ')
    print('~'*tam)
    print(cores[0])
    sleep(0.5)


def ajuda(com):
    formatacao(f"Carregando manual de '{com}'", 1)
    sleep(0.5)
    print(cores[5],end='')
    help(com)
    print(cores[0])
    sleep(2.5)


#Programa Principal
while True:
    formatacao('Sistema de Ajuda PyHELP',2)
    aj = input('Função ou Biblioteca: ').strip().lower()
    if aj == 'fim':
        break
    else:
        ajuda(aj)
formatacao('Volte Sempre...',3)
