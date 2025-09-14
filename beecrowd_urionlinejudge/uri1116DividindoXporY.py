'''
Autor: Alexandre Borgmann
Data: 03/04/2020
URI Online Judge | 1116 Dividindo X por Y

Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

Exemplo de Entrada	Exemplo de Saída
3
3 -2
-8 0
0 8

-1.5
divisao impossivel
0.0
'''

quantidadeLer = int(input())

for i in range(quantidadeLer):
    linha = input("")
    campos = linha.split()
    try:
        dividendo = int(campos[0])
    except ValueError:
        dividendo=0

    try:
        divisor = int(campos[1])
    except ValueError:
        divisor=0

    try:
        resultado=dividendo/divisor
    except (ValueError,ZeroDivisionError):
         print('divisao impossivel')

    if(divisor!=0):
        print('{:.1f}'.format(resultado))
