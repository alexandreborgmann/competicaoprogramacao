n= int(input(""))
if n>10**5 or n<1:
    exit(1)
naoatendido = 0
policia = 0
x = list(map(int,input("").split()))
for i in range(n):
    if x[i] != -1:
        policia = policia + x[i]
    else:
        if policia == 0:
            naoatendido = naoatendido + 1
        else:
            policia = policia - 1
print(naoatendido)
