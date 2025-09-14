vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    lista = [0]*n
    if n%2 == 0:
        lista[0] = 1
        lista[n-1] =1
    else:
        meio = int(n / 2)
        lista[meio] = 1

    for i in range(n):
        print(lista[i],end='')
    print('')