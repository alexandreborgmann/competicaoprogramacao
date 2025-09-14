vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    linha = input("")
    partes = linha.split()
    x = float(partes[0])
    y = float(partes[1])
    if (x<1 and x>6) or (y<1 and y>6):
        exit(1)
    if x+y>6:
        print('YES')
    else:
        print('NO')