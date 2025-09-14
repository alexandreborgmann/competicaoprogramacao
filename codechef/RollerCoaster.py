t = int(input())
if t<1 or t>1000:
    exit(1)
for i in range(t):
    a, b = map(int,input("").split())
    if a>=b:
        print('YES')
    else:
        print('NO')
