t = int(input())
if t<1 or t>10:
    exit(1)
for i in range(t):
    n = int(input(""))
    lista = []
    for i in range(n):
        lista.append(int(input("")))
    for i in lista:
        if lista.count(i)%2 !=0:
            print(i)
            break

