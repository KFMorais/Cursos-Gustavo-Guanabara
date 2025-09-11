from random import randint

#temporal = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
#print(temporal)  
######## ACIMA ESTÁ CRIADA UMA TUPLA COM VALORES RANDOMICOS... 
######## A IDEIA AQUI FOI QUEBRAR UM POUCO A LÓGICA DE QUE TUPLAS SÃO IMUTÁVEIS


temp = []
for i in range(5):
    temp.append(randint(1, 100))

#final = (temp)

#print(type(final))
print(temp)
#print(sorted(temp))
print(max(temp))
print(min(temp))


maior = temp[0]
for i in range(5):
    if maior < temp[i]:
        maior = temp[i]

print(maior)

menor = temp[0]
for i in range(5):
    if menor > temp[i]:
        menor = temp[i]

print(menor)


