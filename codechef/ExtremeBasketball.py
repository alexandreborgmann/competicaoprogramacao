t = int(input())
if  t<1 or t>10**4:
    exit(1)
for i in range(t):
    a, b = map(int, input().split())
    d = (a - b)
    if d >= 10:
        print(0)
    else:
        print(int((12 - (a-b))/3))
