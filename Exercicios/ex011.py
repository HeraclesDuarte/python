print('\n============================ Desafio 11 =============================')

print('Faça um programa que Leia a Largura e a Altura de uma parede em Metros, \n'
      'Calcule a sua área e a quantidade de Tinta necessária para Pintá-la, \n'
      'Sabendo que cada Litro de Tinta, pinta uma area de 2M Quadrados')

print('='*70)

a = float(input('\nQuantos m a Parede tem de Altura? : '))
l = float(input('Quanto m a Parede tem de Largura? : '))
#sm = float((a) * (l))

#print('soma {} '.format(sm))
print('As Dimenções da sua Parede são {}m² x {}m² e sua area total é de {}m² \n'.format(a , l, (a*l)))

print('Para isso vamos precisar de {:.2f} litros de Tinta.'.format((a*l)/2))

print('-'*15)
print(' **** Fim **** ')
print('-'*15)