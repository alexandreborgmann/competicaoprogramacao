'''
Autor: Alexandre Borgmann
Data: 02/04/2020
URI Online Judge | 1143 Quadrado e ao Cubo

Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
5

1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
'''
while True:
    x = int(input())
    if(x>=1 and x<=1000):
      break;
    print("Informe um numero entre 1-1000")

for i in range(1,x+1):
    for potencia in range(1,4):
        if(potencia==3):
            print(i ** potencia)
        else:
            print(i ** potencia, end=" ")





