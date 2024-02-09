vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for x in range(vezes):
    n = int(input(""))
    lista = list(map(int,input("").split()))
    maiorMultipla=0
    for i in range(len(lista)):
        multiplica=1
        for j in range(len(lista)):
            if i==j:
                multiplica*=lista[j]+1
            else:
                multiplica*=lista[j]
        if maiorMultipla<multiplica:
            maiorMultipla=multiplica
    print(maiorMultipla)
