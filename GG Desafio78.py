nm = list()
for i in range(5):
    nm.append(int(input(f'Digite um valor para a posição {i}: ')))

maior = nm[0]
for j in range(len(nm)):
    if nm[j] > maior:
        maior = nm[j]
print(f'O maior número é o {maior} e ele está nas posições:', end=' ')

for z in range(5):
    if maior == nm[z]:
        print(z, end=' ')
print()

menor = nm[0]
for k in range(1, len(nm)):
    if nm[k] < menor:
        menor = nm[k]
print(f'O menor número é o {menor} e ele está nas posições:', end=' ')

for m in range(5):
    if menor == nm[m]:
        print(m, end=' ')
print()

maiord = max(nm)
print(maiord)

menord = min(nm)
print(menord)
