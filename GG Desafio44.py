print(f'\033[33m{' Python Story ':=^40}\033[m')

preco = float(input('informe o valor do produto: ').strip())

print('''Opções de Pagamento:
      - 1 À vista no dinheiro ou cheque com 10% de desconto
      - 2 À vista no cartão (direto) com 5% de desconto
      - 3 Em até 2x no cartão com preço normal
      - 4 Em 3x ou mais no cartão com 20% de juros
        ''')
cdp = int(input('\033[33minforme o número correspondente a opção desejada: \033[m').strip())

print(f'Opção de pagamento escolhida: {cdp}')

if cdp == 1:
    preco_1 = preco - (preco*0.1)
    print(f'O valor final a ser pago será: R$ {preco_1:.2f}')
elif cdp == 2:
    preco_1 = preco - (preco*0.05)
    print(f'O valor final a ser pago será: R$ {preco_1:.2f}')
elif cdp == 3:
    print(f'O valor final a ser pago será: R$ {preco:.2f}')
elif cdp == 4:
    preco_1 = preco + (preco*0.2)
    print(f'O valor final a ser pago será: R$ {preco_1:.2f}')
else:
    print('Opção inválida!')
