vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for z in range(vezes):
    n, m = map(int, input("").split())
    x = input("")
    s = input("")
    achou = -1
    letraDiferente = 0
    if x.find(s) != -1:
        print(0)
        continue
    for i in range(len(s)):
        #print('x=', x, 'i=', i, 's[i]=', s[i])
        if x.find(s[i]) == -1:
            letraDiferente = 1
            break
    if letraDiferente == 0:
        for i in range(1,len(s)+1):
            x = x*2
            achou = x.find(s)
            #print('x=',x,'i=',i,'achou=',achou)
            if achou != -1:
                break
    if achou != -1:
        print(i)
    else:
        print(-1)