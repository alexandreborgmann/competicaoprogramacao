gritou = 0
soma = 0
while True:
    linha = input("")
    if linha == 'caw caw':
        print(soma)
        gritou +=1
        soma = 0
        if gritou == 3:
            exit(0)
    else:
        if linha == '--*':
            soma += 1
        elif linha == "-*-":
            soma += 2
        elif linha == "-**":
            soma += 3
        elif linha == "*--":
            soma += 4
        elif linha == "*-*":
            soma += 5
        elif linha == "**-":
            soma += 6
        elif linha == "***":
            soma += 7;


