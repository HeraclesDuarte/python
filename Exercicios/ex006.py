print('\n === Desafio 6 Crie ===\n\n'
      'Faça um algoritmo que leia um número \n'
      'e mostre o seu dobro, Triplo \n'
      'e a sua Raiz Quadrada\n')


n = int(input('Digite o numero: '))
d = n*2
t = n*3
r = n**0.5
print('Nº Digitado é : {:^4} \n'
      'Onde e dobro é: {:^4} \n'
      'o Triplo fica : {:^4} \n'
      'Raiz Quadrada : {:^4.2f}'.format(n, d, t, r))

print('Raiz Quadrada : {:^4.2f}'.format(pow(n, (1/2))))