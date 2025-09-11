#Questões Youtube (https://www.youtube.com/watch?v=VED_gsUu7S4)
'''
#Questão 1

def adicao(item):
    soma = 0
    for i in item:
        soma += i
    return soma

num = [9, 19, 23, 36, 51]
print(adicao(num))

#Questão 2

def multiplicar(item):
    multi = 1
    for i in item:
        multi *= i
    return multi

num = [4, 19, 23, 36, 51]
print(multiplicar(num))

#Questão 3
#Estratégia 1 (não foi isso o solicitado na questão más deixei pq achei interessante a forma de minha resolução)

def ranger(n, i):
    valor = False
    for i in range(0, n+1, i):
        if i == n:
            valor = True
    return valor


print(ranger(15, 5))

#Questão 3
#Estratégia 2

def ranger(n, i):
    if n in list(i):  #colocando range(1,10) dentro de list(range(1,10)) faz uma lista de numeros de 1 a 9
        return True
    else:
        return False


print(ranger(2, range(1,10)))
print(ranger(32, range(1,10)))

#Questão 4
#Estratégia 1

def palindromo(palin):
    ind = len(palin)-1
    for i in palin:
        if i != palin[ind]:
            return 'Não é palindromo'
        ind-= 1
    return 'Palindromo'
    
        
print(palindromo('arara'))
    
#Questão 4
#Estratégia 2

def testar_palindromo(palavra):
    if palavra == palavra[::-1]:   #Dica 2: aqui eu consigo inverter a ordem da string
        return True
    else:
        return False

test1 = 'arara'
test2 = 'casa'

if testar_palindromo(test1):
    print(f'A palavra é um palindromo')
else:
    print(f'A palavra não é um palindromo')

if testar_palindromo(test2):
    print(f'A palavra é um palindromo')
else:
    print(f'A palavra não é um palindromo')


#Questão 5
#Estratégia 1

def somar_numeros(*n):
    soma = 0
    for i in n:
        soma += i
    return soma

print(somar_numeros(4, 19, 23, 36, 51))
        
#Questão 5
#Estratégia 2

def somar_numeros(n):
    soma = 0
    for i in n:
        soma += i
    return soma

num = [4, 19, 23, 36, 51]
print(somar_numeros(num))

#Questão 5
#Estratégia 3

def somar_numeros(*n):
    return sum(n)

num = [4, 19, 23, 36, 51]
print(somar_numeros(*num))

#Questão 6

def mult_num(*n):
    total = 1
    for i in n:
        total*= i
    return total

print(mult_num(5, 4, 3))

#Questão 7

def dados_pessoais(**disc):
    for i in disc.keys():
        if i in ('nome', 'sobrenome', 'idade'):
            print(f'{i}: {disc[i]}')
    print('Finalizou...')

dados_pessoais(nome='Klewerton', sobrenome='Figueiredo Morais', idade=39, profissão='serv publico')
dados_pessoais(nome='Klewerton', sobrenome='Figueiredo Morais', idade=39)
dados_pessoais()

'''