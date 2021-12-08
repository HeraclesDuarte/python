'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

numero = int(input('Digite a quantidade de KM da sua Viagem: '))
if numero <= 150:
    print('Preço da Passagem R${:.2f}'.format((numero)*0.50))
    print(' **** FIM **** ')
    print('-' * 15)
else:
    numero > 150
    print('Preço da Passagem R${:.2f}'.format((numero) * 0.45))


