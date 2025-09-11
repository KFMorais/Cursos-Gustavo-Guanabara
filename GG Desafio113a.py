#Desafio criado pelo Gemini
'''
#Desafio 1

def leia_real(txt):
    while True:
        try:
            n = float(input(txt)) 
        except ValueError:
            print('ERRO: Digite um número válido !!!')
        else:
            return n


#Programa Principal

a = leia_real('Digite o primeiro número: ')
b = leia_real('Digite o segundo número: ')
print(a+b)
'''
'''
#Desafio 2

def leia_real(txt):
    while True:
        try:
            n = float(input(txt)) 
        except ValueError:
            print('ERRO: Digite um número válido !!!')
        else:
            return n

def operacao(Do, dr):
    while True:
'''
#        print('''Operações disponíveis
#        1- Adição
#        2- Subtração
#        3- Multiplicação
#        4- Divisão''')
'''
        while True:
            try:
                opcao = int(input('Digite o número correspondente a operação desejada: '))
            except ValueError:
                print('Eita!!! Você não digitou um número válido. Tenta novamente.')
                continue
            else:
                break
        if opcao == 1:
            return f'O resultado da soma de {Do} + {dr} é {Do + dr}'
        elif opcao == 2:
            return f'O resultado da subtração de {Do} - {dr} é {Do - dr}'
        elif opcao == 3:
            return f'O resultado da multiplicação de {Do} x {dr} é {Do * dr}'
        elif opcao == 4:
            try:
                d = Do/dr
            except ZeroDivisionError:
                return 'ERRO: Não é possível dividir um número por zero.'
            else:
                return f'O resultado da divisão de {Do} por {dr} é {d}'
        else:
            print('Ops! Você digitou uma opção que não existe no menu. Tente novamente.')
        
#Programa Principal

a = leia_real('Digite o primeiro número: ')
b = leia_real('Digite o segundo número: ')

resultado = operacao(a , b)
print(resultado)
'''
'''
#Desafio 3

def leia_real(txt):
    while True:
        try:
            n = float(input(txt)) 
        except ValueError:
            print('ERRO: Digite um número válido !!!')
            continue
        else:
            return n

def calc_segura():
    while True:
'''
#        print(f'''{'='*30}
#{'CALCULADORA SEGURA':^30}
#{'='*30}
#Operações disponíveis
#        1- Adição
#        2- Subtração
#        3- Multiplicação
#        4- Divisão
#        5- Sair do programa
#{'='*30} ''')
'''
        while True:
            try:
                opcao = int(input('Digite o número correspondente a operação desejada: '))
            except ValueError:
                print('Eita!!! Você não digitou um número válido. Tenta novamente.')
                continue
            else:
                if opcao > 5 or opcao < 1:
                    print('Ops! Você digitou uma opção que não existe no menu. Tente novamente.')
                    continue
                elif opcao == 5:
                    return 'Volte sempre a função Calculadora Segura'
                break
        
        n1 = leia_real('Digite o primeiro número: ')
        n2 = leia_real('Digite o segundo número: ')

        if opcao == 1:
            print(f'O resultado da soma de {n1} + {n2} é {n1 + n2}')
        elif opcao == 2:
            print(f'O resultado da subtração de {n1} - {n2} é {n1 - n2}')
        elif opcao == 3:
            print(f'O resultado da multiplicação de {n1} x {n2} é {n1 * n2}')
        elif opcao == 4:
            try:
                d = n1/n2
            except ZeroDivisionError:
                print('ERRO: Não é possível dividir um número por zero.')
            else:
                print(f'O resultado da divisão de {n1} por {n2} é {d}')
           
        
#Programa Principal

print(calc_segura())

'''

#Desafio 4

class idadeInvalidaError(Exception):
    pass

def leia_idade():
    i = int(input('digite uma idade válida: '))
    if i <= 0:
        raise idadeInvalidaError('A idade deve ser um número positivo.')
    else:
        return i
        

#Programa Principal
while True:
    try: 
        a = leia_idade()
        print(f'Idade registrada com sucesso: {a}')
        break

    except ValueError:
        print("ERRO: O valor digitado não é um número inteiro.")

    except idadeInvalidaError as e:
        print(f"ERRO de validação: {e}")
