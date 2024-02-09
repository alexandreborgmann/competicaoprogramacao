n, k = map(int, input("").split())
meio = int(n/2)
if n%2==1:
    meio+=1

if k<=meio:
    print(2*k-1)
else:
    print((k-meio)*2)


'''
forca bruto da problema de memoria
pares = []
impares =[]
for i in range(1,n+1):
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)
#print(impares,pares)
k=k-1
if k<len(impares):
    print(impares[k])
else:
    k=k-len(impares)
    print(pares[k])
'''
