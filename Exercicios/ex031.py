'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

'''Jeito 1'''
numero = int(input('Digite a quantidade de KM da sua Viagem: '))
if numero <= 150:
    print('Preço da Passagem R${:.2f}'.format((numero)*0.50))
    print(' **** FIM **** ')
    print('-' * 15)
else:
    numero > 150
    print('Preço da Passagem R${:.2f}'.format((numero) * 0.45))
    print(' **** FIM **** ')

# '''Jeito 2'''
# numero = int(input('Digite a quantidade de KM da sua Viagem: '))
# if numero <= 150:
#     print('Preço da Passagem R${:.2f}'.format((numero)*0.50))
# if numero > 150:
#     print('Preço da Passagem R${:.2f}'.format((numero)*0.45))

# ------------------------------------------------------------------------------------------------

# '''JEITO 1 DO PROFESSOR usando o if e else'''

# distancia = float(input('Qual é a Distancia da sua Viagem? '))
# print('Você esta prestes a começar uma viagem de {}KM'.format((distancia)))
# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45
# print('E o Preço da sua passagem será de R${:.2f}'.format(preco))

# JEITO 2 DO PROFESSOR usando o if simplificado

# distancia = float(input('Qual é a Distancia da sua Viagem? '))
# print('Você esta prestes a começar uma viagem de {}KM'.format((distancia)))
# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
# print('E o Preço da sua passagem será de R${:.2f}'.format(preco))


