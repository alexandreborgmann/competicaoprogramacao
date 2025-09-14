vezes = int(input(""))
if vezes>100 or vezes<1:
    exit(1)
for i in range(vezes):
    valor = int(input(""))
    soma=2050
    if soma>valor:
        print(-1)
    else:
        passos = 1
        while soma<valor:
            soma=soma+2050
            passos=passos+1
        if passos==0:
            print(-1)
        else:
            print(passos)

        print('i',i,passos,soma,'valor=',valor,)
        print(2050**1,2050*10,2050*10**2,2050*10**3)