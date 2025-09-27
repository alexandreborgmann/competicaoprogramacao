'''
Chef and Chocolates
Chef has
X
X 5 rupee coins and
Y
Y 10 rupee coins. Chef goes to a shop to buy chocolates for Chefina where each chocolate costs
Z
Z rupees. Find the maximum number of chocolates that Chef can buy for Chefina.

Input Format
The first line contains a single integer
T
T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains three integers
X
X,
Y
Y and
Z
Z — the number of 5 rupee coins, the number of 10 rupee coins and the cost of each chocolate.
Output Format
For each test case, output the maximum number of chocolates that Chef can buy for Chefina.

Constraints
1
≤
T
≤
100
1≤T≤100
1
≤
X
,
Y
,
Z
≤
1000
1≤X,Y,Z≤1000
'''
t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    x = x * 5
    y = y * 10
    v = int((x + y) / z)
    print(v)
