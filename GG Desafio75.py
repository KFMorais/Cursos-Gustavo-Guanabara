entrada = (int(input('digite um número: ')), int(input('digite outro número: ')), 
           int(input('digite mais um número: ')), int(input('digite o último número: ')))

print(f'Voce digitou os valores {entrada}')




print('=X='*30)
print('Letra A')

#Formato 1
teste = entrada.count(9)
print(f'O número "9" apareceu {teste} vez(es) ==> Formato 1')

#Formato 2
soma = 0
for i in range(4):
    if 9 == entrada[i]:
        soma += 1     
print(f'O número "9" apareceu {soma} vez(es) ==> Formato 2')




print('=X='*30)
print('Letra B')

#Formato 1
posicao = 0
j = 0
while j < 4: 
    if entrada[j] == 3:
        posicao = j+1
        print(f'O número "3" foi digitado pela primeira vez na posição {j+1}')
        break
    else:
        j += 1
if posicao == 0:
    print('O número "3" não foi digitado')

#Formato 2
if 3 in entrada:
    print(f'O número "3" foi digitado pela primeira vez na posição {entrada.index(3)+1}')
else:
    print('O número "3" não foi digitado')




print('=X='*30)
print('Letra C')
#Formato 1

pares = 0
for z in entrada:
    if z % 2 == 0:
        pares +=1
        if pares == 1:
            print('Os números pares encontrados foram:', end= ' ')
        print(z, end=' ')

if pares == 0:
    print('não localizados números pares')
