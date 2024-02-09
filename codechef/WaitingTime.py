t = int(input())
if t<1 or t>500:
    exit(1)
for i in range(t):
    (k, x) = map(int, input().split())
    print(k*7-x)
