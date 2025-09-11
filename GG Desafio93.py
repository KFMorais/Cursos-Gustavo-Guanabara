cadastro = dict()

cadastro['nome'] = input('Nome do Jogador: ')

gols = int(input(f'Quantas partidas {cadastro['nome']} jogou? '))

n = []
soma = 0
for i in range(gols):
    temp = int(input(f'Quantos gols na partida {i}? '))
    soma += temp
    n.append(temp)
cadastro['gols'] = n
cadastro['total'] = soma
print('-='*30)
print(cadastro)
print('-='*30)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {cadastro['nome']} jogou {gols} partidas.')

for x, z in enumerate(cadastro['gols']):
    print(f'   => Na partida {x}, fez {z} gols.')
print(f'Foi um total de {cadastro['total']} gols.')
print('-='*30)
