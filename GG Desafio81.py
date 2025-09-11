num = []

while True:
    num.append(int(input('Digite um valor: ')))
    temp = input('Quer continuar: [S/N]? ').lower()
    if 'n' in temp:
        break

print('=-='*30)

print(f'Você digitou {len(num)} elementos.')

num.sort(reverse=True)
print(f'{num}')

if 5 in num:
    print('O valor 5 faz parte da lista e está nas posições: ', end='')
    for e, pos in enumerate(num):
        if pos == 5:
            print(e, end=' ')
    print()
else:
    print('O valor 5 não foi encontrado na lista')
