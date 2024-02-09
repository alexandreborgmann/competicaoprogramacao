'''
Autor: Alexandre Borgmann
Data: 12/04/2020
URI Online Judge | 1075 Resto 2

Leia um valor inteiro N.
Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.
Entrada
A entrada contém um valor inteiro N (N < 10000).
Saída
Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

Exemplo de Entrada
Exemplo de Saída
13
2
15
28
41
...
'''
n = int(input(""))
if(n>10000):
    exit(1)
for i in range(1,10001,1):
    if(i%n==2):
        print(i)
