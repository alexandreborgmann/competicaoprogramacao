'''
Autor: Alexandre Borgmann
Data: 10/04/2020
Sololearn Fruit Bowl

You have a bowl on your counter with an even number of pieces of fruit in it.
Half of them are bananas, and the other half are apples. You need 3 apples to make a pie.

Task
Your task is to evaluate the total number of pies that you can make with the apples that are in your bowl given to total amount
of fruit in the bowl.

Input Format
An integer that represents the total amount of fruit in the bowl.

Output Format
An integer representing the total number of whole apple pies that you can make.

Sample Input
26

Sample Output
4
Você tem uma tigela no seu balcão com um número par de pedaços de frutas.
Metade deles são bananas e a outra metade são maçãs. Você precisa de 3 maçãs para fazer uma torta.

Tarefa
Sua tarefa é avaliar o número total de tortas que você pode fazer com as maçãs que estão na sua tigela, dadas a quantidade total
de frutas na tigela.

Formato de entrada
Um número inteiro que representa a quantidade total de frutas na tigela.

Formato de saída
Um número inteiro representando o número total de tortas de maçã inteiras que você pode fazer.

Entrada de amostra
26

Saída de amostra
4
'''
import math

quantidade=int(input(""))
print(math.trunc((quantidade/2)/3))

