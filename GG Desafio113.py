def leiaint():
    while True:
        try:
            inteiro = int(input('Digite um inteiro: '))
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número')
            return 0
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número INTEIRO válido.')
        else:
            return inteiro

def leiafloat():
    while True:
        try:
            real = float(input('Digite um Real: '))
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número')
            return 0
        except:
            print('ERRO: por favor, digite um número REAL válido.')
        else:
            return real


#Programa Principal
print(f'O valor inteiro digitado foi {leiaint()} e o real foi {leiafloat()}')