ano = int(input(""))
if ano<1000 or ano>9000:
    exit(1)
achouUnico = i = j = 0
while achouUnico != 1:
    ano = ano + 1
    strano = str(ano)
    numeroDuplo = 0
    i = 0
    while i < len(strano) and numeroDuplo!=1:
        numeroDuplo = 0
        j=0
        while j < len(strano) and numeroDuplo!=1:
            #print( i, j, '[i]=',strano[i],' [j]=',strano[j], len(strano), achouUnico, ano)
            if strano[i] == strano[j] and i != j:
                #print('entrei',i, j, strano[i], strano[j], len(strano), achouUnico, ano)
                numeroDuplo = 1
            j = j + 1
        i = i + 1
    if (i == len(strano) and j == len(strano) and i==j) :
        achouUnico = 1
print(ano)