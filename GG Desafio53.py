frase = input('digite uma frase: ').strip().lower()
fraseajustada = []

print(frase) #1

for i in range(len(frase)):
    if frase[i] != ' ':
        fraseajustada.append(frase[i])

print(fraseajustada) #2

total = len(fraseajustada)
ciclos = len(fraseajustada)//2
print(ciclos) #3
print(total) #4

soma = 0
for i in range(ciclos):
    if fraseajustada[i] == fraseajustada[total-1]:
        soma += 1
    total = total - 1

print(soma) #5

if soma == ciclos:
    print('Palindromo')
else:
    print('NÃO')
