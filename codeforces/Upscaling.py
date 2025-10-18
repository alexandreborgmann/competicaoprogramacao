vezes = int(input(""))
if vezes<1 or vezes>1000:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    ms = ['##'],['##']
    mp = ['..'],['..']
    matriz = []
    print(matriz)
    for i in range(1,n+1):
        if i % 2 == 0:
           matriz.append(mp)
        else:
            matriz.append(ms)
    print(matriz)
    for i in range(n+1):
        print(i,matriz[i],end='')
    print('')