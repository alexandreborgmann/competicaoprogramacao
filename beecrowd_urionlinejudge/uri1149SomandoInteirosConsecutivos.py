'''
Author: Alexandre Borgmann
Date: 4/4/2020
URI Online Judge | 1149 Somando Inteiros Consecutivos

Faça um algoritmo para ler um valor A e um valor N.
Imprimir a soma de A para cada i com os valores (0 <= i <= N-1).
Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.
Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos.
Todos os valores estão na mesma linha.
Saída
A saída contém apenas um valor inteiro.

Exemplo de Entrada
3 2
3 -1 0 -2 2
Exemplo de Saída
7
7

soma=0
linha = input("")
campos = linha.split()

a = int(campos[0])
n = int(campos[1])
while True:
    if(n>0):
        break
    n=int(input(""))

for i in range(n):
    soma+=(a+i)
print(soma)
'''
soma=0
linha = input("")
campos = linha.split()

a = int(campos[0])
i=1
while(len(campos)>i):
    n = int(campos[i])
    if(n>0):
        break
    i+=1

for i in range(n):
    soma+=(a+i)
print(soma)