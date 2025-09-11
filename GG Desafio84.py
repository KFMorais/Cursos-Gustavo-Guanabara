#Técnica 1

cadastro = list()
temp = []

while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    cadastro.append(temp[:])
    temp.clear()
    
    validacao = input('Quer continuar? [S/N] ').lower()
    if validacao in 'n':
        break

print(cadastro)

print(f'Ao todo foram cadastradas {len(cadastro)} pessoas')

menor = cadastro[0][1]
maior = cadastro[0][1]
for i in cadastro:
    if i[1] > maior:
        maior = i[1]
    if i[1] < menor:
        menor = i[1]

print(maior)
print(menor)

maiores = []
menores = []

for j in cadastro:
    if j[1] == maior:
        maiores.append(j[0])

for k in cadastro:
    if k[1] == menor:
        menores.append(k[0])

print(f'O maior peso foi de {maior} Kg. Peso de {maiores}')
print(f'O menor peso foi de {menor} Kg. Peso de {menores}')


'''
#Técnica 2

cadastro = list()
temp = []

while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    cadastro.append(temp[:])
    temp.clear()
    
    validacao = input('Quer continuar? [S/N] ').lower()
    if validacao in 'n':
        break

print(cadastro)

print(f'Ao todo foram cadastradas {len(cadastro)} pessoas')

menor = cadastro[0][1]
maior = cadastro[0][1]
for i in cadastro:
    if i[1] > maior:
        maior = i[1]
    if i[1] < menor:
        menor = i[1]

print(maior)
print(menor)

print(f'O maior peso foi de {maior} Kg. Peso de', end =' ')

for j in cadastro:
    if j[1] == maior:
        print(j[0], end=' ')
print()

print(f'O menor peso foi de {menor} Kg. Peso de', end =' ')

for k in cadastro:
    if k[1] == menor:
        print(k[0], end=' ')
print()

'''






