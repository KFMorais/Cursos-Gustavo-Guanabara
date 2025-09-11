num = input('digite um número de 0 a 9999:  ')
num_ajustado =  num.strip()
num_comp = (f'{num_ajustado:0>4}')

print(num_comp)

print(f'''          
    unidade: {num_comp[3]}
    dezena: {num_comp[2]}
    centena: {num_comp[1]}
    milhar: {num_comp[0]}
    ''')