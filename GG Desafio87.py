matriz = [[],[],[]]

maior = -99999999999999999999999
soma3c = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if j == 2:
            soma3c += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]

somap = 0
for z in matriz:
    for x in z:
        print(f'[{x:^5}]', end=' ')
        if x % 2 == 0:
            somap += x
    print()

print(f'A soma dos valores pares é {somap}')

print(f'A soma dos valores da terceira coluna é {soma3c}.')

print(f'O maior valor da segunda linha é {maior}.')