'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Multiples

You need to calculate the sum of all the multiples of 3 or 5 below a given number.

Task:
Given an integer number, output the sum of all the multiples of 3 and 5 below that number.
If a number is a multiple of both, 3 and 5, it should appear in the sum only once.

Input Format:
An integer.

Output Format:
An integer, representing the sum of all the multiples of 3 and 5 below the given input.

Sample Input:
10

Sample Output:
23
'''
soma=0
numero = int(input(""))
for i in range(numero):
    if(i%3==0 or i%5==0):
        soma+=i
print(soma)
