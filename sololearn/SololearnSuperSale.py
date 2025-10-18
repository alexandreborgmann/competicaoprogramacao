'''
Autor: Alexandre Borgmann
Data: 15/04/2020
Sololearn Super Sale

Your favorite store is having a sale!
You pay full price for the most expensive item that you get, but then you get 30% off of everything else in your purchase!
How much are you going to save?
Sales tax is 7%.
Also, you leave anything below a dollar in your saving as a tip to the seller.
If your saving is a round amount, you don't leave any tips.

Task:
Given the prices of items you want to purchase, determine how much you will save during your shopping!

Input Format:
An string of numbers separated by commas that represent the prices for all of the items that you want to purchase (without tax).

Output Format:
An integer number that represents the total savings that you got for shopping during the sale.

Sample Input:
100.25,80.99,40.00

Sample Output:
38
'''
import math

linha=input("")
valores = [float(i) for i in linha.split(",")]
valoresOrdenados =sorted(valores, reverse=True)
totalComDesconto=0
for i in valoresOrdenados[1:]:
    totalComDesconto+=i
desconto = (totalComDesconto+(totalComDesconto*0.07))*.30
print(math.trunc(desconto))
