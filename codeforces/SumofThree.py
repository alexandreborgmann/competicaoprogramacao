vezes = int(input(""))
if vezes>10**4 or vezes<1:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    i = 0
    achou = 0
    while i<n and achou == 0:
        if i%3!=0:
            j = 0
            while j<n and achou == 0:
                if j % 3 != 0:
                    k = 0
                    while k < n and achou == 0:
                         if k % 3 != 0:
                            if i+j+k == n and i!=j and i!=k and j!=k:
                                print('YES')
                                print(i,j,k)
                                achou = 1
                         k += 1
                         #print('i=', i, 'j=', j, 'k=', k, 'n=', n)
                j += 1
        i += 1

    if achou == 0:
        print('NO')


