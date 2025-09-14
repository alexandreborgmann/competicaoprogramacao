vezes = int(input(""))
if vezes > 1000 or vezes < 1:
    exit(1)
for i in range(vezes):
    n, x = map(int, input("").split())
    if n<=2:
        print(1)
    else:
        andar=1
        andar=andar+((n-2)//x)
        if (n-2)%x!=0:
            andar=andar+1
        print(andar)
#    print(x,((n-2)//x))
