'''
Autor: Alexandre Borgmann
Data: 16/04/2020
URI Online Judge | 1132 Múltiplos de 13

Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.

Sample Input
100
200
Sample Output
13954
'''
a=int(input(""))
b=int(input(""))
if(a>b):
    i=b
    f=a+1
else:
    i=a
    f=b+1
soma=0
for l in range(i, f):
    if(l%13!=0):
        soma+=l
print(soma)
