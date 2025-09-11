print('Sequencia de Fibonacci')
print('=' * 47)
n = int(input('informe a quantidade da sequencia de Fibonacci: ').strip())
print('=' * 47)

item1= 0  #O correto é 1 más GG usou 0 com primeiro termo!!!
item2= 1 
print(item1, end=', ')
print(item2, end=', ')

ciclos = 2
while ciclos != n:
    ciclos += 1
    subsequente = item1 + item2 
    if ciclos == n:
         print(subsequente, end=' => ')
    else:
        print(subsequente, end=', ')
    item1 = item2 
    item2 = subsequente 
print('fim')

    