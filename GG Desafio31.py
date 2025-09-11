km = int(input('informe a quantidade de km: ').strip())

if (km<=200):
    preco = km*0.50
    print(f'O valor da passagem será R$ {preco:.2f}')
if (km>200):
    preco = km*0.45
    print(f'O valor da passagem será R$ {preco:.2f}')
