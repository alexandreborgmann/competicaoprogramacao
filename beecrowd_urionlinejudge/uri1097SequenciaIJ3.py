'''
Autor: Alexandre Borgmann
Data: 03/04/2020
URI Online Judge | 1097 Sequencia IJ 3

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
'''
for i in range(1,10,2):
    for j in range(i+6,i+3,-1):
        print('I={} J={}'.format(i,j))
