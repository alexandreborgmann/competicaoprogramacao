'''
Autor: Alexandre Borgmann
Data: 20/04/2020
URI Online Judge | 2164 Fibonacci Rápido

A fórmula de Binet é uma forma de calcular números de Fibonacci.

Sua tarefa é, dado um natural n, calcular o valor de Fibonacci(n) usando a fórmula acima.
Entrada
A entrada é um número natural n (0 < n ≤ 50).
Saída
A saída é o valor de Fibonacci(n) com 1 casa decimal utilizando a fórmula de Binet dada.

Exemplos de Entrada
1
2
3
Exemplos de Saída
1.0
1.0
2.0
'''
import math

numero = int(input(""))
if numero<0 or numero>50:
    print("(0 < n ≤ 50)")
    exit(1)
f = (((1 + math.sqrt(5))/2)**numero - ((1 - math.sqrt(5))/2)**numero)/math.sqrt(5)
print("{:0.1f}".format(f))

