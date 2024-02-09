vezes = int(input(""))
if vezes > 200 and vezes < 1:
    exit(1)
for i in range(vezes):
    dias, proteinas = map(int, input("").split())
    diasCafe = list(map(int, input("").split()))
    sobra = 0
    suficiente = 1
    for i in range(dias):
        #print('i=',i,'diasCafe[i]=',diasCafe[i],sobra,proteinas,)
        if diasCafe[i] > proteinas:
            sobra += diasCafe[i]-proteinas
        else:
            if diasCafe[i] + sobra<proteinas:
                print('NO ',i+1)
                suficiente = 0
                break
            else:
                sobra =sobra-(proteinas-diasCafe[i])

    if suficiente:
        print('YES')

