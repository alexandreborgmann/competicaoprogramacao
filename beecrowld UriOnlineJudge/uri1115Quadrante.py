'''
Author: Alexandre Borgmann
Date: 4/4/2020
URI Online Judge | 1115 Quadrante

Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano.
Para cada ponto escrever o quadrante a que ele pertence.
O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).
Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.
Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

Exemplo de Entrada
2 2
3 -2
-8 -1
-7 1
0 2
Exemplo de Saída
primeiro
quarto
terceiro
segundo

'''
def QuadrantesCartesianos(x,y):
    if(x>0 and y>0):
        print("primeiro")
    if(x<0 and y>0):
        print("segundo")
    if(x<0 and y<0):
        print("terceiro")
    if(x>0 and y<0):
        print("quarto")

while True:
    linha = input("")
    campos = linha.split()

    x = int(campos[0])
    y = int(campos[1])
    if(x==0 or y==0):
        break
    QuadrantesCartesianos(x,y)