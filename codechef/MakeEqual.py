t = int(input())
if t<1 or t>10**4:
    exit(1)
for z in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    mudou = 1
    #print('inicio=',n,a)
    while mudou and len(set(a))>1:
        mudou = 0
        i = 1
        while mudou==0 and i < len(a)-1:
            if a[i] >= a[i-1] and a[i] >= a[i+1]:
                a[i] -= 1
                mudou = 1
            i +=1
        #print(a)
    if len(set(a)) > 1:
        print('NO')
    else:
        print('YES')
