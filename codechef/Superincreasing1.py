t = int(input())
if t<1 or t>10**5:
    exit(1)
for i in range(t):
    n, k, x = map(int, input().split())
    sum_val = 2**(k-1) - 1
    if x > sum_val:
        print('YES')
    else:
        print('NO')