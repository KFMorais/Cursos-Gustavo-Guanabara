bd = []

while True:
    temp = int(input('Digite um valor: '))
    if temp not in bd:
        bd.append(temp)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    validacao = input('Quer continuar? [S/N] ').lower()
    if 'n' in validacao:
        break

print('=-='*30)
print(f'Você digitou os valores {bd}')
bd.sort()                                                   
print(f'Segue os números colocados em ordem 1 {bd}')
print(f'Segue os números colocados em ordem 2 {sorted(bd)}')


    
