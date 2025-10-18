'''
You're given an integer N. Write a program to calculate the sum of all the digits of N.

Input Format
The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.

Output Format
For each test case, calculate the sum of digits of N, and display it in a new line.

Constraints
1
≤
T
≤
1000
1≤T≤1000
1
≤
N
≤
1000000
1≤N≤1000000
'''
t = int(input())
for _ in range(t):
    n = input()
    soma = 0
    for i in n:
        soma += int(i)
    print(soma)
