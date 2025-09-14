t = int(input())
if t<1 or t>10**5:
    exit(1)
for i in range(t):
    n = int(input(""))
    om = list(map(int, input("").split()))
    andy = list(map(int, input("").split()))
    somaOn = 0
    maiorOn = 0
    for i in range(len(om)):
        if om[i] == 0:
            somaOn = 0
        else:
            somaOn += 1
        if maiorOn<somaOn:
            maiorOn = somaOn
    somaAndy = 0
    maiorAndy = 0
    for i in range(len(andy)):
        if andy[i] == 0:
            somaAndy = 0
        else:
            somaAndy += 1
        if maiorAndy<somaAndy:
            maiorAndy = somaAndy
    if maiorOn > maiorAndy:
        print('On')
    elif maiorAndy > maiorOn:
        print('Andy')
    else:
        print('Draw')