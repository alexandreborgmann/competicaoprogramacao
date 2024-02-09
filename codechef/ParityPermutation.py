vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
for i in range(vezes):
    n, k = map(int,input("").split())
    a = list(map(int,input("").split()))
    muda = 0
    for i in range(n-1):
        for j in range(i+1,len(a)):
            if (i+j)%2!=0:
                if (a[i]+a[j]) % 2 == k:
                    muda += 1
            print('i=',i,'j=',j,'i+j=',i+j,(i+j)%2,a[i],a[j],a[i]+a[j],'a[i]+a[j] % 2=',(a[i]+a[j]) % 2,'muda=',muda)
    print(muda)
