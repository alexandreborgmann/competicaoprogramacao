t = int(input())
if t<1 or t>10**4:
    exit(1)
for z in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    if a[0] != a[-1]:
        print('NO')
    else:
        c = a[0]
        f = True
        for i in range(n):
            if c > a[i]:
                print('NO')
                f = False
                break
        if f:
            print('YES')

