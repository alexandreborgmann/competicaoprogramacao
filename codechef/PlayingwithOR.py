vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
for z in range(vezes):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    conta = 0
    for i in range(n - k + 1):
        sa = a[i:i + k]
        bor = 0
        for v in sa:
            bor |= v
        if bor % 2 !=0:
            conta += 1
    print(conta)


