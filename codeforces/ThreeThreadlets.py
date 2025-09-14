vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for z in range(vezes):
    lista = list(map(int, input("").split()))
    if lista[0]==lista[1] and lista[1]==lista[2]:
        print('YES')
        continue
    minimo = min(lista)
    if (lista[0]%minimo!=0 or lista[1]%minimo!=0 or lista[2]%minimo!=0):
        print('NO')
    elif (lista[0]/minimo>3 or lista[1]/minimo>3 or lista[2]/minimo>3) and \
        lista[0] > minimo ** 3 or lista[1] > minimo ** 3 or lista[2] > minimo ** 3:
        print('NO')
    else:
        print('YES')
print(1**3)


