t = int(input())
if t<1 or t>10:
    exit(1)
for i in range(t):
    x, y = map(int, input().split())
    print(x-y)