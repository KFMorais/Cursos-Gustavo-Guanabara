lista = []
soma = 0

while True:
    cadastro = {}

    cadastro['Nome'] = input('Nome: ')
    Sexo = input('Sexo: [M/F] ').lower()[0]
    while Sexo not in 'mf':
        print('Erro! Responda apenas M ou F.')
        Sexo = input('Sexo: [M/F] ').lower()[0]
    cadastro['Sexo'] = Sexo
    cadastro['Idade'] = int(input('Idade: '))
    soma += cadastro['Idade']

    lista.append(cadastro)

    validador = input('Deseja continuar [S/N] ').lower()[0]
    while validador not in 'sn':
        print('Erro! Responda apenas S ou N.')
        validador = input('Deseja continuar [S/N] ').lower()[0]
    if validador == 'n':
          break

print('-='*40)

print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')

media = soma/len(lista)
print(f'B) A média de idade é de {media} anos.')

print(f'C) As mulheres cadastradas foram:', end=' ')
for i in lista:
    if i['Sexo'] == 'f':
          print(f'[{i['Nome']}]', end=' ')
print()



print(f'D) Lista das pessoas que estão acima da média: ')
for j in lista:
    if j['Idade'] >= media:
        for k, p in j.items():
            print(f'{k} = {p};', end=' ')     
        print()

print('<<< ENCERRANDO >>>')


"""

for k in range(qtdp):
    if principal['Final'][k]['Idade'] > media:
        for z, g in principal['Final'][k].items():
            print(f'{z} = {g}',end='; ')
        print()






"""













'''


lista = []

while True:
    cadastro = {}

    cadastro['Nome'] = input('Nome: ')
    Sexo = input('Sexo: [M/F] ').lower()
    while Sexo != 'm' and Sexo != 'f': 
        print('Erro! Responda apenas M ou F.')
        Sexo = input('Sexo: [M/F] ').lower()
    cadastro['Sexo'] = Sexo
    cadastro['Idade'] = int(input('Idade: '))

    lista.append(cadastro)

    validador = input('Deseja continuar [S/N] ').lower()
    while validador != 's' and validador != 'n':
        print('Erro! Responda apenas S ou N.')
        validador = input('Deseja continuar [S/N] ').lower()
    if validador == 'n':
          break

principal = {'Final':lista}
print(principal)

print('-='*40)

qtdp = len(principal["Final"])
print(f'A) Ao todo temos {qtdp} pessoas cadastradas.')

soma = 0
for i in range(qtdp):
    soma += principal['Final'][i]['Idade']
media = soma/qtdp
print(f'B) A média de idade é de {media} anos.')

print(f'C) As mulheres cadastradas foram:',end=' ')
for j in range(qtdp):
    if principal['Final'][j]['Sexo'] == 'f':
        print(f'[{principal['Final'][j]['Nome']}]',end=' ')
print()

print(f'D) Lista das pessoas que estão acima da média: ')
for k in range(qtdp):
    if principal['Final'][k]['Idade'] > media:
        for z, g in principal['Final'][k].items():
            print(f'{z} = {g}',end='; ')
        print()
print('<<< ENCERRANDO >>>')





'''