'''
Autor: Alexandre Borgmann
Data: 05/04/2020
URI Online Judge | 1957 Converter para Hexadecimal

Os dados armazenados no computador estão em binário.
Uma forma econômica de ver estes números é usar a base 16 (hexadecimal).
Sua tarefa consiste em escrever um programa que, dado um número natural na base 10, mostre sua representação em hexadecimal.
Entrada
A entrada é um número inteiro positivo V na base 10 (1 ≤ V ≤ 2 x 109).
Saída
A saída é o mesmo número V na base 16 em uma única linha (não esqueça do caractere de fim-de-linha).
Use letras maiúsculas, conforme os exemplos.

Exemplos de Entrada
10
15
16
31
65535
Exemplos de Saída
A
F
10
1F
FFFF

Prova 1 de Programação de Computadores da UNILA (2015/2)
'''
try:
    while True:
        n = int(input(''))
        if(n<1 or n>2000000000):
            break
        print('{:x}\n'.upper().format(n),end="")
except:
    print("",end="")





