vezes = int(input(""))
if vezes<1 or vezes>200:
    exit(1)
for i in range(vezes):
    velocidade = int(input(""))
    if velocidade<=70:
        print(0)
    elif velocidade>70 and velocidade<=100:
        print(500)
    else:
        print(2000)
