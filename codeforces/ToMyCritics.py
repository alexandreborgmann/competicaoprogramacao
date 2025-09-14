vezes = int(input(""))
if vezes > 1000 or vezes < 1:
    exit(1)
for i in range(vezes):
    lista = list(map(int, input("").split()))
    i=0
    achou=0
    while achou==0 and i<len(lista)-1:
        j=i+1
        while achou==0 and j<len(lista):
            #print(i,j,lista[i],lista[j])
            if lista[i]+lista[j]>=10:
                achou=1
            j=j+1
        i=i+1
    if achou==1:
        print('YES')
    else:
        print('NO')