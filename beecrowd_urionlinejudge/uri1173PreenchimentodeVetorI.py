'''
Author: Alexandre Borgmann
Date: 4/4/2020
URI Online Judge | 1173 Preenchimento de Vetor I

Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10].
Em cada posição subsequente, coloque o dobro do valor da posição anterior.
Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente.
Mostre o vetor em seguida.
Entrada
A entrada contém um valor inteiro (V<=50).
Saída
Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i.
O primeiro número do vetor N (N[0]) irá receber o valor de V.

Exemplo de Entrada
1
Exemplo de Saída
N[0] = 1
N[1] = 2
N[2] = 4
'''
vetor = []
n = int(input(""))
if(n>50):
    print("valor invalido deve ser <=50")
else:
    for i in range(10):
        vetor.append(n)
        n*=2
        print('N[{}] = {}'.format(i,vetor[i]))
