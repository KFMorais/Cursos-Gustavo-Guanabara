entrada = input('Digite a expressão: ')
pilha = []

for val in entrada:
    if val == '(':
        pilha.append('(')
    elif val == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')



'''

entrada = input('Digite a expressão: ')
verificacao = [] #Levantamento de parenteses

while True:
    for item in entrada:
        if item == ')' or item == '(':
            verificacao.append(item)
    print(entrada)
    print(verificacao)

    # Pegando as situações que é possível identificar de cara que a expressão está errada
    if verificacao[len(verificacao)-1] == '(' or verificacao[0] == ')' or len(verificacao) % 2 != 0:
        print('Sua expressão está errada')
        break
        
    z = len(verificacao)-1
    w = int(len(verificacao)/2)
    for i in range(w):
        if verificacao[i] != '(' or verificacao[z] != ')':
            print('Sua expressão está errada')
            break
        z -= 1

    print('Sua expressão é válida')
    break






'''










'''

entrada = input('Digite a expressão: ')
verificacao = [] #Levantamento de parenteses

while True:
    for item in entrada:
        if item == ')' or item == '(':
            verificacao.append(item)
    print(entrada)
    print(verificacao)

    # Pegando as situações que é possível identificar de cara que a expressão está errada
    if verificacao[len(verificacao)-1] == '(' or verificacao[0] == ')' or len(verificacao) % 2 != 0:
        print('Sua expressão está errada')
        break

    z = len(verificacao)-1
    for i in range((len(verificacao))/2):
        if verificacao[i] != '(' or verificacao[z] != ')':
            print('Sua expressão está errada')
            break
        z -= 1

    print('Sua expressão é válida')
    break

'''