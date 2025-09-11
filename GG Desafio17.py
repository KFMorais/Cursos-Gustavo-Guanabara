from math import pow, sqrt

catop = float(input('informe o valor do cateto oposto: '))
catad = float(input('informe o valor do cateto adjacente: '))

hipotenusa = sqrt(pow(catop, 2) + pow(catad, 2))

print(hipotenusa)

#h**2 = c1**2 + c2**2

