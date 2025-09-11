n = soma = cont = 0
while n != 999:
    soma += n
    n = int(input('digite um valor [999 para parar]: ')) 
    if n != 999:
        cont += 1    

print(f'{soma}')
print(cont)