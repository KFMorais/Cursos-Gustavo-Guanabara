numero = int(input('Informe um número: ').strip())

print('''Base de conversão:
      - 1 para binário
      - 2 para octal
      - 3 para hexadecimal     
      ''')
opcao = int(input('informe o número referente a base de convesão de sua escolha: ').strip())

if opcao == 1:
    conversao = bin(numero)
    print (f'{conversao[2:]}')
elif opcao == 2:
    conversao = oct(numero)
    print (f'{conversao[2:]}')
elif opcao == 3:
    conversao = hex(numero)
    print (f'{conversao[2:]}')
else:
    print('opção inválida')
