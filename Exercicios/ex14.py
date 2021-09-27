'''Exercício Python 14: Escreva um programa que converta uma
temperatura digitando em graus Celsius e converta para graus Fahrenheit.

(31 °C × 9/5) + 32 = 88,7 °F'''

g = float(input('Informe um numero em graus °C: '))
calc = (g * ((9/5))) + 32
#calc = ((9 * g) /5) + 32 '''Jeito Professor'''
print('O valor {} em Graus Celsius convertido para graus Fahrenheit será {:.3f}°F'.format (g, calc))
