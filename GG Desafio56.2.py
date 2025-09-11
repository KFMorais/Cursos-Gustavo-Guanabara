somaidade = 0
idademaisvelho = 0
nomemaisvelho = 0
mm20 = 0
for i in range(4):
    nome = input(f'Informe o {i+1}º nome: ').strip().title()
    idade = int(input('Informe a idade: ').strip())
    genero = input('Informe o gênero (M/F): ').strip().title()
    somaidade = somaidade + idade
    if i == 3:
        media = somaidade/4 #resultado do 1º questionamento
    '''if i == 0:
        idademaisvelho = idade
        nomemaisvelho = nome'''
    if genero == 'M' and idade > idademaisvelho:
        idademaisvelho = idade
        nomemaisvelho = nome
    if genero == 'F' and idade < 20:
        mm20 += 1

print(f'1º: A média de idade do grupo é de {media:.1f} anos')   #1º respondido
print(f'2º: O nome do homem mais velho do grupo é {nomemaisvelho} e ele tem {idademaisvelho} anos') #2º respondido
print(f'3º: Para os dados informados, {mm20} mulheres tem menos de 20 anos') #3º respondido
