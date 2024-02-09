t = int(input())
if t<1 or t>100:
    exit(1)
for i in range(t):
    x = int(input(""))
    if x<=30:
        print('NO')
    else:
        print('YES')