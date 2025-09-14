vezes = int(input(""))
if vezes > 10**4 and vezes < 1:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    b = list(map(int,input("").split()))
    achou3 = 0
    for i in range(len(b)):
        if b.count(b[i])>=3:
            achou3 = 1
            break
    if achou3 == 1:
        print('No')
    else:
        print('Yes')
