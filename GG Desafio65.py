controle = 'S'
ciclos = soma = 0
while controle != 'N':
    n = int(input('informe um número: ').strip())
    soma = soma + n
    controle = input('Deseja informar mais números? [Sim ou Não] ').strip().upper()[0]    
    ciclos += 1
    if ciclos == 1:
        maior = n  
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    
print(f'Você digitou {ciclos} números e a média foi: {soma/ciclos:.2f}')
print(maior)
print(menor)
