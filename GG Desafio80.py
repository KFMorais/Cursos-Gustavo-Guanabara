num = list()
num.append(int(input('Digite um valor: ')))
print('Adicionado ao final da lista...')

for i in range(4):
    temp = int(input('Digite um valor: '))
    posicao = 0
    if temp > num[(len(num))-1]:
        num.append(temp)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while num[posicao] < temp:
            posicao += 1
        num.insert(posicao, temp)
        print(f'Adicionado na posição {posicao}')

print(f'Os valores digitados em ordem foram {num}')







'''
num = list()

for i in range(5):
    temp = int(input('Digite um valor: '))
    if i == 0:
        num.append(temp)

    elif i == 1:
        if temp > num[0]:
            num.append(temp)
        else:
            num.insert(0, temp)
    elif i >= 2:        
        posicao = 0
        while temp > num[posicao]:
            posicao += 1
        if posicao+1 >= len(num):
            num.append(temp)
        else:
            num.insert(posicao, temp)
'''

'''
    elif i == 1:
        if temp > num[0]:
            num.append(temp)
        else:
            num.insert(0, temp)

    else:
        posicao = 0
        while temp > num[posicao]:
            posicao +=1
        num.insert(posicao, temp)            

print(num)
'''

'''
num = list()

for i in range(5):
    temp = int(input('Digite um valor: '))
    if i == 0:
        num.append(temp)
    elif i == 1:
        if temp > num[0]:
            num.append(temp)
        else:
            num.insert(0, temp)

    else:
        posicao = 0
        while temp > num[posicao]:
            posicao +=1
        num.insert(posicao, temp)            

print(num)
'''