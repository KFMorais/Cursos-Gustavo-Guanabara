n_arq = input('Digite o nome para um arquivo: ')

try:
    with open(n_arq, 'r', encoding='utf-8') as arq_teste:
        ref = arq_teste.readlines()
except FileNotFoundError:
    print('Arquivo não encontrado.')
else:
    print(f'O arquivo {n_arq} tem {len(ref)} linhas')
