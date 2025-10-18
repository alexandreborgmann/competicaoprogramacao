vezes = int(input(""))
if vezes<1 or vezes>30:
    exit(1)
for z in range(1,vezes+1):
    n, m = map(int, input().split())
    fila = [i for i in range(1,n+1)]
    x = 0
    y = 1
    while len(fila)>1:
        if x >= len(fila):
            x = 0
        elif y == m:
            fila.pop(x)
            y = 1
        else:
            y += 1
            x += 1
        #print(x,y,fila)
    print('Case {}: {}'.format(z,fila[0]))



