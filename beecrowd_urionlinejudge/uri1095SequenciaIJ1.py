'''
Autor: Alexandre Borgmann
Data: 03/04/2020
URI Online Judge | 1095 Sequencia IJ 1

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

Exemplo de Entrada	Exemplo de Saída
I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0
'''
i=1
for j in range(60,-1,-5):
    print('I={} J={}'.format(i,j))
    i+=3




