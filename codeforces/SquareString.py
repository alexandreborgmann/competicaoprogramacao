vezes = int(input(""))
if vezes>100 or vezes<1:
    exit(1)
for i in range(vezes):
    palavra = input("")
    meio=int(len(palavra)/2)
    #print('palavra',palavra,' -->',palavra[0:meio],palavra[meio:],meio)
    if palavra[0:meio]==palavra[meio:] and len(palavra)%2==0:
        print('YES')
    else:
        print('NO')