salario = float(input('informe o valor do seu salário: ').strip())

if salario > 1250:
    aumento1 = salario * 0.1
    print(f'Seu novo salário com o reajuste será no valor de R$ {(aumento1+salario):.2f}')
else:
    aumento2 = salario * 0.15
    print(f'Seu novo salário com o reajuste será no valor de R$ {(aumento2+salario):.2f}')