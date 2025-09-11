while True:
    entrada = int(input('Digite um número entre 0 e 20: '))
    while entrada > 20 or entrada < 0:
        entrada = int(input('Tente novamente. Digite um número entre 0 e 20: '))

    tupla = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove', 
            'dez', 'onze', 'doze', 'treze', 'quatorze', 
            'quinze', 'dezesseis', 'dezessete', 
            'dezoito', 'dezenove', 'vinte')

    print(f'Você digitou o número \033[7;31m{tupla[entrada]}\033[m')
    
    repetidor = input('Se desejar repetir o processo aperte "Enter", caso contrário, digite "-1": ')
    if repetidor == '-1':
        break
