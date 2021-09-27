print('\n================= Desafio 12 ================')

print('Faça um Algoritmo que leia o preço de um produto \n'
      'e mostre seu novo preço, com 5% de desconto.')
print ('_'*45)

valor = float(input('\nInforme o Valor do Produto?:'))
#p = float (0.05)
p = float (5/100)
calc = float(p * valor)
result = valor-calc

print ('_'*45)

print('=> o valor do produto é: {} \n'
      '=> o percentual Aplicado será :{:.0f}%'.format(valor, p*100))
print('=> 5% de {} Será de R$:{} Reais '.format(valor, calc))
print('\nLogo... \n\n '
      'o valor com os 5% de Desconto será R$:{:.2f} Reais '.format(result))


print('-'*15)
print(' **** Fim **** ')
print('-'*15)
