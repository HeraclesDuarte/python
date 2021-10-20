# Exercício Python 24:
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

'''cidade = str(input('Digite o nome de uma Cidade: ')).strip()
print(('A palavra Santo esta dentro da frase: {}'.format(('Santo'in cidade))))'''

#---------------------------------------------------------
#Jeito do Professos
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')