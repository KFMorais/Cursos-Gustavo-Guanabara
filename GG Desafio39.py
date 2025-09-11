from datetime import date #atenção
ano_nsc = int(input('informe o seu ano de nascimento: ').strip())
genero = input('Informe seu genero (M ou F) ').strip().title()

if genero == 'F':
    print('Alistamento militar é obrigatório apenas pessoas do gênero Masculino')
elif genero == 'M':
    idade = date.today().year - ano_nsc #atençãoooooooooo
    if idade > 18: #já passou do tempo
        diferenca = idade - 18
        print(f'Você está com {idade} anos de idade ou seja, já passaram {diferenca} anos do tempo do alistamento')
    elif idade < 18: #Ainda vai se alistar
        diferenca = 18 - idade
        print(f'Você está com {idade} anos de idade ou seja, faltam {diferenca} anos para realizar seu alistamento')
    else:
        print(f'Você está com {idade} anos de idade ou seja, já está na hora de realizar seu alistamento')
else:
    print('O gênero informado é inválido')
