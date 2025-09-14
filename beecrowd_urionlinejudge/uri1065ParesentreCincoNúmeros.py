'''
Autor: Alexandre Borgmann
Data: 11/04/2020
URI Online Judge | 1065 Pares entre Cinco Números

Faça um programa que leia 5 valores inteiros.
Conte quantos destes valores digitados são pares e mostre esta informação.
Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

Exemplo de Entrada
Exemplo de Saída
7
-5
6
-4
12
3 valores pares

'''
pares=0
for i in range(5):
    a = int(input())
    if(a%2==0):
        pares+=1
print(pares,'valores pares')