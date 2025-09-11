from time import sleep
def maior(*max):  #vem como tupla
    print('-='*30)
    print('Analisando os valores passados...')
    maior = 0
    for e, i in enumerate(max):
        print(i, end=' ', flush=True)
        sleep(0.5)
        if e == 0 or i > maior:
            maior = i
    print(f'foram analisandos {len(max)} valores ao todo')

    print(f'O maior valor informado foi: {maior}')    


maior(2, 9 , 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
