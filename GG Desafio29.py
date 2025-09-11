vel = int(input('Informe a velocidade do carro: ').strip())

if (vel > 80):
    exc = vel - 80
    multa = exc * 7
    print(f'''Você ultrapassou o limite de velocidade permitido na via então, vai ser multado. 
    E o valor da multa é R$ {multa:.2f}''')