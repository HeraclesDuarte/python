'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Qual a velocidade do carro?'))
if velocidade > 80:
    print('-=-' * 20)
    print('Você foi Multado por estar acima de 80KM')
    print('Sua multa e de R${:.2f}'.format((velocidade - 80) * 7))
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('Tenha um bom dia! Dirija com cuidado!')
    print('-=-' * 20)

# JEITO DO PROFESSOR sem Else usando condição simples
# VER AULA BONUS DE CORES

# velocidade = float(input('Qual a velocidade do carro: '))
# if velocidade > 80:
#     print('MULTADO! Você excedeu o Limite permitido que é de 80KM/h')
#     multa = (velocidade-80) * 7
#     print('Sua multa é de R${:.2f}'.format(multa))
# print('Tenha um bom dia! Dirija com segurança!')