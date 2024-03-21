vezes = int(input(""))
if vezes>100 or vezes<1:
    exit(1)
for i in range(vezes):
    a = input("")
    b = a[0:2]
    for i in range(3,len(a)-2,3):
        b= b + a[i]
        print(i, a[i])
    if len(a) > 2:
        b +=a[-2:]
    print(b)
