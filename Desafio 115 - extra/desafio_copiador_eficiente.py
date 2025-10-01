orig = input('Digite o nome do arquivo de origem: ')
dest = input('Digite o nome do arquivo de destino: ')

try:
    with open(orig, 'r', encoding='utf-8') as orig_a:
        with open(dest, 'w', encoding='utf-8') as dest_a:
            for linha in orig_a:
                dest_a.write(linha)
            print(f'Copia do arquivo {orig} para o {dest} realizada com sucesso')
except FileNotFoundError:
    print('Tivemos problemas e não localizamos um dos arquivos em questão')
except Exception as z:
    print(f'Erro inesperado do tipo: {z}')
