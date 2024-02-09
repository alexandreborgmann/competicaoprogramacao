'''
Autor: Alexandre Borgmann
Data: 01/04/2020
URI Online Judge | 1013 O Maior

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
Utilize a fórmula:

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Um segundo passo, portanto é necessário para chegar no resultado esperado.
Entrada
O arquivo de entrada contém três valores inteiros.
Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
Exemplos de Entrada/Exemplos de Saída
7 14 106
106 eh o maior
217 14 6
217 eh o maior
'''

linha = input("")
variaveis = linha.split()
a = int(variaveis[0])
b = int(variaveis[1])
c = int(variaveis[2])

maiorab=(a+b+abs(a-b))/2
maior=(maiorab+c+abs(maiorab-c))/2
print(int(maior),'eh o maior')
