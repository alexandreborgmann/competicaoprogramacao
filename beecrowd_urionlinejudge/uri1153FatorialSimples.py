'''
Author: Alexandre Borgmann
Date: 4/4/2020
URI Online Judge | 1153 Fatorial Simples

Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.
Entrada
A entrada contém um valor inteiro N (0 < N < 13).
Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.

Exemplo de Entrada
4
Exemplo de Saída
24
'''
def fatorial(n):
    if(n<=1):
        return 1
    else:
        return n * fatorial(n-1)

f = int(input(""))
print(fatorial(f))