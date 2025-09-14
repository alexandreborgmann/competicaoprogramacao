vezes = int(input(""))
if vezes > 6840 or vezes < 1:
    exit(1)
for i in range(vezes):
    lista = list(map(int, input("").split()))
    lista.sort()
    print(lista[1])