'''
Autor: Alexandre Borgmann
Data: 11/04/2020
URI Online Judge | 1060 Números Positivos

Faça um programa que leia 6 valores.
Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
A seguir, mostre a quantidade de valores positivos digitados.
Entrada
Seis valores, negativos e/ou positivos.
Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.

Exemplo de Entrada
7
-5
6
-3.4
4.6
12
Exemplo de Saída
4 valores positivos

'''
positivo=0
for i in range(6):
    a = float(input())
    if(a>0):
        positivo+=1
print(positivo,'valores positivos')
