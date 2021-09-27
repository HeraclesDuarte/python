

print('\n========================Desafio 10========================')
print('Criar um programa que leia quanto de dinheiro uma pessoa \n'
      'tem na carteira e mostre quantos Dolares ela pode Comprar \n'
      '#Considere US$ 1,00 = R$ 3,27#')

r = float(input('\nQuanto tenho na Carteira de Dinheiro em Reais R$: '))
#print('\nO Valor em Reais é: {}'.format(r))
print('O Valor de R${:.2f} corresponde a US${:.2f} Dolares: '.format(r, r/3.27))


print('-'* 15)
print(' **** FIM **** ')
print('-'* 15)