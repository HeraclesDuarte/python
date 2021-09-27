'''----------------------Falso Não Digite nada se digitar e Verdadeiro------------------------'''
print ('Falso ou Verdadeiro')
n = bool(input('Digite um Valor para Verdade ou Não digite nada para Falso e tecle Enter: '))
print(n)
'''-------------------------------------------------------------------------------------------'''

'''-----------------------Verificar se é conteudo e Numerico----------------------------------'''
print ('Verificar se é Numerico')
n = input('Digite Algo para Validar é Numerico: ')
print(n.isnumeric()) #é Numerico?
'''--------------------------------------------------------------------------------------------'''

'''----------------------Verificar se é o conteudo e uma Letra---------------------------------'''
print ('Verificar se é Letra')
n = input('Digite Algo para Validar é Letra: ')
print(n.isalpha()) #é letra?
'''-------------------------------------------------------------------------------------------'''

'''----------------------Verificar se é o conteudo e AlfaNumerico-----------------------------'''
print ('Verificar se é ALFA_Numerico')
n = input('Digite Algo para Validar é ALFA_Numerico: ')
print(n.isalnum()) #é ALFA_Numerico?
'''-------------------------------------------------------------------------------------------'''

'''--------------------Verificar se é o conteudo e CAIXA Alta ou não -------------------------'''
print ('Verificar se é CAIXA Alta ou não')
n = input('Digite Algo para Validar é CAIXA Alta ou não: ')
print(n.isupper()) #é CAIXA Alta?
'''-------------------------------------------------------------------------------------------'''