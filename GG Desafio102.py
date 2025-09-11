def fatorial(num, show=False):
    """
Teste de Help
    
"""
    if show == False:
        cont = 1
        tot = num
        while cont < num:
            tot = tot * cont #5*1 = 5 // 5*2 = 10 // 10* 3 = 30 // 30 * 4 = 120
            cont += 1
        
        return f'''{'-'*50}
{tot}
        '''

    else:
        cont = 4
        tot = num
        print(f'''{'-'*50}
5 x''', end=' ')
        while cont > 0:
            if cont > 1: 
                print(f'{cont}', end =' x ')
            else:
                print(f'{cont}', end =' ')
            tot = tot * cont 
            cont -= 1
                
        return f'= {tot}'


#Programa Principal
print(fatorial(5, show = True))
help(fatorial)