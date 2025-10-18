'''
Autor: Alexandre Borgmann
Data: 10/04/2020
Sololearn Skee-Ball

You are playing a game at your local arcade, and you receive 1 ticket from the machine for every 12 points that you score.
You want to purchase a squirt gun with your tickets.
Given your score, and the price of the squirt gun (in tickets) are you able to buy it?

Task
Evaluate whether or not you have scored high enough to earn enough tickets to purchase the squirt gun at the arcade.

Input Format
The first input is an integer value that represents the points that you scored playing, and the second input is an integer
value that represents the cost of the squirt gun (in tickets).

Output Format
A string that say 'Buy it!' if you will have enough tickets, or a string that says 'Try again' if you will not.

Sample Input
500
40

Sample Output
Buy it!

Você está jogando no seu fliperama local e recebe 1 bilhete da máquina para cada 12 pontos que marcar.
Você deseja comprar uma pistola de água com seus ingressos.
Dada a sua pontuação e o preço da pistola de água (em ingressos), você pode comprá-la?

Tarefa
Avalie se você pontuou alto ou não o suficiente para ganhar ingressos suficientes para comprar a pistola de água no fliperama.

Formato de entrada
A primeira entrada é um valor inteiro que representa os pontos que você marcou jogando e a segunda entrada é um número inteiro
valor que representa o custo da pistola de água (em bilhetes).

Formato de saída
Uma string que diz 'Compre!' se você tiver ingressos suficientes ou uma string que diga 'Tente novamente', se não tiver.

Entrada de amostra
500
40.

Saída de amostra
Compre!
'''
pontos = int(input(""))
custoPistola = int(input(""))
if(custoPistola<=pontos/12):
    print("Buy it!")
else:
    print("Try again")
