vezes = int(input(""))
if vezes > 10**4 or vezes < 1:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    lista = list(map(int,input("").split()))
    maior = 0
    for i in range(len(lista)-1):
        listaNova = lista.copy()
        listaMultiplica = []
        listaSomaAntes = []
        listaSomaAntes=lista[0:i+1]
        multiplica=1
        for j in range(i+1,len(lista)):
            listaMultiplica.append(lista[j])
            multiplica=multiplica*lista[j]
        somaTotal=sum(listaSomaAntes)+multiplica
        if somaTotal>maior:
            l=i+1
            r=j+1
            maior=somaTotal
        print('listaSomaAntes=',listaSomaAntes,'listamultiplica=',listaMultiplica,'i=',i,'j=',j,'maior=',maior,'l=',l,'r=',r)
