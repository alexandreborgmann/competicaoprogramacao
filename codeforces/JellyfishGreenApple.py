vezes = int(input(""))
if vezes<1 or vezes>10**40:
    exit(1)
for i in range(vezes):
    maca, pessoas = map(int, input("").split())
    passo = 0
    operacao = 0
    while maca!=0 and passo<1001:
        if (maca >= pessoas):
                maca = maca % pessoas
        else:
            operacao += maca
            maca *= 2
        #print(maca,pessoas,passo)
        passo += 1
    if maca != 0:
        print(-1)
    else:
        print(operacao)
