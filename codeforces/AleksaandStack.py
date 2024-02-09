vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    k = 3
    for i in range(n+1,1,-1):
        print(k,' ',end='')
        k +=2
    print('')

