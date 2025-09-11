termo = int(input('informe o primeiro termo da PA: '))
razao = int(input('informe a razão da PA: '))

soma = termo
ciclo = 0

print(f'{soma}', end=', ')

limitador = 8

while True:
    while ciclo <= limitador:
        ciclo += 1
        soma = soma + razao
        if ciclo == limitador+1:
            print(f'{soma}')
        else:
            print(f'{soma}', end=', ')
    novo = int(input('quantos termos você quer a mais? '))
    if novo != 0:
        limitador += novo
    else:
        break

print(f'O {limitador+2}º termo da PA é: {soma}')