t = int(input())
if t<1 or t>100:
    exit(1)
for i in range(t):
    (a, b) = map(int, input().split())
    print(abs(a-b))
