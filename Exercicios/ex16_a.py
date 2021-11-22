# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
# a sua porção Inteira.



num = float(input('Digite um numero: '))
num2 = math.floor(num)
print('O numero {} tem a parte inteira igual a : {}'.format(num, math.trunc(num2)))
#print('O numero {} tem a parte inteira igual a : {}'.format(num, (num2)))

#JEITO DO PROFESSOR'''

'''from math import trunc
num = float(input('Digite um numero: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num))) 


num = float(input('Digite um numero: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''

