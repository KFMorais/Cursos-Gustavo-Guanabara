numero = int(input('digite um número: '))
cores = {
'limpa':'\033[m',
'azul':'\033[1;34m',
'amarelo':'\033[1;33m',
'vermelho':'\033[1;31m',
'verde':'\033[1;32m'
}

print(f"o número digitado foi {cores['azul']}{numero}{cores['limpa']}, o antecessor dele é {cores['amarelo']}{numero-1}{cores['limpa']} e o sucessor é {cores['verde']}{numero+1}{cores['limpa']}")