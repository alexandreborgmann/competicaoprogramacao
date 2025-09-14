vezes = int(input(""))
if vezes<1 or vezes>100:
    exit(1)
for i in range(vezes):
    linha = input("")
    partes = linha.split('+')
    a = int(partes[0])
    b = int(partes[1])
    print(a+b)