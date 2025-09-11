from datetime import date
ano = str(input('Informe um ano para saber se ele é bissexto: ').strip())
if ano == '0':
    ano = str(date.today().year)
anoint = int(ano)
tamanho = len(ano)

if (ano[tamanho-1] == '0') and (ano[tamanho-2] == '0'):
    if (anoint % 400) == 0:
        print(f'O ano de {anoint} é bissexto')
    else:
        print(f'O ano de {anoint} NÃO é bissexto')    
else:
    if (anoint % 4) == 0:
        print(f'O ano de {anoint} é bissexto')
    else:
        print(f'O ano de {anoint} NÃO é bissexto')