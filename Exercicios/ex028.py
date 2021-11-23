# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
usuario = int(input('Escreva um numero de 0 a 5: '))
n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
numero = [n0, n1, n2, n3, n4, n5]
dois = random.choice(numero)
print('O numero Digitado = {}.'.format(usuario))
print('O numero pensado foi = {}.'.format(dois))

if usuario == dois:
    print('Você Venceu')
else:
    print('Você errou, Tente outra vez')


#'''////JEITO DO PROFESSOR////'''

# from random import randint
# from time import sleep
# print('-=-'*30)
# print('Pense em um número entre 0 e 5 e Tente Adivinhar o numero que o computador vai escolher...')
# print('-=-'*30)
# jogador = int(input('Digite um número que você acha que o computador escolheu para vencer você: '))
# computador = randint(0, 5) #FAZ O COMPUTADOR PENSAR
# print('Aguarde Computador esta pensando...')
# sleep(1)
# print('Será que vc vai Ganhar???')
# sleep(1)
# print('3')
# sleep(1)
# print('2')
# sleep(1)
# print('1')
# sleep(1)
# print('-=-'*15)
# print('O computador escolheu o número =={}=='.format(computador)) # jogador tenta adivinhar
# if jogador == computador:
#     print('Parabéns, você GANHOU!')
#     print('-=-' * 15)
# else:
#     print('Que pena, você PERDEU!')
#     print('-=-'*15)


