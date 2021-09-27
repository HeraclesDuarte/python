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


