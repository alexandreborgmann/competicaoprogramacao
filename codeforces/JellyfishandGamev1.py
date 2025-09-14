vezes = int(input(""))
if vezes<1 or vezes>2000:
    exit(1)
for i in range(vezes):
    appleGellyfish = []
    nJellyfish, nGellyfish, k = map(int, input("").split())
    if nJellyfish>50:
        exit(1)
    if nGellyfish>50:
        exit(1)
    if k<1 and k>10**9:
        exit(1)
    a = list(map(int, input("").split()))
    b = list(map(int, input("").split()))

    a.sort()
    b.sort()
    k -= 1
    if(b[-1] > a[0]):
        a[0], b[-1] = b[-1], a[0]
    a.sort()
    b.sort()
    if(k & 1):
        a[-1], b[0] = b[0], a[-1]
    print(sum(a))
