'''
Author: Alexandre Borgmann
Date: 4/4/2020
URI Online Judge | 1144 Logical Sequence

Write a program that reads an integer value N.
N * 2 lines of output will be presented in the execution of the program, following the logic of the example below.
For values with more than 6 digits, all digits must be displayed.
Input
The input file contains a positive integer N (1 <N <1000).
Output
Print the output according to the example provided.

Entry example
5
Output Example
1 1 1
1 2 2
2 4 8
2 5 9
3 9 27
3 10 28
4 16 64
4 17 65
5 25 125
5 26 126
'''
while True:
    n = int(input())
    if(n<=1 or n>=1000):
        print("Value must be 1 < N < 1000")
        continue
    break

for i in range(1,n+1):
    for s in range(2):
        for j in range(1,4):
            print((i ** j)+ ( 0 if(j==1) else s),end="\n" if (j==3) else " ")