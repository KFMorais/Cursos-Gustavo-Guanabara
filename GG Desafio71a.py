print(f'''{'='*50}
{'Banco ZABO':^50}
{'='*50}''')
saque = int(input('informe o valor a ser sacado: R$ ').strip())
while True:
    if (saque / 50) >= 1:
        print(f'Total de {saque//50} celulas de R$ 50,00')
        saque = saque % 50
    if (saque / 20) >= 1:
        print(f'Total de {saque//20} celulas de R$ 20,00')
        saque = saque % 20
    if (saque / 10) >= 1:
        print(f'Total de {saque//10} celulas de R$ 10,00')
        saque = saque % 10
    if (saque / 1) >= 1:
        print(f'Total de {saque//1} celulas de R$ 1,00')
        saque = saque % 1
    
    break

print(f'''{'='*50}
Volte sempre ao Banco ZABO! Tenha um bom dia!''')
