letraa = letrab = letrac = 0

while True:
    idade = int(input('Digite a idade: ').strip())
    sexo = str(input('Digite o sexo. [M] ou [F]: ').strip().upper()[0])
    while sexo not in 'MF':
        sexo = str(input('Opção inválida!!! Digite o sexo. [M] ou [F]: ').strip().upper()[0])
    
    if idade > 18:
        letraa += 1
    
    if sexo == 'M':
        letrab += 1
    
    if sexo == 'F':
        if idade < 20:
            letrac += 1

    opcao = str(input('Deseja cadastrar mais usuários? [S] ou [N]: ').strip().upper()[0])
    while opcao not in 'SN':
        opcao = str(input('Opção inválida!!! Deseja cadastrar mais usuários? [S] ou [N]: ').strip().upper()[0])
    if opcao == 'N':
        break

print(f'Quantas pessoas tem mais de 18 anos? {letraa}')
print(f'Quantos homens foram cadastrados? {letrab}')
print(f'Quantas mulheres tem menos de 20 anos? {letrac}')
print('Fim')
