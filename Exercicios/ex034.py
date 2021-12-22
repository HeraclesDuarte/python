'''''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''''


salario = float(input('Informe o salário: R$ '))
if salario <= 1250:
   valor = salario + (salario / 100*15)
   print('O novo salário com 10% de R${:.2f} passa para R${:.2f}'.format(salario, valor))
else:
    valor = salario + (salario / 100*10)
    print('O novo salário com 15% de R${:.2f} passa para R${:.2f}'.format(salario, valor))

