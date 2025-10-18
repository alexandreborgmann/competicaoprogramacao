vezes = int(input(""))
if vezes > 2*(10**5) and vezes <= 1:
    exit(1)
for i in range(vezes):
    x = int(input(""))
    a = x
    b = x
    achoua = False
    achoub = False
    while True:
        if ((a&b) % x) == 0 and (a&b) != 0:
            achoua = True
        if not achoua:
            a += x
        if (a^b) % x == 0 and (a^b) != 0:
            achoub = True
        if not achoub:
            b += x
        #print('a=',a,'b=',b,achoua,achoub,a&b, a^b, x)
        if (achoua and achoub) or b>100:
            break
    print(a,b)