from datetime import date
ano = 2018 #date.today().year

cadastro = {}

cadastro['Nome'] = input('Nome ')
cadastro['Idade'] = ano - int(input('Ano de Nascimento: '))
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de Contratação'] = int(input('Ano de Contratação: ')) 
    cadastro['Salário'] = float(input('Salário R$: '))
    cadastro['Aposentadoria'] = (35 - (ano - cadastro['Ano de Contratação'])) + cadastro['Idade']

#print(cadastro)

print('-='*40)
print()
for k, v in cadastro.items():
    print(f'     - {k} tem o valor {v}')
print()



