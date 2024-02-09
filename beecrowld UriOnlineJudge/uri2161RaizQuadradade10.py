'''
Author: Alexandre Borgmann
Date: 6/4/2020
URI Online Judge | 2161 Raiz Quadrada de 10

Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas.
Esse método usa como denominador uma repetição de frações.
Essa repetição pode ser feita uma quantidade específica de vezes.
Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz quadrada de 10, temos a fórmula abaixo.

Sua tarefa é, dado o número N de repetições, calcular o valor aproximado da raiz quadrada de 10.
Entrada
A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições do denominador na fração continuada.
Saída
A saída é o valor aproximado da raiz quadrada com 10 casas decimais.

Exemplos de Entrada
0
1
5
Exemplos de Saída
3.0000000000
3.1666666667
3.1622776623
'''
try:
    n = int(input(""))
except:
    exit(0)
if(n<0 or n>100):
    exit(0)
decimal=0.0
for i in range(n):
    decimal += 6.0
    decimal = 1.0 / decimal
print("{:.10f}".format(3+decimal))
