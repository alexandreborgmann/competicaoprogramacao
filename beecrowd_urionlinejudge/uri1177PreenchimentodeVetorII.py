'''
Author: Alexandre Borgmann
Date: 4/5/2020
URI Online Judge | 1177 Preenchimento de Vetor II

Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 repetidas vezes,
conforme exemplo abaixo.
Imprima o vetor N.
Entrada
A entrada contém um valor inteiro T (2 ≤ T ≤ 50).
Saída
Para cada posição do vetor, escreva "N[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.

Exemplo de Entrada
3
Exemplo de Saída
N[0] = 0
N[1] = 1
N[2] = 2
N[3] = 0
N[4] = 1
N[5] = 2
N[6] = 0
N[7] = 1
N[8] = 2
...

'''
vetor = []
n = int(input(""))
if(n<2 or n>50):
    print("valor invalido deve ser 2 ≤ T ≤ 50)")
else:
    j=0
    for i in range(1000):
        vetor.append(j)
        j+=1
        if(j==n):
            j=0
        print('N[{}] = {}'.format(i,vetor[i]))
