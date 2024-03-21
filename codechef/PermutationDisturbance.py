    vezes = int(input(""))
    if vezes > 10**4 and vezes < 1:
        exit(1)
    for z in range(vezes):
        n = int(input(""))
        p = list(map(int, input("").split()))
        trocou = 0
        for i in range(len(p)):
            #print('inicio i', i,'p[i]',p[i], 'p', p)
            if i == len(p)-1:
                desloca = -1
            else:
                desloca = 1
            if p[i] == i+1:
                aux = p[i]
                p[i] = p[i+desloca]
                p[i+desloca] = aux
                trocou += 1
            #print('fim i', i,'p[i]',p[i], 'p', p)
        print(trocou)

