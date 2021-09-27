a = (input('Digite Algo: '))

# Verificar se é String
print\
    ('O Tipo Primitivo do valor Digitado é: {} '
     ''.format(type(a)))

# Verificar se tem Espaços
print\
    ('Só Tem espaços? {} '
     ''.format((a.isspace())))

# Verificar se é conteudo e Numerico
print\
    ('É Numerico? {} '
     ''.format((a.isnumeric())))#é Numerico?

# Verificar se o conteudo e uma Letra
print\
    ('O conteudo e uma Letra/Alfabético? {} '
     ''.format((a.isalpha())))#é letra?

# Verificar se é o conteudo e AlfaNumerico
print\
    ('O conteudo e AlfaNumerico? {} '
     ''.format((a.isalnum()))) #é ALFA_Numerico?

# Verificar se é o conteudo e CAIXA Alta
print\
    ('O conteudo e Maiusculo? {} '
     ''.format((a.isupper()))) #é CAIXA Alta?

# Verificar se é o conteudo e Minuscula
print\
    ('O conteudo e Minusculo? {} '
     ''.format((a.islower()))) #Não CAIXA Alta?

# Verificar se é Decimal
print\
    ('O conteudo e Decimal? {} '
     ''.format((a.isdecimal()))) #É Decimal?

# Verificar se Esta Capitalizada (Maiuscula e Minuscula Juntos)
print\
    ('O conteudo e Capitalizada? {} '
     ''.format((a.istitle()))) #Esta Capitalizada?