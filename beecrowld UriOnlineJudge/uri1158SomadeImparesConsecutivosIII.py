'''
Author: Alexandre Borgmann
Date: 4/4/2020
URI Online Judge | 1158 Soma de Ímpares Consecutivos III

Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste de dois inteiros X e Y.
Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar.
Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13
Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.
Saída
Imprima a soma dos consecutivos números ímpares a partir do valor X.

Exemplo de Entrada
2
4 3
11 2
Exemplo de Saída
21
24


'''
n = int(input())
for i in range(n):
    linha = input("")
    campos = linha.split()

    x = int(campos[0])
    y = int(campos[1])
    SomaImpar = 0
    conta=0
    while(y>conta):
        if(x%2!=0):
            SomaImpar+=x
            conta+=1
        x+=1
    print(SomaImpar)


