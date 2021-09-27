print('\n================= Desafio 12 ================ \n'
      'Faça um Algoritmo que Leia o Sálario de um Funcionário\n'
      'e mostre seu novo Salário, com 15% de Aumento.')
print ('_'*45)

salario = float(input('Informa o Salario R$: '))
calculo = salario + (salario*15/100)
print('Novo salario com 15% de aumento {:.2f}'.format(calculo))

print('-'*15)
print(' **** Fim **** ')
print('-'*15)