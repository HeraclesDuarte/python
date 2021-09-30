'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random
n1 = input('Escreva o nome 1: ')
n2 = input('Escreva o nome 2: ')
n3 = input('Escreva o nome 3: ')
n4 = input('Escreva o nome 4: ')
alunos = (n1, n2, n3, n4)
print('O aluno escolhido foi = {:=^11}.'.format(random.choice(alunos)))

'''#Jeito do professor

from random import choice
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
lista = [n1, n2, n3, n4] # Aqui usamos uma lista que fica entre colchetes
escolhido = choice(lista)
print('O aluno escolhido foi = {}.'.format(escolhido))'''