#aqui só cabe while (não cabe for) por causa da quantidade de ciclos serem incertos...

genero = input('Informe seu gênero (M/F): ').strip().upper()[0]
#while (genero != 'M') and (genero != 'F'):
while genero not in 'MF':
    #print('Dados inválidos, por favor informe seu gênero corretamente!')
    genero = input('Dados inválidos, por favor informe seu gênero corretamente! ').strip().upper()[0]
    #genero = input('Informe seu gênero (M/F): ').strip().upper()[0]
print(f'Gênero {genero} registrado com sucesso!')
