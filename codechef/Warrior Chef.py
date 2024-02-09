vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)

for i in range(vezes):
    ninimigos, forca = map(int,input("").split())
    forcainimigos = list(map(int,input("").split()))
    i=0
    resistencia = 0
    forcan=-1
    while forcan<0:
        forcan=forca
        i=0
        while i<len(forcainimigos):
            if i + 1 > resistencia:
                forcan = forcan - forcainimigos[i]
                if forcan<0:
                    resistencia +=1
                    break
            #print('i=',i,'forcan=',forcan,'forcainimigos[i]=',forcainimigos[i],'resistencia=',resistencia)
            i=i+1
    print(resistencia)
