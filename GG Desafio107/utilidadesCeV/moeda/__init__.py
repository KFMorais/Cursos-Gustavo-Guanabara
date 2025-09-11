def aumentar(num, q, m=True): 
    '''
    Função que serve para acrescentar um percentual ao principal
    parâmetro num: recebe um número real a ser informado pelo usuário
    parâmetro q: percentual a ser acrescido
    retorna o valor principal acrescido do percentual informado 
    '''
    if m == True:
        return moeda(num + num*q/100)
    else:
        return num + num*q/100

def diminuir(num, q, m=True): 
    '''
    Função que serve para diminuir um percentual do principal
    parâmetro num: recebe um número real a ser informado pelo usuário
    parâmetro q: percentual a ser reduzido
    retorna o valor principal reduzido do percentual informado
    '''
    if m == True:
        return moeda(num - num*q/100)
    else:
        return num - num*q/100

def dobro(num, m=True):
    '''
    Função que serve para dobrar um valor informado
    parâmetro num: recebe um número real a ser informado pelo usuário
    retorna o dobro do valor informado
    '''
    if m == True:
        return moeda(num*2)
    else: 
        return num*2

def metade(num, m=True):
    '''
    Função que serve para gerar a metade de um valor informado
    parâmetro num: recebe um número real a ser informado pelo usuário
    retorna a metade do valor informado
    '''
    if m == True:
        return moeda(num/2)
    else:
        return num/2

def moeda(valor):
    '''
    Função que serve para 
    parâmetro valor: 
    retorna 
    '''
    return f'R$ {valor:.2f}'.replace('.',',')

def resumo(num=0,a=10,d=5):
    '''
    a = percentual a ser adicionado
    d = percentual a ser reduzido
    '''
    return print(f'''
{'-'*30}
{'RESUMO DO VALOR'.center(30)}
{'-'*30}
{'Preço analisado:':<18} {moeda(num)}
{'Dobro do preço:':<18} {dobro(num,True)}
{'Metade do preço:':<18} {metade(num,True)}
{f'{a}% de aumento:':<18} {aumentar(num,a,True)}
{f'{d}% de redução:'}\t{diminuir(num,d,True)}     #Deixei a tabulação no projeto para lembrar dessa estratégia de formatação
{'-'*30}
''')


