print('\n========================Desafio 10========================')
print('Criar um programa que leia quanto de dinheiro uma pessoa \n'
      'tem na carteira e mostre quantos Dolares eu posso comprar')

print('-'* 58)

r = float(input('\nQuanto tenho na Carteira em Reais R$: '))
d = float(input('\nQual é o Valor do Dolar Hoje em Reais: '))

print('O Valor de R${:.2f} corresponde a US${:.2f} Dolares: '.format(r, r/d))
print('-'* 15)
print(' **** Fim **** ')
print('-'* 15)

