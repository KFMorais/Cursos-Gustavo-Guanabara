cadastro = {}

cadastro['Nome'] = input('Nome: ')
cadastro['Média'] = float(input(f'Média de {cadastro['Nome']}: '))
if cadastro['Média'] >= 7:
    cadastro['Situação'] = 'Aprovado'
elif 5 <= cadastro['Média'] < 7:
    cadastro['Situação'] = 'Recuperação'
else:
    cadastro['Situação'] = 'Reprovado'

#print(cadastro)

print('-='*20)

for e, i in cadastro.items():
    print(f'{e} é igual à {i}')

'''
cadastro = {}

cadastro['Nome'] = input('Nome: ')
cadastro['Média'] = float(input(f'Média de {cadastro['Nome']}: '))
print('-='*20)
print(f'   - Nome é igual a {cadastro['Nome']}')
print(f'   - Média é igual a {cadastro['Média']}')
if cadastro['Média'] >= 7:
    print('   - Situação é igual a Aprovado')
elif 5 <= cadastro['Média'] < 7:
    print('   - Situação é igual a Final')
else:
    print('   - Situação é igual a Reprovado')
print()
''' 
