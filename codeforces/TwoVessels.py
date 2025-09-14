import math
vezes = int(input(""))
if vezes > 1000 or vezes < 1:
    exit(1)
for i in range(vezes):
    a,b,copo = map(int, input("").split())
    if a==b:
        print(0)
    else:
        if a>b:
            maior=a
            menor=b
        else:
            maior=b
            menor=a
        servidas=0
        aumenta=0
        #print('inico aumenta=', aumenta, 'servidas=', servidas, 'menor', menor, 'maior', maior)
        while menor<maior and servidas<maior:
            diferenca=maior-menor
            if diferenca<copo:
                menor=menor+diferenca
            else:
                menor=menor+copo
                maior=maior-copo
            servidas=servidas+1
            #print('aumenta=',aumenta,'servidas=',servidas,'menor',menor,'maior',maior)
        print(servidas)