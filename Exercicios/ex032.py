'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''


# JEITO 1
# #
# ano = int(input('Digite o ano: '))
# if (ano % 4) == 0:
#     print('Ano {} é bissexto'.format(ano))
# else:
#     print('Ano {} não é bissexto'.format(ano))


# JEITO DO PROFESSOR

from datetime import date
ano = int(input('Que ano quer analisar? ou Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): #DIVISIVEL POR 4 E TAMBÉM NÃO PODE SER DIV POR 100 E NÃO PODE SER DIFERENTE DE 0 OU O ANO SER DIVISIVEL POR 400
    print('{} é bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))
