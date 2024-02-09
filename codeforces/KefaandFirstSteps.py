vezes = int(input(""))
if vezes<1 or vezes>10**5:
    exit(1)
a = list(map(int, input("").split()))
maior = 1
conta = 1
anterior = a[0]
for i in range(1,len(a)):
    if anterior<=a[i]:
        conta +=1
    else:
        conta = 1
    anterior = a[i]
    if conta > maior:
        maior = conta
    #print('i=',i,'conta=',conta,'maior=',maior,'anterior=',anterior,)
print(maior)



