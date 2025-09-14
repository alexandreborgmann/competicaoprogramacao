vezes = int(input(""))
if vezes>100 or vezes<1:
    exit(1)
for x in range(vezes):
    n = int(input(""))
    listaValores = list(map(int, input("").split()))
    valorIgual = 0
    i = 0
    while valorIgual==0 and i<len(listaValores)-1:
        if listaValores[i]==listaValores[i+1]:
            valorIgual = listaValores[i]
        i = i + 1
    if valorIgual==0 and len(listaValores)==3:
        valorIgual = listaValores[0]
    for i in range(len(listaValores)):
        if listaValores[i] != valorIgual:
            print(i+1)
            break

