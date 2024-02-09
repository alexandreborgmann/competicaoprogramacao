'''
Autor: Alexandre Borgmann
Data: 05/04/2020
URI Online Judge | 1186 Conta

Dois amigos pedem ao atendente de uma lanchonete propor um desafio, de modo que quem acertasse mais, não precisaria pagar a conta.
Então foi proposto o seguinte: Dado o seguinte somatório abaixo, informar o resultado, com uma quantidade de termos no mesmo:
S = 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 ...
Escreva um programa que, dada uma quantidade de termos, informar o resultado do somatório acima.
Entrada
Um número inteiro C será informado, que será a quantidade de casos de teste.
Cada caso de teste inicia com um número inteiro N (1 ≤ N ≤ 1000), indicando a quantidade de termos da soma.
Saída
Para cada caso de teste imprima um número S, que é o resultado da soma dos N termos da expressão.

Exemplo de Entrada
3
11
7
18
Exemplo de Saída
1
1
0
'''
while True:
    n = int(input(''))
    if(n<1 or n>1000):
        print("Digite entre N(1 ≤ N ≤ 1000")
        conintue
    break

for i in range(n):
    x=int(input(""))
    if(x%2==0):
        print("0")
    else:
        print("1")





