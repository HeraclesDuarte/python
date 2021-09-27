print( ' //// Desafio 9 ///// \n\n Faça um Programa que Leia um número inteiro qualquer\n e mostre na tela a sua tabuada')

numero = int(input('\nDigite um numero para a Tabuada: '))
m1 = int(numero)*1
m2 = int(numero)*2
m3 = int(numero)*3
m4 = int(numero)*4
m5 = int(numero)*5
m6 = int(numero)*6
m7 = int(numero)*7
m8 = int(numero)*8
m9 = int(numero)*9
m10 = int(numero)*10

print('\nA tabuada para o Numero {} é: \n'.format(numero))
print('{} *  1 = : {}'.format(numero, m1))
print('{} *  2 = : {}'.format(numero, m2))
print('{} *  3 = : {}'.format(numero, m3))
print('{} *  4 = : {}'.format(numero, m4))
print('{} *  5 = : {}'.format(numero, m5))
print('{} *  6 = : {}'.format(numero, m6))
print('{} *  7 = : {}'.format(numero, m8))
print('{} *  9 = : {}'.format(numero, m9))
print('{} * 10 = : {}'.format(numero, m10))