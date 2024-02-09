vezes = int(input(""))
if vezes > 1000 or vezes < 1:
    exit(1)
lista = []
for i in range(vezes):
    dias = int(input(""))
    lista = list(map(int, input("").split()))
    menor=min(lista)
    if menor<0:
        print(sum(lista) + abs(menor))
    else:
        print(sum(lista) - menor)


