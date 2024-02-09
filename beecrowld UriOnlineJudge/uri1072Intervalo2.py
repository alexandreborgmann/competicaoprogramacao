'''
Author: Alexandre Borgmann
Date: 4/2/2020
URI Online Judge | 1072 Interval 2

Read an integer N. This value will be the amount of integer X values that will be read next.
Show how many of these X values are in the range [10.20] and how many are out of the range, showing this information.
Input
The first line of the entry contains an integer value N (N <10000), which indicates the number of test cases.
Each test case below is an integer value X (-107 <X <107).

Output
For each case, print how many numbers are in (in) and how many values are out (out) of the range.

Input Example / Output Example
4
14
123
10
-25
2 in
2 out
'''

ValIn=0;
ValOut=0;
ValoresLidos = []
while True:
    QuantidadeLer = int(input())
    if(QuantidadeLer<=10000):
        break
    print('Only Values <10000')

for i in range(QuantidadeLer):
    ValoresLidos.append(int(input()))
    if(ValoresLidos[i]>=10 and ValoresLidos[i]<=20):
        ValIn+=1
    else:
        ValOut+=1
print(ValIn,'in')
print(ValOut,'out')
