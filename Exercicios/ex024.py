# Exercício Python 24:
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma Cidade: ')).strip()
#dividido = (cidade.split())

#print ('Cidade: {} '.format((dividido[0])))
print(('A palavra Santo esta dentro da frase ? = '),('Santo'in cidade))
