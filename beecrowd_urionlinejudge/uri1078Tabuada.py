'''
Autor: Alexandre Borgmann
Data: 12/04/2020
URI Online Judge | 1078 Tabuada

Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:
1 x N = N      2 x N = 2N        ...       10 x N = 10N
Entrada
A entrada contém um valor inteiro N (2 < N < 1000).
Saída
Imprima a tabuada de N, conforme o exemplo fornecido.

Exemplo de Entrada
140
Exemplo de Saída
1 x 140 = 140
2 x 140 = 280
3 x 140 = 420
4 x 140 = 560
5 x 140 = 700
6 x 140 = 840
7 x 140 = 980
8 x 140 = 1120
9 x 140 = 1260
10 x 140 = 1400
'''
n = int(input(""))
if(n<2 or n>1000):
    exit(1)
for i in range(1,11,1):
    print(i,"x",n,"=",i*n)
