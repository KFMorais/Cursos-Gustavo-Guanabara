num = []
ft = ['primeiro','segundo','terceiro']
cont = 0
maior = 0

while (len(num)<3):
    num.append(int(input(f'Informe o {ft[cont]} número: ').strip()))
    if (num[cont] > maior):
        maior = num[cont]
    cont += 1

if (num[cont] < num[cont]):
    menor = num[cont]
    
DEU ERRADO!!!

print(maior)
#print(menor)