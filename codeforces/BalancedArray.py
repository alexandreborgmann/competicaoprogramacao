vezes = int(input(""))
if vezes > 10**4 or vezes < 1:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    meio = int(n/2)
    if (n/2)%2 !=0:
        print('NO')
    else:
        print('YES')
        par = 2
        for i in range(meio):
            print(par,end=' ')
            par += 2
        par -= 2
        impar = 1
        for i in range(meio-1):
            print(impar, end=' ')
            impar += 2
        print(par+meio-1)