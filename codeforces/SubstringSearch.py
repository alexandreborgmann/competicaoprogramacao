frase = input("")
vezes = int(input(""))
if vezes>300 or vezes<1:
    exit(1)
for i in range(vezes):
    palavra = input("")
    tamanho = len(palavra)
    achou = 0
    for j in range(len(frase)-(tamanho-1)):
        #print('frase=',frase[j:j+tamanho],'j',j,tamanho,'palavra',palavra)
        if frase[j:j+tamanho]==palavra:
            achou=1
            break
    if achou==1:
        print('Yes')
    else:
        print('No')
