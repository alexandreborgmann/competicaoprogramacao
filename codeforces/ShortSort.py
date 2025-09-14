vezes = int(input(""))
if vezes>6 or vezes<1:
    exit(1)
listaOrdenada = ['a','b','c']
for j in range(1,vezes+1):
    lista = list(map(str,input("")))
    if lista == listaOrdenada:
        print('YES')
    else:
        achou=0
        i=0
        while i<len(lista)-1 and achou==0:
            z=i+1
            while z<len(lista) and achou==0:
                listanova = lista.copy()
                listanova[i] = lista[z]
                listanova[z] = lista[i]
                #print('listanova=',listanova,'lista=',lista,i,z,'j=',j)
                if listanova == listaOrdenada:
                    achou=1
                z=z+1
            i=i+1
        #print(listanova,lista,j)
        if achou==1:
            print('YES')
        else:
            print('NO')