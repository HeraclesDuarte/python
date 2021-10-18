# Exercício Python 23:
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# EX. Digite o numero 1834 ele terá
# Unidade:4
# dezena:3
# Centena: 3
# Milhar:1
# e que funcione para numeros menores
# --------JEITO 1 DÁ ERRO COM MENOS UNIDADES --------------
# num = int(input('Informe um numero: '))
# n = str(num)
# # print('\nAnalisando o número')
# # print('Quantas numeros = ',len(n))
#
# print('Unidade = {}'.format(n[3]))
# print('Dezena = {}'.format(n[2]))
# print('Centena = {}'.format(n[1]))
# print('Milhar = {}'.format(n[0]))
# ------------------------------------------------------------

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
