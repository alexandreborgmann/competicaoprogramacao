a, b = map(int,input("").split())
for r in range(abs(b)):
    q = int((-(a) + r)/-(b))
    if a == (b * q + r):
        print(q, r)
        exit(0)