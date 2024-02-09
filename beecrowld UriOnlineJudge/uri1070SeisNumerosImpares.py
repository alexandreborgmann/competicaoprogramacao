'''
Autor: Alexandre Borgmann
Data: 03/04/2020
URI Online Judge | 1070 Seis Números Ímpares

Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

Exemplo de Entrada	Exemplo de Saída
8s

9
11
13
15
17
19
'''
x = int(input())
for i in range(x,x+12,1):
    if(i%2!=0):
        print(i)



