n1 = float(input('informe sua primeira nota: ').strip())
n2 = float(input('informe sua segunda nota: ').strip())

media = (n1 + n2)/2
print(f'{media:.1f}')

if media >= 7 and media <= 10:
    print('\033[32mAprovado\033[m')
elif media < 5:
    print('\033[31mReprovado\033[m')
elif 5 <= media < 7:
    print('\033[33mRecuperação\033[m')
else:
    print('\033[7mvalor inválido\033[m')