def verificaResultado(listaf: list) -> int:
    vezes=listaf[0]
    for i in range(1,len(listaf)):
        vezes = vezes * listaf[i]
    return(vezes)
n=int(input(""))
lista = list(map(int,input("").split()))
for i in range(len(lista)):
    listat = lista.copy()
    resultadoAnterior=verificaResultado(listat)
    operacoes=0
    while verificaResultado(listat)!=0 and verificaResultado(listat)>=resultadoAnterior and operacoes<10:
        resultadoAnterior = verificaResultado(listat)
        listat[i]=listat[i]-1
        operacoes = operacoes + 1
        #print('negativo','i',i,operacoes,listat,verificaResultado(listat),'resultadoanterior=',resultadoAnterior)
    if verificaResultado(listat)==0:
        print(operacoes)
        break
    listat = lista.copy()
    resultadoAnterior=verificaResultado(listat)
    operacoes=0
    while verificaResultado(listat)!=0 and verificaResultado(listat)>=resultadoAnterior and operacoes<10:
        resultadoAnterior = verificaResultado(listat)
        listat[i]=listat[i]+1
        operacoes = operacoes + 1
        #print('positivo',operacoes,'i',i,listat,verificaResultado(listat),'resultadoanterior=',resultadoAnterior)
    if verificaResultado(listat)==0:
        print(operacoes)
        break
    #print(verificaResultado(listat))
