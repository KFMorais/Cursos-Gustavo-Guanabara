arq_orig = input('Nome do arquivo de origem: ')
arq_dest = input('Nome do arquivo de destino: ')

try:
    with open(arq_orig, 'r', encoding='utf-8') as ar_or_ab:
        conteudo = ar_or_ab.read()

except FileNotFoundError:
    print(f'arquivo de origem ({arq_orig}) não encontrado')

else:
    with open(arq_dest, 'w', encoding='utf-8') as ar_dest_ab:
        ar_dest_ab.write(conteudo)

    print(f"Arquivo '{arq_orig}' copiado para '{arq_dest}' com sucesso!")

    try:
        with open(arq_dest, 'r', encoding='utf-8') as arq_final:
            print(f'''Segue o conteudo do arquivo de destino: 
{arq_final.read()}''')
    except Exception as e:
        print(f'Ocoreu um erro na leitura do arquivo: {e}')

