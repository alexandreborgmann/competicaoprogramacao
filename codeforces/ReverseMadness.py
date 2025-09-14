vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for i in range(vezes):
    tamanhoString, tamanholr = map(int, input("").split())
    s = list(input(""))
    listal = list(map(int,input("").split()))
    listar = list(map(int, input("").split()))
    modifica = int(input(""))
    listax = list(map(int, input("").split()))
    for i in range(len(listax)):
        if i>=len(listal) and i>=len(listar):
            continue
        if listax[i]>=listal[i] and listax[i]<=listar[i]:
            a=min(listax[i],listar[i]+listal[i]-listax[i])-1
            b=max(listax[i],listar[i]+listal[i]-listax[i])-1
#            print(a,b,s)
            aux = s[a]
            s[a] = s[b]
            s[b] = aux
    s1 = ''.join(str(e) for e in s)
    print(s1)