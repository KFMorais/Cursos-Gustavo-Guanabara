valor_produto = int(input('Informe o valor do produto: '))

p_desconto = (valor_produto) - (valor_produto*5/100)

print(f'O valor do produto com desconto é R$ {p_desconto:.2f}')