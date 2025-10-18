while True:
    n = int(input(""))
    if n == 0:
        exit(0)
    for i in range(1,n+1):
        print(i,sep='',end='')
        if i!=n:
            print(' ',end='')
        else:
            print("")