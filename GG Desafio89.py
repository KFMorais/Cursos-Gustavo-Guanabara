cadastro = []

dados = ('Nome:', 'Nota 1:', 'Nota 2:')
temp = [[]]
while True: 
    temp.insert(0, input(f'{dados[0]} '))
    for j in range(2):
            temp[1].append(float(input(f'{dados[j+1]} ')))
    media = float((temp[1][0]+temp[1][1])/2)
    temp[1].append(f'{media:.1f}')
    cadastro.append(temp[:])

    temp = [[]]

    val = input('Quer continuar: [S/N] ').lower() 
    if val in 'n': 
        break 

print('-='*60) 

print()

print(f'No. {dados[0]:<15} Média')
print('-'*25) 

for k in range(len(cadastro)):
     print(f'{k:<4}{cadastro[k][0]:<15} {cadastro[k][1][2]}') 
print('-'*25) 
print() 
while True:
    val2 = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if val2 == 999:
        break
    if val2 < 0 or val2 > len(cadastro)-1:                     
         print('Referencia inexistente, tente novamente!')
    else:
        print(f'Notas de {cadastro[val2][0]} são: {cadastro[val2][1][0]} e {cadastro[val2][1][1]}')

print('-='*30) 
print(f'{'Volte Sempre!!!':^60}')    
print('-='*30)     
    
    


'''



cadastro = []

dados = ('Nome:', 'Nota 1:', 'Nota 2:')
temp = [[],[],[]]
while True: 
    temp[0].append(input(f'{dados[0]} '))
    for j in range(2):
            temp[1].append(float(input(f'{dados[j+1]} ')))
    media = [(temp[1][0]+temp[1][1])/2]
    temp[2].append(media)
    cadastro.append(temp[:])

    temp = [[],[], []]

    val = input('Quer continuar: [S/N] ').lower() 
    if val in 'n': 
        break 

print('-='*60) 

print(cadastro)

'''