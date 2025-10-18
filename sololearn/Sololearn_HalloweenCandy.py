'''
Autor: Alexandre Borgmann
Data: 10/04/2020
Sololearn Halloween Candy

You go trick or treating with a friend and all but three of the houses that you visit are giving out candy.
One house that you visit is giving out toothbrushes and two houses are giving out dollar bills.
Task
Given the input of the total number of houses that you visited, what is the percentage chance that one random item pulled from
your bag is a dollar bill?

Input Format
An integer (>=3) representing the total number of houses that you visited.

Output Format
A percentage value rounded up to the nearest whole number.

Sample Input
4

Sample Output
50

Você gosta de doces ou travessuras com um amigo e quase todas as casas que você visita estão distribuindo doces.
Uma casa que você visita está dando escovas de dentes e duas casas estão dando notas de dólar.
Tarefa
Dada a entrada do número total de casas que você visitou, qual é a chance percentual de retirada de um item aleatório
sua mala é uma nota de um dólar?

Formato de entrada
Um número inteiro (> = 3) representando o número total de casas que você visitou.

Formato de saída
Um valor percentual arredondado para o número inteiro mais próximo.

Entrada de amostra
4

Saída de amostra
50
'''
import math

entrada=int(input(""))
if(entrada<3):
    print("Valor informado deve ser >=3")
    exit(1)
print(math.ceil(2*100.00/entrada))

