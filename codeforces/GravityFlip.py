n = int(input(""))
lista = list(map(int, input("").split()))
lista.sort()
for i in range(len(lista)):
    print(lista[i],end=' ')
