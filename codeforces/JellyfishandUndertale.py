vezes = int(input(""))
if vezes<1 or vezes>2000:
    exit(1)
for i in range(vezes):
    xTempo = []
    aMaxTempo, bInicioTempo, nFerramentas = map(int, input("").split())
    xTempo = list(map(int, input("").split()))
    tempoDecorrido = bInicioTempo
    for j in range(nFerramentas):
        tempoDecorrido += min(xTempo[j], aMaxTempo-1)
        #print(j,tempoDecorrido,xTempo[j])
    print(tempoDecorrido)