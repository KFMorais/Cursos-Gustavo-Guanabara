n1 = int(input('informe o primeiro número: ').strip())
n2 = int(input('informe o segundo número: ').strip())

if n1 > n2:
    print('O \033[31mprimeiro\033[m número é maior que o segundo')
elif n1 < n2:
    print('O segundo número é maior que o primeiro')
else:
    print('Os dois números são iguais')