n,k = map(int,input("").split())
lista = list(map(int,input("").split()))
conta=0
for i in range(len(lista)):
    if lista[i]>=lista[k-1] and lista[i]>0:
        conta=conta+1
print(conta)
