num = input('digite um número de 0 a 9999:  ')

num_ajustado =  num.strip()

if (len(num_ajustado) == 4):
    print(f'''          
    unidade: {num_ajustado[3]}
    dezena: {num_ajustado[2]}
    centena: {num_ajustado[1]}
    milhar: {num_ajustado[0]}
    ''')

if (len(num_ajustado) == 3):
    print(f'''          
    unidade: {num_ajustado[2]}
    dezena: {num_ajustado[1]}
    centena: {num_ajustado[0]}
    milhar: 0
    ''')

if (len(num_ajustado) == 2):
    print(f'''          
    unidade: {num_ajustado[1]}
    dezena: {num_ajustado[0]}
    centena: 0
    milhar: 0
    ''')

if (len(num_ajustado) == 1):
    print(f'''          
    unidade: {num_ajustado[0]}
    dezena: 0
    centena: 0
    milhar: 0
    ''')

if (len(num_ajustado) == 0):
    print('''          
   digite um número válido
    ''')