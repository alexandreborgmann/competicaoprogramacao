t = int(input())
if t<1 or t>10**4:
    exit(1)
for i in range(t):
    a, b = map(int,input("").split())
    if a>b:
        print('A')
    else:
        print('B')