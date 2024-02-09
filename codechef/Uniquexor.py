vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for z in range(vezes):
    tamanho, k = map(int, input("").split())
    s = input("")
    lista = [int(val) for val in s]
    conta = 0
    if lista.count(0)==tamanho or lista.count(1)==tamanho:
        print(0)
        continue
    print(lista)
    print(lista.count(0))

'''
    terminou = 0
    i = 0
    while i<tamanho and terminou==0:
        j = i+1
        while j<tamanho and terminou==0:
            if i!=j and (i+1)%k==(j+1)%k:
                r = lista[i] ^ lista[j]
                lista[i] = r
                lista[j] = r
                conta += 1
#                if lista.count(0)==tamanho or lista.count(1)==tamanho:
#                    terminou = 1
                #print('entrei','i=',i,'j=',j,lista,'conta=',conta,r,'k=',k,'tamanho=',tamanho)
            #print('i=',i,'j=',j,lista,'conta=',conta,r,'k=',k,'tamanho=',tamanho)
            j += 1
        i += 1
    print(conta)
'''