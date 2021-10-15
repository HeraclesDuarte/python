# print("""Exercício Python 22:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.""")

nome = str(input('Nome completo: ')).strip()

print('O nome com todas as letras em MAIÚSCULA: {}'.format(nome.upper()))
print('O nome com todas as letras em minusculo: {}'.format(nome.lower()))
print('Quantas letras tem ao todo sem considerar espaços: {}'.format(len(nome) - nome.count(' ')))

qpn = (nome.find(' '))
dividido = nome.split()

print ('\nseu primeiro nome é: {} '.format((dividido[0])))
print('Seu primeiro nome tem {} Letras' .format(qpn))

'''#JEITO DO PROFESSOR
separa = nome.split()
print('\nSeu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))'''

