t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if b > a and b > c:
        print(b)
    elif a > b and a > c:
        print(a)
    else:
        print(c)
