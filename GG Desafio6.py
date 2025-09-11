numero = int(input('digite um número: '))

cores = {
'limpa':'\033[m',
'azul':'\033[34m', 
'amarelo':'\033[33m',
'famarelo':'\033[43m'
}

print(f'O número digitado foi {cores['amarelo']}{numero}{cores['limpa']}. O dobro dele vale {numero*2}, o triplo {numero*3} e a sua raiz quadrada {numero**(1/2):.0f}')