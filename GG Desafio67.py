while True:
    valor = int(input('digite o valor para que possamos informar a tabuada: ').strip())
    if "-" in str(valor):
        break
    cont = 1
    while True:
        tabuada = print(f'{valor} x {cont} = {valor * cont}')
        cont += 1
        if cont == 11:
            break
print('Volte sempre!!!')