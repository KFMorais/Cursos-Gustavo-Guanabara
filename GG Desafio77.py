palavras = ('casea', 'show', 'bibu', 'bbcc', 'Luiz', 'batata', 'aaa')
vogais = ('a', 'e', 'i', 'o', 'u')

#Formato 1
for p in palavras:
    print(f'na palavra {p} temos as seguintes vogais: ', end='')
    soma = 0
    for l in p:
        if l in 'aeiou':
            print(l, end=' ')
            soma += 1
    if soma == 0:
        print('palavra sem vogal',end='')
    print() #funciona com um quebra de página

#Formato 2
for i in range(len(palavras)):
    soma = 0
    print(f'Na palavra {palavras[i]} temos as seguintes vogais:',  end=' ')
    for j in range(len(palavras[i])):    
        for v in vogais:
            if palavras[i][j] == v:
                print(f'{v}', end=' ')
                soma += 1
    if soma == 0:
        print('palavra sem vogal', end='')
    print()
#Formato 3 = faltou colocar as vogais em ordem de aparição e em todas as ocorrências
for i in range(len(palavras)):
    soma = 0
    print(f'Na palavra {palavras[i]} temos', end = ' ')
    for v in vogais:
        if v in palavras[i]:
            print(v, end = ' ')
            soma += 1
    if soma == 0:
        print('palavra sem vogal', end='')
    print()
    