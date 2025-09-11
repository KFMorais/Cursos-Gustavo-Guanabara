soma = ciclos = 0
while True:
    n = int(input('digite um valor: '))
    if n == 999:
        break
    ciclos += 1
    soma += n

print(f'Foram digitados {ciclos} números e a soma deles é {soma}')

