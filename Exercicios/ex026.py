'''Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em
que posição ela aparece a última vez.'''

frase = str(input('Digite uma Frase: ')).lower().strip()
print ('A Letra A na frase Aparece {} Vezes'.format (frase.count('a')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra A apareceu pela última vez na posição {}'.format(frase.rfind('a')+1))






