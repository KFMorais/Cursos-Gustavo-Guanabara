bd = ('Gabinete', 300, 
      'Processador', 1100,
      'Placa mãe', 900,
      'Fonte', 380, 
      'Placa de Vídeo', 1340, 
      'Adaptador Wi-Fi', 80, 
      'Mouse', 30, 
      'Teclado', 80, 
      'Mouse Pad', 65,)

print('-'*80)
print(f'{'LISTAGEM DE PREÇOS':^80}')
print('-'*80)

#Formato 1
for i in range(18):
    if i % 2 == 0:
        print(f'{bd[i]:.<70}R$',end='')
    else:
        print(f'{bd[i]:>8.2f}')

print('-'*80)

#Formato 2
for i in range(0,18,2):
    print(f'{bd[i]:.<72}R$', end='') 
    print(f'{bd[i+1]:>5}')

print('-'*80)

#Formato 3
print(f'{bd[0]:.<72}R$', end='') 
print(f'{bd[1]:>5}')

print(f'{bd[2]:.<72}R$', end='') 
print(f'{bd[3]:>5}')

print(f'{bd[4]:.<72}R$', end='') 
print(f'{bd[5]:>5}')

print(f'{bd[6]:.<72}R$', end='') 
print(f'{bd[7]:>5}')

print(f'{bd[8]:.<72}R$', end='') 
print(f'{bd[9]:>5}')

print(f'{bd[10]:.<72}R$', end='') 
print(f'{bd[11]:>5}')

print(f'{bd[12]:.<72}R$', end='') 
print(f'{bd[13]:>5}')

print(f'{bd[14]:.<72}R$', end='') 
print(f'{bd[15]:>5}')

print(f'{bd[16]:.<72}R$', end='') 
print(f'{bd[17]:>5}')

print('-'*80)