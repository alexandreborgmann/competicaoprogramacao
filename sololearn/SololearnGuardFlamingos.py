'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Guard Flamingos

You decide to add a pink flamingo lawn ornament every 2 feet around the perimeter of your yard.
How many flamingos do you need to purchase?

Task:
Given the length and width of your rectangular yard, determine how many flamingos your should buy to put one every 2 feet
along the edges of your yard.

Input Format:
Two integer values that represent the length and width of your front yard.

Output Format:
An integer that represents the total number of flamingos that you should purchase.

Sample Input:
10
10

Sample Output:
20
'''
comprimento = int(input(""))
largura = int(input(""))
print("{:.0f}".format((comprimento/2+largura/2)*2))