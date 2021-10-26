'''Exercício Python 25:
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

silva = str(input('Qual o seu nome completo: ')).strip()
print ('Seu nome tem Silva: {} '.format('SILVA' in silva.upper()))