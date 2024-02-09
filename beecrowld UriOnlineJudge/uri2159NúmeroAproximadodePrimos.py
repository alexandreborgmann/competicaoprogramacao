'''
Autor: Alexandre Borgmann
Data: 20/04/2020
URI Online Judge | 2159 Número Aproximado de Primos

Schoenfeld e Rosser publicaram em 1962 um artigo descrevendo um valor mínimo e máximo para a quantidade de números primos até n,
para n ≥ 17. Esta quantidade é representada pela função (n) e a fórmula é mostrada abaixo.

Sua tarefa é, dado um natural n, calcular o mínimo e máximo do intervalo para o número aproximado de primos até n.
Entrada
A entrada é um número natural n (17 ≤ n ≤ 109).
Saída
A saída são dois valores P e M com 1 casa decimal cada, tal que P < (n) < M, de acordo com a fórmula dada acima.
Os valores devem ser separados por um espaço em branco.

Exemplos de Entrada
17
50
100
Exemplos de Saída
6.0 7.5
12.8 16.0
21.7 27.3
'''
import math

numero = int(input(""))
if numero<17 or numero>10**9:
    print("(17 ≤ n ≤ 109)")
    exit(1)
p = numero / math.log(numero)
m = p * 1.25506
print("{:.1f} {:.1f}".format(p,m))

