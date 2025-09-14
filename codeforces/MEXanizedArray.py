vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for x in range(vezes):
    n, m = map(int,input("").split())
    a = list(map(int,input("").split()))
    b = list(map(int,input("").split()))
    minimo=-1
    maximo=-1
    c=[]
    for i in range(len(b)):
        for j in range(len(a)):
            c.append(a[j]|b[i])
        soma=0
        print(c)
        for j in range(len(c)):
            soma=soma^c[j]
        if maximo==-1 or soma>maximo:
            maximo=soma
        if minimo==-1 or soma<=minimo:
            minimo=soma
    print(minimo,maximo)
