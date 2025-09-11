cores = {
'limpa':'\033[m',
'azul':'\033[1;34m',
'amarelo':'\033[1;33m',
'vermelho':'\033[1;31m',
'verde':'\033[1;32m'
}
n = int(input('informe um número: ').strip())
soma = 0
for i in range(1, n+1):
    if n % i == 0:
        soma += 1
        print(f'{cores['verde']}{i}{cores['limpa']}', end=' ')
    elif n % i != 0:
        print(f'{cores['vermelho']}{i}{cores['limpa']}', end=' ')
if soma == 2:
    print(f'\nO número {n} é divisível por {soma} números, por isso ele é primo')
else:
    print(f'\nO número {n} é divisível por {soma} números, por isso ele \033[31mNÃO\033[m é primo')

'''
n = int(input('informe um número: ').strip())
soma = 0
for i in range(1, n+1):
    if n % i == 0:
        soma += 1
if soma == 2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} \033[31mNÃO\033[m é primo')
'''