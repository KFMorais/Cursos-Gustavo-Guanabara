soma = 0
for i in range (1, 7):
    n = int(input(f'informe o {i}º número: ').strip()) #interessante
    if n % 2 == 0:
        soma += n
print(soma)
