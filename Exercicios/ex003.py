n1 = int(input('Digite o valor: '))
print(type(n1))
print(n1)

n2 = int(input('Digite o segundo numero: '))
print(type(n2))
print(n2)
s = int(n1) + int(n2)
#print('A soma é entre',n1, 'e', n2,'Será igual a:', s) => Formato Antigo
print('A soma entre {0} e {1} Será igual a:{2}!'.format(n1, n2, s,)) #Novo Formato
