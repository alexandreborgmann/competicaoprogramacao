'''
Author: Alexandre Borgmann
Date: 4/3/2020
URI Online Judge | 1099 Consecutive Odd Sum II

Read an integer value N which is the number of test cases that follows.
Each test case consists of two integers X and Y. You must present the sum of all odd numbers between X and Y.

Input
The first line of entry is an integer N which is the number of test cases that follows.
Each test case consists of a line containing two integers X and Y.

Output
Print the sum of all odd values between X and Y.

Entry example
7
4 5
13 10
6 4
3 3
3 5
3 4
3 8
Output Example
0
11
5
0
0
0
12
'''
n = int(input())
for i in range(n):
    linha = input("")
    campos = linha.split()

    x = int(campos[0])
    y = int(campos[1])
    SomaImpar = 0

    if(x>y):
        inicio=y+1
        fim=x
    else:
        inicio=x+1
        fim=y

    #print('{} {}'.format(inicio,fim))
    for j in range(inicio,fim):
        #print('j=',j)
        if(j%2!=0):
            SomaImpar+=j
    print(SomaImpar)


