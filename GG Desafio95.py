jogadores = []
cadastro = dict()

while True:
    cadastro['nome'] = input('Nome do Jogador: ')

    gols = int(input(f'Quantas partidas {cadastro['nome']} jogou? '))

    n = []
    soma = 0
    for i in range(gols):
        temp = int(input(f'     Quantos gols na partida {i+1}? '))
        soma += temp
        n.append(temp)
    cadastro['gols'] = n[:]
    cadastro['total'] = soma

    jogadores.append(cadastro.copy())

    validador = input('Quer continuar? [S/N] ').lower()[0]
    while validador not in 'sn':
        print('Error! Digite uma opção válida')
        validador = input('Quer continuar? [S/N] ').lower()[0]
    if validador == 'n':
        break
    print('-'*30)
    
print('-='*30)
print(f'{'cod':<3} {'nome':<15} {'gols':<15} {'total':<6}')
print('-'*43)

for j,k in enumerate(jogadores):
    print(f'{j:>3}',end=' ')
    for m in k.values():
        print(f'{str(m):<15}',end=' ')
    print()

print('-'*43)

while True:
    det = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if det == 999:
        break
    elif 0 <= det <= len(jogadores)-1:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[det]['nome']}')
        for w, z in enumerate(jogadores[det]['gols']):
            print(f'No jogo {w+1} fez {z} gols.')
    else:
        print(f'Erro! Não existe jogador com o código {det}')

print('<<< Encerrando >>>')
