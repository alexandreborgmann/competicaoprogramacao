vezes = int(input(""))
if vezes > 10**4 or vezes < 1:
    exit(1)
for i in range(vezes):
    linha = input("")
    partes = linha.split()
    a = float(partes[0])
    b = float(partes[1])
    passos = 0
    while True:
        if a<b or passos==5:
           print('entrei',b-a)
           exit(0)
        print('a=',a,'b=',b,passos,'resto=',a%b)
        if a%b == 0:
            print(passos)
            break
        a = a + 1
        passos = passos +1


