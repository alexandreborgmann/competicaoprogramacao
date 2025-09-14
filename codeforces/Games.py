vezes = int(input(""))
if vezes > 30 or vezes < 2:
    exit(1)
a = [0]*vezes
b = [0]*vezes
for i in range(vezes):
    a[i], b[i] = map(int, input("").split())
resultado = 0
for i in range(vezes):
    for j in range(i):
        #print('i=',i,'j=',j,'a[i]=',a[i],'a[j]=',a[j],'b[i]=',b[i],'b[j]=',b[j])
        if b[i] == a[j]:
            resultado += 1
        if a[i] == b[j]:
            resultado += 1
print(resultado)
