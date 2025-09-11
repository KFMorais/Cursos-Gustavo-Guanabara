mult3 = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        mult3 += 1 # contador
        soma = soma + i #acumulador
print(mult3)
print(soma)
