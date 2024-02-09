'''
Autor: Alexandre Borgmann
Data: 11/04/2020
URI Online Judge | 1064 Positivos e Média

Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.
Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.
Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

Exemplo de Entrada
7
-5
6
-3.4
4.6
12
Exemplo de Saída
4 valores positivos
7.4
'''
soma=0
positivo=0
for i in range(6):
    a = float(input())
    if(a>0):
        positivo+=1
        soma+=a
print(positivo,'valores positivos')
print("{:.1f}".format(soma/positivo))