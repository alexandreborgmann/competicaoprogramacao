'''
Author: Alexandre Borgmann
Date: 4/4/2020
URI Online Judge | 1175 Troca em Vetor I

Faça um programa que leia um vetor N[20].
Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º.
Mostre o vetor modificado.
Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.
Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.

Exemplo de Entrada
0
-5
...
63
230
Exemplo de Saída
N[0] = 230
N[1] = 63
...
N[18] = -5
N[19] = 0
'''
vetor = []
for i in range(20):
    vetor.append(int(input("")))

j=len(vetor)-1
for i in range((int)(len(vetor)/2)):
    aux=vetor[j]
    vetor[j]=vetor[i]
    vetor[i]=aux;
    j-=1

for i in range(len(vetor)):
    print('N[{}] = {}'.format(i,vetor[i]))


