t = int(input())
if t<1 or t>100:
    exit(1)
for i in range(t):
    a, b, c = map(int, input("").split())
    if a+b==c:
        print('YES')
    else:
        print('NO')