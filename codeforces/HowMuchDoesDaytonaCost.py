vezes = int(input(""))
if vezes<1 or vezes>1000:
    exit(1)
for i in range(vezes):
    n, k = map(int,input("").split())
    a = list(map(int,input("").split()))
    if a.count(k):
        print('YES')
    else:
        print('NO')