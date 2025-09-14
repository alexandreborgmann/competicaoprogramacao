vezes = int(input(""))
lista = list(map(int,input("").split()))
listaNova = lista.copy()
for j in range(len(lista)):
    listaNova[lista[j]-1]=j+1
for j in range(len(listaNova)):
    print(listaNova[j],end=' ')
