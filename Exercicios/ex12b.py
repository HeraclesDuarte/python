'''
 - Desafio 12
Façã um Algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
'''

v = float(input('Informe o Valor do Produto?:'))
ip = float(input('Informe o Valor do % de Desconto?:'))
d = (v/100)*ip
r = v-d
print('o valor do produto é R$:{} o seu desconto é: {}Reais'.format(v , d))
print('O Valor do seu produto é R$: {} Reais'.format(r))