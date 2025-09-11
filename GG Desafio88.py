#Técnica 1
from random import choice
from time import sleep

num = []
for i in range(1,61):
    num.append(i)

final = []
temp = list()
qnt = int(input('Informe a quantidade de jogos que vc deseja '))

for j in range(qnt):
    for k in range(6): 
        sort = choice(num)
        if len(temp) == 0:
            temp.append(sort)
        else:       
            while True:
                for l in range(len(temp)):
                    if sort == temp[l]:
                        sort = choice(num)
                        l = 0
                break
            temp.append(sort)
    final.append(temp[:])
    temp.clear()

print('=-='*20)
print(f'Os {qnt} jogos sorteados foram:')

for e, z in enumerate(final):
    final[e].sort()
    print(f'Jogo {e+1}: {final[e]}')
    sleep(1)

print('=-='*20)
'''

#Técnica 2
from random import choice
from time import sleep

num = []
for i in range(1,61):
    num.append(i)



final = []
temp = list()

qnt = int(input('Informe a quantidade de jogos que vc deseja '))
for j in range(qnt):
    for k in range(6):
        sort = choice(num)
        if sort != temp:
            temp.append(sort)
    final.append(temp[:])
    temp.clear()

print(final)    


'''
'''

            while sort == l:
                        
            for l in temp:
                if sort == l:

                while sort == l:
                    sort = choice(num)



        
        for k in range(len)
        
        
        while sort in temp:
            sort = choice(num)




        temp.append(sort)
    final.append(temp[:])
    temp.clear()

print(final)    
'''