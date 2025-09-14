t = int(input())
if  t<1 or t>100:
    exit(1)
for i in range(t):
    (n, x, y) = map(int, input().split())
    if x+(y*2)<=n:
        print('YES')
    else:
        print('NO')