serieaclass = ('Cruzeiro', 'Flamengo', 'Bragantino', 'Palmeiras', 'Botafogo', 
                'Bahia', 'Mirassol', 'Fluminense', 'Atlético-MG', 'Corinthians', 
                'Ceará', 'Internacional', 'Grêmio', 'São Paulo', 'Vitória', 
                'Vasco', 'Santos', 'Juventude', 'Fortaleza', 'Sport')
k = 1
print()
print('Classificação do Brasileirão 2025 em 21/07/2025')
print()
for times in serieaclass:
    print(f'{k} {times}')
    k += 1
print()

print('#'*120)    
print('LETRA A:')
print(f'Os 5 primeiros colocados do Brasileirão são: {serieaclass[:5]}')

print(f'Os 5 primeiros colocados do Brasileirão são: ')
for i in range(5):
    if i == 3:
        print(f'{serieaclass[i]}', end=' e ')
    elif i == 4:
        print(f'{serieaclass[i]}.')
    else:
        print(f'{serieaclass[i]}', end=', ')
print('#'*120)


print('LETRA B:')

print(f'Os 4 últimos colocados do Brasileirão são, respectivamente:', end =' ')
print(serieaclass[16:])
print('#'*120)    

print('LETRA C:')
print(sorted(serieaclass))
print('#'*120)  


print('LETRA D:')

i = 0
while True:
    if 'Mirassol' == serieaclass[i]:
        break
    else:
        i += 1
print(f'O Mirassol está na {i+1}ª colocação')

print(f'{(serieaclass.index('Mirassol')+1)}')  ####### INTERESSANTÍSSIMO #######


print('#'*120)  
