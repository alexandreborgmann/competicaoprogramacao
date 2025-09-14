'''
Author: Alexandre Borgmann
Date: 4/11/2020
URI Online Judge | 1071 Soma de Impares Consecutivos I

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
Entrada
O arquivo de entrada contém dois valores inteiros.
Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

Exemplo de Entrada
6
-5

15
12
Exemplo de Saída
5
13
'''
SomaImpar = 0
x = int(input(""))
y = int(input(""))

if(x>y):
  inicio=y+1
  fim=x
else:
  inicio=x+1
  fim=y

#print('{} {}'.format(inicio,fim))
for j in range(inicio,fim):
    #print('j=',j)
    if(j%2!=0):
        SomaImpar+=j
print(SomaImpar)

