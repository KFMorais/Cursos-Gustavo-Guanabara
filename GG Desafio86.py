#Técnica 1
matriz = [[],[],[]]

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

for z in matriz:
    for x in z:
        print(f'[{x:^5}]', end=' ')
    print()
    

'''

#Técnica 2

matriz = [[],[],[]]

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

for z in matriz:
    print(z)


'''