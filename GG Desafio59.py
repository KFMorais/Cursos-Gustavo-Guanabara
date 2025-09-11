from time import sleep
n1 = int(input('informe o 1º número: ').strip())
n2 = int(input('informe o 2º número: ').strip())

while True:
    print('''Opções:
        [1] somar 
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
          ''')
    opcao = int(input('Escolha uma das opções: ').strip())
    if opcao == 5:
        break
    elif opcao == 4:
        n1 = int(input('informe o 1º número: ').strip())
        n2 = int(input('informe o 2º número: ').strip())
    elif opcao == 3:
        if n1 > n2:
            print(f'o primeiro número digitado é maior que o segundo')
        elif n1 < n2:
            print(f'o segundo número digitado é maior que o primeiro')
        else:
            print(f'Os dois números são iguais')
    elif opcao == 2:
        print(f'O resultado da multiplicação de {n1} por {n2} é igual à {n1*n2}')
    elif opcao == 1:
        print(f'O resultado da soma de {n1} mais {n2} é igual à {n1+n2}')
    else:
        print('Opção inválida. Tente novamente')

    sleep(2)


print('fim do programa')
