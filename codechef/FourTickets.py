t = int(input())
if t<1 or t>100:
    exit(1)
for i in range(t):
    x = int(input(""))
    if x*4>1000:
        print('NO')
    else:
        print('YES')