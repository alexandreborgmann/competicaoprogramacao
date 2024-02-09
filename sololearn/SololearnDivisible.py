'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Divisible

You need to know if a number is divisible by each of a group of other numbers.
If you are given the number and the group of other numbers, you will test to make sure that it is divisible by all of them.

Task:
Test your number against all of the other numbers that you are given to make sure that it is divisible by them.

Input Format:
Two inputs: an integer value (the number you are testing) and a string of variable length of the integers that you should
test against separated by spaces.

Output Format:
A string that says 'divisible by all' or 'not divisible by all'.

Sample Input:
100
2 5 10

Sample Output:
divisible by all
'''
numero=int(input(""))
linha=input("")
divisores=linha.split()
for i in divisores:
    if(numero%int(i)!=0):
        print("not divisible by all")
        exit(0)
print("divisible by all")
