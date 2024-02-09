'''
Author: Alexandre Borgmann
Date: 4/4/2020
URI Online Judge | 1157 Divisores I

Ler um número inteiro N e calcular todos os seus divisores.
Entrada
O arquivo de entrada contém um valor inteiro.
Saída
Escreva todos os divisores positivos de N, um valor por linha.

Exemplo de Entrada
6
Exemplo de Saída
1
2
3
6
'''
n = int(input(""))
for i in range(1,n+1):
    if(n%i==0):
        print(i)