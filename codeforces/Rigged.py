vezes = int(input(""))
if vezes<1 or vezes>100:
    exit(1)
for x in range(vezes):
    atletas = int(input(""))
    forca = [0]*atletas
    resistencia = [0]*atletas
    for i in range(atletas):
        forca[i], resistencia[i] = map(int, input("").split())
    maiorValor = -1
    for i in range(1,atletas):
        if forca[0] <= forca[i] and resistencia[0] <= resistencia[i]:
            maiorValor = -1
            break
        if resistencia[0]<=resistencia[i] and forca[0]>=forca[i]:
            if maiorValor<forca[i]+1:
                maiorValor = forca[i]+1
    print(maiorValor)