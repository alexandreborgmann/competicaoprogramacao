t = int(input())
if t<1 or t>20:
    exit(1)
for i in range(t):
    x = int(input(""))
    if x < 7:
        print('YES')
    else:
        print('NO')