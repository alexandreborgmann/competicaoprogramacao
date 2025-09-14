vezes = int(input(""))
for i in range(vezes):
    linha = input("")
    partes = linha.split()
    a = int(partes[0])
    b = int(partes[1])
    c = int(partes[2])
    if a+b==c or a+c==b or b+c==a:
        print('YES')
    else:
        print('NO')