vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    linha = input("")
    partes = linha.split()
    inicio = int(partes[0])
    fim = int(partes[1])
    idade = int(partes[2])
    if idade>=inicio and idade<fim:
        print('YES')
    else:
        print('NO')