print(f'''{'='*50}
{'Banco ZABO':^50}
{'='*50}''')
saque = int(input('informe o valor a ser sacado: R$ ').strip())
notas = [50, 20, 10, 1]
for i in range(4):
    if (saque / notas[i]) >= 1:
        print(f'Total de {saque//notas[i]} celulas de R$ {notas[i]}')
        saque = saque % notas[i]
    
print(f'''{'='*50}
Volte sempre ao Banco ZABO! Tenha um bom dia!''')
