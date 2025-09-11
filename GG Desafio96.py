def area(base, altura): 
    res = base * altura 
    print(f'A área de um terreno de {base} x {altura} é {res:.2f}m2') 


print('Calculo de Terrenos')   
print('-'*19) 
largura = float(input('Largura (m): ')) 
comprimento = float(input('Comprimento (m): ')) 

area(largura, comprimento) 