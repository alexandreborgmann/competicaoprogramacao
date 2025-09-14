'''
Autor: Alexandre Borgmann
Data: 02/04/2020
URI Online Judge | 1067 Números Ímpares

Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

Entrada
O arquivo de entrada contém 1 valor inteiro qualquer.

Saída
Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

Exemplo de Entrada	Exemplo de Saída
8

1
3
5
7
'''
while True:
    x = int(input())
    if(x>=1 and x<=1000):
      break;
    print("Informe um numero entre 1-1000")

for i in range(1,x+1,2):
    print(i)



