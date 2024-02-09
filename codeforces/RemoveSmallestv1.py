vezes = int(input(""))
if vezes>1000 or vezes<1:
    exit(1)
for x in range(vezes):
    n = int(input(""))
    a = list(map(int, input("").split()))
    removeu = 1
    while len(a)>1 and removeu == 1:
        removeu = 0
        i = 0
        while i<len(a)-1:
            j=i + 1
            while j<len(a):
                print('i=', i, 'a[i]=', a[i], 'a[j]=', a[j], 'abs(a[i]-a[j])=', abs(a[i] - a[j]))
                if abs(a[i]-a[j])<=1:
                    removeu = 1
                    if a[i]<=a[j]:
                        a.pop(i)
                    else:
                        a.pop(j)
                else:
                    j += 1
                print('len(a)=', len(a), 'removeu=', removeu)
            i += 1
    if len(a) == 1:
        print('YES')
    else:
        print('NO')




