#Comentario simples

'''
Comentario
em Blocos
'''

print('Olá Mundo') # Aula 1

nome = input('Qual é o seu nome? ')
print('é um grande prazer te conhecer', nome)

int = Numeros inteiro (7,-4, 0,9875) # Aula 3
floot = Numeros Reais ou ponto Flutuante (4.5,0.076, -15.223, 7.0)
bool = Logicos ou Booleanos (True = Verdadeiro / False = Falso)
str = caracteres ou String ('olá Mundo','8888', '7.5','')

print ('a soma vale',s) ==> print ('A soma vale {}'.format(aqui digito o que vai aparecer dentro das chaves))

() - Parenteses
{} - Chaves
[] - Colchetes


Operadores Aritméticos - Aula 7

+ = Soma
- = Subtração
* = Multiplicação
/ = Divisão
** = Potencia
// = Divisão Inteira
% = Resto da Divisão

Ordem de precedencia
1 = ()
2 = **
3 = * / // % ou na ordem que aparecer primeiro
4 = + -


#Alinhamento
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome)) # Escrito em 20 posições alinhado a DIREITA
print('Prazer em te conhecer {:<20}!'.format(nome)) # Escrito em 20 posições alinhado a ESQUERDA
print('Prazer em te conhecer {:^20}!'.format(nome)) # Escrito em 20 posições alinhado a CENTRO
print('Prazer em te conhecer {:=^20}!'.format(nome)) # Escrito em 20 posições alinhado a ESPAÇOS EM BRANCO PREENCHIDOS

Varios Format

n1 = int(input('Um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A Soma Vale: {} , O Produto é: {}, \n ' #\N Quebra de Linha
      'A Divisão e: {:.3f}, Resultado do Resto e: {},'.format(s,m,d,di),end='') #end='' Mantem sem a Quebra de Linha
print( 'E a Potencia: {}'.format(e))

importacao
import math (math é a biblioteca matematica INTEIRA)
from math import sqrt (importa a biblioteca matematica ESPECIFICA)


      ceil (arredonda para cima)
      floor (arredonda para baixo)
      trunc (Trunca ou elimina qq valor da virgula para frente sem arrendondar)
      pow (Power potencia semelhante aos **)
      sqrt (raiz quadrada)
      factorial (Fatorial)

import random => Exibe a informação de forma Randomica (o PC escolhe)
random.choice = Esse escolhe um aleatorio
random.shuffle = Esse exibe todos mas troca as ordens

print('O aluno escolhido foi = {:=^11}.'.format(random.choice(alunos)))


# Regras de Fatiamento (String ou Manipulação de Texto)


frase = 'Curso em Video Python'

# print(frase)

frase[13] = Print/Escreva da posição 13 (Neste caso o Python NÃO ignora a posição 13)
frase[9:13] = Print/Escreva da posição 9 ao 13 (Python ignora a posição 13)
frase[9:13:2] = Print/Escreva da posição 9 ao 13 (Python ignora a posição 13 e pulando de 2 em 2)
frase[9:21] = Print/Escrevada posição 9 ao 21 (Python ignora a posição 21 e não dá erro mesmo que não exista a posição 21)
frase[:5] = Print/Escrevada tudo até a posição 5 (Neste caso o Python NÃO ignora a posição 5)
frase[:15] = Print/Escrevada tudo depois da posição 15 (Neste caso o Python NÃO ignora a posição 15)
frase[9::3]= Print/Escrevada do 9 até o final (MAS O :3 PULANDO DE 3 EM 3)

# Analise

len(frase) = 'len' leia e analise a frase ou a String neste caso a variavel frase tem 21 caracteres
frase.count('o') = 'count' neste caso = Neste caso quantas vezes aparece a letra "o" em minusculo nesta frase teremos 3
frase.count('o,0,13') = count neste caso = faço uma contagem já com o fatiamento então neste caso
                        o Python considera da posição 0 ao 13 e não inclui a posição 13
                        porém do 0 até a posição 12 eu tenho apenas uma letra "o" minuscula


frase.find('deo') = 'find' tem a função de encontrar ou buscar neste caso estamos solicitando ao Python
                            que encontre 'deo' na variavel frase que contem o conteudo 'Curso em Video Python'
                            neste exemplo então temos 'deo' apenas 1 vez nas posições 11 a 13 neste caso ele mostra
                            em quais posições o deo estão.

frase.find('Android') = 'find' neste caso na nossa string não tem 'Android' então o Python retorna o valor -1
                                significa que não existe
'Curso' in frase = Neste caso o operador in diz para o python = existe a palavra CURSO na variavel frase??
                    Logo o Python retorna True que significa sim

# TRANSFORMAÇÃO

Uma string é IMUTAVÉL mas eu consigo manipular ela através de metodos

frase.replace('Python', 'Android') = o 'replace' aqui significa TROCAR e ou reposicionar neste exemplo aqui
                                    o Python vai procurar por 'Python' e vai substituir por 'Android'
                                    neste caso minha string frase mudaria para 'Curso em Video Android'

==> lembrando que essa "substituição" não é na String e sim de forma "secundaria"

frase.upper() = o upper significa MAIUSCULA trocar o que esta minusculo por CAIXA ALTA

frase.lower() = o lower significa minusculo trocar o que esta em CAIXA ALTA para minusculo o contrario do upper

frase.capitalize() = transforma tudo em minusculo da String e mantem só a PRIMEIRA LETRA EM MAIUSCULA da frase

frase.title() = transforma tudo em minusculo da String e mantem só a PRIMEIRA LETRA EM MAIUSCULA de CADA PALAVRA


# DIVISÃO DE STRING

frase.split() tem variss funcionalidades mas basicamente = Ele vai dividir a String tirando os espaços e passando
              a considerar cada palavra como se fosse uma frase e reiniciando os indices / numeração de cada caracter
                ==> ver minuto 26:45 do curso

'-'.join(frase) = Depois que eu faço o split eu posso fazer o 'join' neste caso usando o caracter '-'
                  neste caso ficaria assim "Curso-em-Video-Python"


# mudando a string agora para
# frase='___Aprenda Python__' com espaços em branco antes e depois da Strin

frase.strip() = remove TODOS os espaços inuteis antes e depois da string

frase.rstrip() = remove TODOS os espaços inuteis à DIREITA (no fim) Depois da string por conta do "R" antes do strip

frase.lstrip() = remove TODOS os espaços inuteis à ESQUERDA (no INICIO) da string por conta do "L" antes do strip








