'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''


# ano = int(input('Digite o ano: '))
# if (ano % 4) == 0:
#     print('Ano {} é bissexto'.format(ano))
# else:
#     print('Ano {} não é bissexto'.format(ano))


# JEITO DO PROFESSOR

ano = int(input('Que ano quer analisar? '))
if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0: '''DIVISIVEL POR 4 E TAMBÉM NÃO PODE SER DIV POR 100 E NÃO PODE SER DIFERENTE DE 0 OU O ANO SER DIVISIVEL POR 400'''
    print('O Ano {} é bissexto'.format(ano))
else:
    print('O Ano {} não é bissexto'.format(ano))
