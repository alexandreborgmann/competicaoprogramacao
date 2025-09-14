t = int(input())
if  t<1 or t>1000:
    exit(1)
for i in range(t):
    (a, b, c, d) = map(int, input().split())
    x=a-b
    y=c-d
    if x+y<0:
        print('YES')
    else:
        print('NO')