
'''JEITO DO PROFESSOR'''

preco = float(input('Qual é o Preço do Produto? R$'))
novo = preco - (preco*5/100)

print('O Produto que custava R$ {:.2f} Na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco,novo))
