from datetime import date

ano_nasc = int(input('Informe o ano de seu nascimento: ').strip())
#ano_atual = date.today().year
ano_atual = 2017
idade = ano_atual-ano_nasc
print(f'{idade} anos')

if idade <=9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 25:
    print('Categoria: Sênior')
elif idade > 25:
    print('Categoria: Master')
