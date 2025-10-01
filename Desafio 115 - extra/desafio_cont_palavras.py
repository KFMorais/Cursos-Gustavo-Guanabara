arq = 'teste.txt'#input('Digite o nome do arquivo a ser analisado: ')
final = {}

try: 
    with open(arq, 'r', encoding='utf-8') as arq_a:
        with open('analise.txt', 'w', encoding='utf-8') as analise_t:
            for linhas in arq_a:
                #Tratar o p para que só vá isalpha
                for p in linhas.lower().split():
                    if p in final:
                        final[p] = final[p]+1
                    else:
                        final[p] = 1
            for key, value in final.items():
                analise_t.write(f'{key:<.15}: {value}\n')
                    
except FileNotFoundError:
    print(f'Arquivo {arq} não localizado')

