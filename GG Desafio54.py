from datetime import date
maior = 0
menor = 0
for i in range(7):
    ano = int(input(f'informe o ano de nascimento da {i+1}ª pessoa: ').strip())
    #idade = date.today().year - ano
    idade = 2017 - ano
    if idade >=18:
        maior += 1
    elif idade <18:
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} são menores de idade')