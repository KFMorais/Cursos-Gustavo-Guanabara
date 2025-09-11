'''
nome = (input('Qual seu nome? ').strip().title())
if nome == 'Klewerton':
    print('Que nome bonito!')
elif nome == 'Vinicius' or nome == 'Angelina' or nome == 'Luiz':
    print('Seu nome é especial!')
elif nome in 'Ana Claudia Jessica Juliana': #dica nova - eu não conhecia
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia {nome}')
#Laços de Repetição - Parte 1 (for)

#for i in range(0,3):

#for i in range(1,6):
#    print(i)

#for i in range(6, 0, -1): # o -1 aqui, é a forma de interação, se fosse 2 no final seria de 2 em 2... 
#    print(i)

#for i in range(0, 7, 2): # o -1 aqui, é a forma de interação, se fosse 2 no final seria de 2 em 2... 
#    print(i)

#for i in range((int(input('digite o número de ciclos: ')))+1):
#    print(i)

#i = int(input('digite o número de inicio: '))
#f = int(input('digite o número de fim: '))
#p = int(input('digite o número de modo: '))

#for i in range(i, f+1, p):
#    print(i)

s = 0
for i in range(0,3):
    n = int(input('digite um número: '))
    s += n

print(s)



#while #enquanto - mais utilizado quando não sabe o limite - INTERESSANTE!!!
#for geralmente usa para quando tem limite
#while => condição verdadeira

for c in range (1,10):
    print(c)
print('FIM')

c = 1
while c <10:
    print(c)
    c +=1
print('FIM')

r = 'S'

while r == 'S':
    c = int(input('digite um valor: '))
    r = input('Quer continuar? (S/N): ').upper().strip()
print('Fim')

n = 1
pares = 0
impares = 0
while n != 0:
    n = int(input('digite um número: ').strip())
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f'Foram digitados {pares} números pares e {impares} números impares')
'''



