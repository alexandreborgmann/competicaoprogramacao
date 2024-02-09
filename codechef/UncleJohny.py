t = int(input())
if t<1 or t>1000:
    exit(1)
for i in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    k = int(input(""))-1
    valor = a[k]
    a.sort()
    print(a.index(valor)+1)
