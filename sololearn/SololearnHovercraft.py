'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Hovercraft

You run a hovercraft factory.
Your factory makes ten hovercrafts in a month.
Given the number of customers you got that month, did you make a profit?
It costs you 2,000,000 to build a hovercraft, and you are selling them for 3,000,000.
You also pay 1,000,000 each month for insurance.

Task:
Determine whether or not you made a profit based on how many of the ten hovercrafts you were able to sell that month.

Input Format:
An integer that represents the sales that you made that month.

Output Format:
A string that says 'Profit', 'Loss', or 'Broke Even'.

Sample Input:
5

Sample Output:
Loss
'''
unidadeVendida = int(input(""))
custoFabricacao=10*2
lucro=1
seguro=1
custoTotal=custoFabricacao+seguro
venda=unidadeVendida*3

if(custoTotal>venda):
    print("Loss")
elif(custoTotal==venda):
    print("Broke Even")
else:
    print("Profit")

