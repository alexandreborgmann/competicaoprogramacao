vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    lista = list(map(int, input("").split()))
    print(max(lista)-min(lista))