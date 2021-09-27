nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecher {:20}! '.format(nome))
print('Prazer em te conhecher {:=^20}'.format(nome))

n1 = int(input('Um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A Soma Vale: {} , O Produto é: {}, \n A Divisão e: {:.3f}, Resultado do Resto e: {},'.format(s,m,d,di),end='')
print( 'E a Potencia: {}'.format(e))