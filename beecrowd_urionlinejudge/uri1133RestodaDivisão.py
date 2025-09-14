'''
Autor: Alexandre Borgmann
Data: 16/04/2020
URI Online Judge | 1132 Múltiplos de 13

Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Sample Input	Sample Output
10
18

12
13
17
'''
a=int(input(""))
b=int(input(""))
if(a>b):
    i=b+1
    f=a
else:
    i=a+1
    f=b
soma = 0
for l in range(i, f):
    if(l%5 in (2,3)):
        print(l)

