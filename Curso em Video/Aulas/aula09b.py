frase = '   Curso em Vídeo Python   '
frase2 = 'Curso em Vídeo Python'
dividido = frase2.split()

print('1  = ',frase[3])
print('2  = ',frase[3:13])
print('3  = ',frase[:13])
print('4  = ',frase[13:])
print('5  = ',frase[1:15])
print('6  = ',frase[1:15:2])
print('7  = ',frase[1::2])
print('8  = ',frase[::2])
print('9  =  Oi')

print("""10 =  Texto Longo, Texto Longo, Texto Longo, Texto Longo, Texto Longo, 
      Texto Longo, Texto Longo, Texto Longo, Texto Longo, Texto Longo, Texto 
      Longo, Texto Longo, Texto Longo, Texto Longo, Texto Longo, Texto Longo, 
      Texto Longo, Texto Longo, Texto Longo, Texto Longo, Texto Longo, 
      Texto Longo, Texto Longo, """)


print('11 = Quantas vezes tem a letra o minusculo = ',frase.count('o'))
print('12 = Quantas vezes tem a letra o Maiusculo = ',frase.count('O'))

print('13 = Quantas vezes tem a letra o Maiusculo agora usando o Upper= ',frase.upper().count('O'))

print('14 = Qual o tamanho da frase quantos caracteres usando len = ', len(frase))

print('15 = Qual o tamanho da frase quantos caracteres usando len com espaços = ', len(frase))

print('16 = Qual o tamanho da frase quantos caracteres usando len e strip que remove espaços = ', len(frase.strip()))

print('17 = Usando o Replace trocando Python por Android =', (frase.replace('Python', 'Android')))

print('18 =', frase2.replace('Python', 'Android'))

print(('19 = A palavra curso esta dentro da frase ? = '),('Curso'in frase))

print('20 = A palavra curso esta dentro da frase ? = ', (frase2.find('Curso')))

print('21 = Existe Vídeo dentro da frase ? = ', (frase2.find('Vídeo')))

print('22 = Existe vídeo dentro da frase em minusculo? = ', (frase2.find('vídeo')))

print('23 = Existe vídeo dentro da frase em minusculo? só que usando a função que muda tudo para minusculo  = ', (frase2.lower().find('vídeo')))

print('24 = Dividido usando o comando split = ', (frase2.split()))

print('25 = Dividido mostrando apenas o dividido ZERO da minha lista que é o primeira item letra da minha lista = ', (dividido[0]))

print('26 = Agora dentro do Dividido eu quero mostrar a posição 2 da minha lista = ', (dividido[2]))

print('27 = Agora dentro do Dividido quero mostrar a posição 2 da minha lista e apenas a letra 3 = ', (dividido[2][3]))
