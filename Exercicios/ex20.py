'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''


import random
n1 = input('Escreva o nome do aluno 1: ')
n2 = input('Escreva o nome do aluno 2: ')
n3 = input('Escreva o nome do aluno 3: ')
n4 = input('Escreva o nome do aluno 4: ')
lista = [n1, n2, n3, n4]
escolhido = random.shuffle(lista)
print('... A Ordem sorteada então será = {}.'.format(escolhido))