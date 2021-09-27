'''import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de um {} e igual a : {}'.format(num, math.ceil(raiz)))

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de um {} e igual a : {}'.format(num, math.foor(raiz)))'''

from math import sqrt, ceil
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de um {} e igual a : {}'.format(num, ceil(raiz)))

from math import sqrt, ceil, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de um {} e igual a : {}'.format(num, floor(raiz)))