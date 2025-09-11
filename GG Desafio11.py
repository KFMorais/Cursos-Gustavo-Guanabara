largura = int(input('Informe a largura: '))
altura = int(input('Informe a altura: '))

area = (largura * altura)

l_tinta = 2 

qt_necessaria = (area/l_tinta)

print(f'{qt_necessaria:.0f}')