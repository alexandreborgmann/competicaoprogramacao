'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Carrot Cake

You are packing boxes of carrots for a farm co-op, and you are supposed to evenly distribute all of the carrots that you have
into the boxes.
The total number of carrots in each box doesn't matter as long as you distribute them evenly, and there are not enough leftover to
put another carrot in each box. Anything that you have left over, you get to keep.
You need 7 carrots to make the cake the way that you want to.

Task:
Determine if you will have enough leftover carrots to make your cake.

Input Format:
Two integer values. The first represents the number of carrots that you start with, and the second is the number of boxes that
need to be packed into.

Output Format:
A string that says 'Cake Time' if you have enough, or that says 'I need to buy X more' where X is the extra amount you need for
your cake.

Sample Input:
100
10

Sample Output:
I need to buy 7 more
'''
import math

cenouras = int(input(""))
caixas = int(input(""))
if cenouras/caixas==math.trunc(cenouras/caixas):
    print("I need to buy 7 more")
else:
    comprar = cenouras-(caixas*math.trunc(cenouras/caixas))
    if comprar<=7:
        print("I need to buy {} more".format(7-comprar))
    else:
        print("Cake Time")