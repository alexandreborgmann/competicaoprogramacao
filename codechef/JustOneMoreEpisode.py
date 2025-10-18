t = int(input())
if t<1 or t>100:
    exit(1)
for i in range(t):
    a = int(input(""))
    if a<=24:
        print('NO')
    else:
        print('YES')
