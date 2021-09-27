# Aqui Digita o Tipo
a = (input('\nDigite Algo: \n'))

# Verificar se é String
print('O Tipo Primitivo do valor Digitado é:', type(a))

# Verificar se tem Espaços
print('Só Tem espaços? ', a.isspace())

# Verificar se é conteudo e Numerico
print('É Numerico? ', a.isnumeric())#é Numerico?

# Verificar se o conteudo e uma Letra
print('O conteudo e uma Letra/Alfabético? ', a.isalpha())#é letra?

# Verificar se é o conteudo e AlfaNumerico
print('O conteudo e AlfaNumerico? ', a.isalnum()) #é ALFA_Numerico?

# Verificar se é o conteudo e CAIXA Alta
print('O conteudo e CAIXA Alta/Maiusculas? ', a.isupper()) #é CAIXA Alta?

# Verificar se é o conteudo e Minuscula
print('O conteudo e Minuscula? ', a.islower()) #Não CAIXA Alta?

# Verificar se é Decimal
print('O conteudo e Decimal? ', a.isdecimal()) #É Decimal?

# Verificar se Esta Capitalizada (Maiuscula e Minuscula Juntos)
print('O conteudo e Capitalizada? ', a.istitle()) #Esta Capitalizada?