# '''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
#
#
import random
n1 = input('Escreva o nome do aluno 1: ')
n2 = input('Escreva o nome do aluno 2: ')
n3 = input('Escreva o nome do aluno 3: ')
n4 = input('Escreva o nome do aluno 4: ')
lista = [n1, n2, n3, n4]
escolhido = random.shuffle(lista)
print('... A Ordem sorteada então será = {}.'.format(lista))

# #Jeito do Professsor
#
# from random import shuffle
# n1 = str(input('Primeiro Aluno: '))
# n2 = str(input('Segundo  Aluno: '))
# n3 = str(input('Terceiro  Aluno: '))
# n4 = str(input('Quarto  Aluno: '))
# lista = [n1, n2, n3, n4]
# shuffle(lista)
# print('A Ordem de apresentação será')
# print(lista)