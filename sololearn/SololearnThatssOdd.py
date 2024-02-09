'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn That's odd...

You want to take a list of numbers and find the sum of all of the even numbers in the list. Ignore any odd numbers.

Task:
Find the sum of all even integers in a list of numbers.

Input Format:
The first input denotes the length of the list (N). The next N lines contain the list elements as integers.

Output Format:
An integer that represents the sum of only the even numbers in the list.

Sample Input:
9
1
2
3
4
5
6
7
8
9

Sample Output:
20

'''
n = int(input(""))
somaPar = 0
for i in range(n):
    numero=int(input(""))
    if(numero%2==0):
        somaPar+=numero
print(somaPar)
