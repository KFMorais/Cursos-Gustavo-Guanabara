nome = input('digite seu nome: ').title().strip()
nomesplitado = nome.split()
print(nome)
print(f'Primeiro nome: {nomesplitado[0]}')
valor = len(nomesplitado)-1
print(f'Último nome: {nomesplitado[valor]}')