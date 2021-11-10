# '''Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome.'''

nome = str(input('Escreva um nome completo: ')).strip()
nomed = nome.split()
print('O primeiro nome é:{}'.format(nomed[0]))
print('O Ultimo nome é:{}'.format(nomed[len(nomed)-1]))

