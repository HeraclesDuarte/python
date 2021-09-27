print ('++++Desafio 8++++\n Escreva um programa que Leia um Valor em Metros\n e o exiba convertido em centimetros e Milimetros\n')
'''
km ,    hm,     dam,   m,  dm,     cm,     mm
0.0001  0.001   0.1    1  1.0,    10.0    100.0
'''
n1 = float(input('Informe uma Distância em Metros: '))
print('A medida é {} metros vai corresponder a:\n'.format(n1))

dm = float(n1)*10
cm = float(n1)*100
mm = float(n1)*1000
dam = float(n1)/10
hm = float(n1)/100
km = float(n1)/1000

print ('A medida é: {:.0f} em dm'.format(dm))
print ('A medida é: {:.0f} em cm'.format(cm))
print ('A medida é: {:.0f} em mm'.format(mm))
print('A medida é: {} em dam'.format(dam))
print('A medida é: {} em hm'.format(hm))
print ('A medida é: {} em KM'.format(km))