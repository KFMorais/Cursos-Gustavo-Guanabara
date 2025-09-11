'''
import math

angulo = float(input('informe o ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Os valores de seno, cosseno e tangente são, respectivamente: {seno:.2f} {cosseno:.2f} {tangente:.2f}')
'''

from math import sin, cos, tan, radians

angulo = float(input('informe o ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Os valores de seno, cosseno e tangente são, respectivamente: {seno:.2f} {cosseno:.2f} {tangente:.2f}')