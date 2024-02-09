vezes = int(input(""))
if vezes>1000 or vezes<1:
    exit(1)
for i in range(vezes):
    a = int(input(""))
    print(a*15)