'''Exercício Python 17:
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot
oposto = float(input('informe o comprimento do cateto oposto: '))
adjacente = float(input('informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente) # Hipotenusa = Raiz quadrada das soma dos Quadrados dos catetos
print('O comprimento da hipotenusa será {:.2f}'.format(hipotenusa))

'''#Jeito1 do professor sem importação

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2) # Hipotenusa = Raiz quadrada das soma dos Quadrados dos catetos
print('A hipotenusa vai medir {:.2f}'.format(hi))

#Jeito2 do professor com importação

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''