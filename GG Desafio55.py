pesos = []
for i in range(5):
    entrada = float(input(f'informe o peso da {i+1}ª pessoa: ').strip())
    pesos.append(entrada)

maior = pesos[0]
menor = pesos[0]
for i in range(5):
    if pesos[i] > maior:
        maior = pesos[i]
    if pesos[i] < menor:
        menor = pesos[i]

print(maior)
print(menor)