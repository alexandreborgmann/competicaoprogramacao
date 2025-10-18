t = int(input())
if t<1 or t>1000:
    exit(1)
for i in range(t):
    a, b, c = map(int, input("").split())
    if a>b and a>c:
        print('Alice')
    elif b>a and b>c:
        print('Bob')
    elif c>a and c>b:
        print('Charlie')