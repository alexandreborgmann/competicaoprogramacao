'''
Autor: Alexandre Borgmann
Data: 11/04/2020
URI Online Judge | 1066 Pares, Ímpares, Positivos e Negativos

Leia 5 valores Inteiros.
A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e
quantos valores digitados foram negativos.
Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

Exemplo de Entrada
-5
0
-3
-4
12
Exemplo de Saída
3 valor(es) par(es)
2 valor(es) impar(es)
1 valor(es) positivo(s)
3 valor(es) negativo(s)
'''
pares=0
impares=0
positivo=0
negativo=0
for i in range(5):
    a = int(input())
    if(a%2==0):
        pares+=1
    else:
        impares+=1
    if(a>0):
        positivo+=1
    elif(a<0):
        negativo+=1
print(pares,'valor(es) par(es)')
print(impares,'valor(es) impar(es)')
print(positivo,'valor(es) positivo(s)')
print(negativo,'valor(es) negativo(s)')

