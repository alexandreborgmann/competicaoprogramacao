lista = list(map(int, input("").split()))
listaOriginal = lista.copy()
lista.sort()
for i in range(len(lista)):
    print(lista[i])
print()
for i in range(len(lista)):
    print(listaOriginal[i])
