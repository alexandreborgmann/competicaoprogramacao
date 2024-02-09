vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    pessoas, dinheiro = map(int, input("").split())
    fila = list(map(int, input("").split()))
    retirou = ''
    for j in range(len(fila)):
        if fila[j]<=dinheiro:
            dinheiro = dinheiro - fila[j]
            retirou=retirou+'1'
        else:
            retirou=retirou+'0'
    print(retirou)
