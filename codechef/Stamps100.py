t = int(input())
if t<1 or t>10**5:
    exit(1)
for i in range(t):
    n = int(input(""))
    x=input("")
    j=0
    r=""
    while j<len(x):
        if x[j:j+3]=='110' and j<=n-3:
            r=r+'100'
            j=j+3
        else:
            r=r+x[j]
            j=j+1
    print(r)

