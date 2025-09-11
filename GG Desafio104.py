def leiaint(txt):   
    num = input(txt)
    while num.isnumeric() == False:
        print('\033[0;31m Erro, digite um número inteiro: \033[m')
        num = input(txt)
    
    return int(num)


#Programa Principal
print('-'*60)
x = leiaint('Digite o valor de Zabo: ')
print(f'O número {x} é valido e está no formato {type(x)}')

