num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um valor: ')))
    temp = input('Deseja continuar? [S/N] ').strip().lower()
    if temp in 'n':
        break

print('''

      ''')

print(f'Os números digitados foram: {num}')

for n in num:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Os números pares da lista são: {pares}')
print(f'Os números impares da lista são: {impares}')