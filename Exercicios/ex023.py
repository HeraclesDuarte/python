# Exercício Python 23:
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# EX. Digite o numero 1834 ele terá
# Unidade:4
# dezena:3
# Centena: 3
# Milhar:1
# e que funcione para numeros menores
# --------JEITO 1 DÁ ERRO COM MENOS UNIDADES --------------
# numero = int(input('Informe um numero: '))
numero = str(input('Informe um numero: '))
# n = str(numero)
print('\nAnalisando o número...')
# print('Quantas numeros = ',len(n))

print('\nUnidade = {}'.format(numero[3]))
print('Dezena = {}'.format(numero[2]))
print('Centena = {}'.format(numero[1]))
print('Milhar = {}'.format(numero[0]))

# -----------JEITO CORRETO PROFESSOR--------------
# num = int(input('Informe um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('Analisando o número {}'.format(num))
# print('Unidade {}'.format(u))
# print('Dezena {}'.format(d))
# print('Centena {}'.format(c))
# print('Milhar {}'.format(m))
