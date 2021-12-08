'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''
'''ver exec 20'''

## MEU JEITO 1

# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))
# n3 = int(input('Terceiro valor: '))
# lista = [n1, n2, n3 ]
# maior = lista
# print('O maior numero digitado foi: {} '.format(max(lista)))
# print('O menor numero digitado foi: {} '.format(min(lista)))

# # MEU JEITO 2
#
# primeiro = int(input('Primeiro valor: '))
# segundo = int(input('Segundo valor : '))
# terceiro = int(input('Terceiro valor: '))
#
# # Achando o maior numero Digitado
# maior = primeiro
#
# if (segundo > maior):
#     maior = segundo
# if (terceiro > maior):
#     maior = terceiro
#
# print('O Maior Valor é{}: '.format(maior))
#
# # Achando o menor número
# menor = primeiro
#
# if (segundo < menor):
#     menor = segundo
# if (terceiro < menor):
#     menor = terceiro
#
# print('O Menor valor é{}: '.format(menor))

#JEITO 1 PROFESSOR

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor : '))
c = int(input('Terceiro valor: '))
if b<a and a<c:
    menor = a
if b<c and b<a:
    menor = b