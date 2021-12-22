'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''

''''REGRA PARA DESCOBRIR SE POR FORMAR UM TRIANGULO'''

'''As 3 retas tem que formar um Triangulo para isso existe uma regra matematica que diz:

um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados
e menor que a soma dos outros dois lados.'''

print('-='*20)
print('Analisador de TriAngulo')
print('-='*20)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os Segmentos NÃO PODEM FORMAR um triângulo!')