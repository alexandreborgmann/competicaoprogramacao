vezes = int(input(""))
if vezes > (10**4) and vezes <= 1:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    a = list(map(int, input("").split()))
    a.sort()
    mex = 0
    for i in range(len(a)):
        mex += abs(i - a[i])
    print(mex)