'''
JEITO DO PROFESSOR
'''

'''
 - Desafio 11
Faça um programa que Leia a Largura e a Altura de uma parede em Metros,
Calcule a sua área e a quantidade de Tinta necessária para Pintá-la,
Sabendo que cada Litro de Tinta, pinta uma area de 2M Quadrados.
'''
larg = float(input('Quanto m a Parede tem de Largura? : '))
alt = float(input('Quantos m a Parede tem de Altura? : '))
area = larg * alt
litros = area / 2

print('A sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(alt , larg, area))
print('Para pintar essa parede, você precisará de {}l de tinta. '.format(litros))
