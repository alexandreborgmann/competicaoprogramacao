'''
Autor: Alexandre Borgmann
Data: 19/04/2020
Sololearn Tax Free

You are shopping at a store that is having a special where you do not have to pay the tax on anything that costs 20 dollars or more!
If you have a list of prices for all of your items, what is your total once the tax is added in? Tax is 7% on the items that you
would still need to pay tax on.

Task:
Determine the total cost once you include tax of 7% on the items that are still taxed.

Input Format:
A string of numbers, separated by commas, that represent to price of each item that you are going to buy.

Output Format:
A number, rounded to two decimal places, of the total for your purchase once tax is included on items under 20 dollars.

Sample Input:
5,18,25,34

Sample Output:
83.61
'''
total = 0
imposto = 0
linha = input("").split(",")
for i in linha:
    valor=int(i)
    total+=valor
    if(valor<20):
        imposto+=valor
print("{:0.2f}".format(total+imposto*.07))

