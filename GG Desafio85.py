princ = [[],[]]

for i in range(7):
    temp = int(input(f'Digite o {i+1}º número: '))
    if temp % 2 == 0:
        princ[0].append(temp)
    else:
        princ[1].append(temp)

print(princ)

princ[0].sort()
princ[1].sort()
print(f'Os valores pares digitados foram: {princ[0]}')
print(f'Os valores impares digitados foram: {princ[1]}')