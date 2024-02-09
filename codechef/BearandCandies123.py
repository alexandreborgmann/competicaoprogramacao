vezes = int(input(""))
if vezes > 10**4 and vezes < 1:
    exit(1)
for i in range(vezes):
    eatLimak, eatBob = map(int,input("").split())
    somaLimak = 1
    somaBob = 2
    comeuLimak = 0
    comeuBob = 0
    while True:
        comeuLimak += somaLimak
        comeuBob +=somaBob
        if comeuLimak>eatLimak:
            print('Bob')
            break
        if comeuBob>eatBob:
            print('Limak')
            break
        somaLimak +=2
        somaBob +=2
#        print(somaLimak,somaBob)
