t = int(input())
if t<1 or t>100:
    exit(1)
for i in range(t):
    x, y = map(int,input("").split())
    if x * 5 >= y:
        print('YES')
    else:
        print('NO')