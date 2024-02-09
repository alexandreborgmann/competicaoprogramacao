vezes = int(input(""))
if vezes<0 or vezes>1000:
    exit(1)
for j in range(vezes):
    valor = int(input(""))
    if valor%2==0:
        print(0)
    else:
        print(1)