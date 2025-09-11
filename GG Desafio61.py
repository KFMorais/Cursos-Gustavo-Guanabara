termo = int(input('informe o primeiro termo da PA: '))
razao = int(input('informe a razão da PA: '))

soma = termo
ciclo = 0

print(f'{soma}', end=', ')

while ciclo != 9:
    ciclo += 1
    soma = soma + razao
    if ciclo == 9:
        print(f'{soma}')
    else:
        print(f'{soma}', end=', ')

print(f'O décimo termo da PA é: {soma}')