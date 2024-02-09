n, h = map(int, input("").split())
lista = list(map(int, input("").split()))
l=0
for i in range(len(lista)):
    if lista[i]<=h:
        l = l + 1
    else:
        l = l + 2
print(l)