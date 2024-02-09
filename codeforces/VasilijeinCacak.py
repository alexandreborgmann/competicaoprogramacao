vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for i in range(vezes):
    n, diferentek, somax = map(int,input("").split())
    lista = []
    for i in range(n):
        lista.append(i+1)
    achou = 0
    for i in range(0,n,diferentek):
        print('i=',i,lista[i:i+diferentek])
        if sum(lista[i:i+diferentek]) == somax:
            achou = 1
            break
    if achou == 1:
        print('YES')
    else:
        print('NO')
