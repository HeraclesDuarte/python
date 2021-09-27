#Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.

n1 = float(input('\nDigite a Nota 1: '))
n2 = float(input('Difite a nota 2: '))
s = (n1) + (n2)
m = float(s/2)
#média = (n1 + n2) / 2
print('\nNota 1 do Aluno : {} \n'
      'Nota 2 do Aluno : {} \n'
      'Média do Aluno  : {:.1f}'.format(n1 , n2, m))