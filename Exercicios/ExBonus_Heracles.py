'''a vista 5% do valor total
a prazo
TAC - 100,00
sem deconto
acresc 5% na prestação = 5% total
900+100+5% = 1155 / 24'''


preco = float(input('Qual é o Preço do Produto? R$'))
parcela = float(input('Se houver parcelas, gostaria de parcelar em quantas vezes: '))
#Percentual = float(input('Qual é o percentual %: '))

novo = preco - (preco*5/100)
novo2 = preco + (preco * (5/100))


acrescimo = (preco * (5/100))
parcelado = (preco / parcela)
precoparcela = parcelado + (parcelado * (5/100))
total = precoparcela * parcela
tac = 100.00

print('\nO Produto que custava R$ {:.2f} Na promoção pagando à Vista tem desconto de 5% e vai custar R${:.2f}.'.format(preco,novo))
print('O Produto que custava R$ {:.2f} ao ser parcelado vai custar R${:.2f} por parcela.'.format (preco, precoparcela))
print('Então o total do produto parcelado será de R$ {:.2f} já adicionado a TAC'.format(total+tac))

print('-'*15)
print(' **** Fim **** ')
print('-'*15)