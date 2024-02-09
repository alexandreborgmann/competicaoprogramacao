vezes = int(input(""))
if vezes>1000 or vezes<1:
    exit(1)
matriz=[0]*vezes
resposta=0
for i in range(vezes):
    matriz[i]= list(map(int,input("").split()))
for l in range(len(matriz)):
    vaiResolver=0
    for c in range(len(matriz[0])):
        #print('l=', l, 'c=', c,'matriz[l][c]=',matriz[l][c])
        if matriz[l][c]==1:
            vaiResolver=vaiResolver+1
    if vaiResolver>1:
        resposta=resposta+1
print(resposta)
