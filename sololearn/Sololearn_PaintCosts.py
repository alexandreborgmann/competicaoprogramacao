'''
Autor: Alexandre Borgmann
Data: 10/04/2020
Sololearn Paint costs

You are getting ready to paint a piece of art.
The canvas and brushes that you want to use will cost 40.00.
Each color of paint that you buy is an additional 5.00.
Determine how much money you will need based on the number of colors that you want to buy if tax at this store is 10%.

Task
Given the total number of colors of paint that you need, calculate and output the total cost of your project rounded up to
the nearest whole number.

Input Format
An integer that represents the number of colors that you want to purchase for your project.

Output Format
A number that represents the cost of your purchase rounded up to the nearest whole number.

Sample Input
10
Sample Output
99

Você está se preparando para pintar uma obra de arte.
A tela e os pincéis que você deseja usar custarão 40,00.
Cada cor de tinta que você compra é um adicional de 5,00.
Determine quanto dinheiro você precisará com base no número de cores que deseja comprar se o imposto nesta loja for 10%.

Tarefa
Dado o número total de cores de tinta necessárias, calcule e produza o custo total do seu projeto arredondado para
o número inteiro mais próximo.

Formato de entrada
Um número inteiro que representa o número de cores que você deseja comprar para o seu projeto.

Formato de saída
Um número que representa o custo da sua compra arredondado para o número inteiro mais próximo.

Entrada de amostra
10

Saída de amostra
99
'''
import math

cores = int(input(""))
valor=(40+cores*5)
print(math.ceil(valor+valor*0.10))
