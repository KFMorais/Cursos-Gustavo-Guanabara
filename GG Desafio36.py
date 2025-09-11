valor_casa = float(input('Informe o valor da casa: ').strip())
salario = float(input('Informe o seu salário: ').strip())
qtd_anos = int(input('Informe a quantidade de anos que deseja paga-la: ').strip())

valor_prestacao = valor_casa/(qtd_anos*12)
lim_prestacao = salario*0.3 #valor máximo da prestação para que o empréstimo possa ser aprovado

print(f'30% do seu salário: R$ {lim_prestacao:.2f}')
print(f'Valor da prestação nessas condições: R$ {valor_prestacao:.2f}')

if valor_prestacao <= lim_prestacao:
    print('Empréstimo aprovado!')
else: 
    print('Empréstimo recusado!')
