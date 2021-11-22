# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um número para saber se é par ou Impar: '))
if numero % 2 == 0:
    print('-' * 15)
    print('O número informado {} é PAR!'.format(numero))
    print(' **** FIM **** ')
    print('-' * 15)
else:
    print('-' * 15)
    print('o número Informado {} é IMPAR!'.format(numero))
    print(' **** FIM **** ')
    print('-' * 15)

# Jeito do professor

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('\nO número {} é PAR!'.format(numero))
else:
    print('\no número {} é IMPAR!'.format(numero))



