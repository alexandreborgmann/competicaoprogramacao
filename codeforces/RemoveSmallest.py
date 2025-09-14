vezes = int(input(""))
if vezes>1000 or vezes<1:
    exit(1)
for x in range(vezes):
    n = int(input(""))
    a = list(map(int, input("").split()))
    ok = 1
    if len(a) == 1:
        print('YES')
        continue
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(a[i]-a[j])>1:
                ok = 0
                break
            #print('i=',i,'j=',j,'a[i]=',a[i],'a[j]=',a[j],'ok=',ok,'abs(a[i]-a[j])=',abs(a[i]-a[j]))
    if ok == 1:
        print('YES')
    else:
        print('NO')




