t = int(input())
if t<1 or t>10**4:
    exit(1)
for i in range(t):
    x = int(input(""))
    if x<67 or x>45000:
        print('NO')
    else:
        print('YES')
