'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

d = float(input('Quantos Dias de aluguel ? : '))
km = float(input('Quantos KM Rodados? : '))
c1 = (d * 60) + (0.15 * km)
print('O valor total pelo aluguel R${:.2f}'.format(c1))
