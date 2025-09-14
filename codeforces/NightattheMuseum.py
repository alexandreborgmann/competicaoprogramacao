palavra = input("")
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
passos = 0
posicaoAtual = 0
for i in range(len(palavra)):
    letra=palavra[i]
    achou=0
    j=posicaoAtual
    passosHorario=0
    #sentido horario
    while achou==0:
        if letra == alfabeto[j]:
            posicaoAchouHorario=j
            achou=1
            break
        if j==len(alfabeto)-1:
            j=0
        else:
            j=j+1
        passosHorario=passosHorario+1
        #print('horario',letra,alfabeto[j],j,passosHorario)
    achou=0
    j=posicaoAtual
    passosAnti=0
    #sentido anti-horario
    while achou==0:
        if letra == alfabeto[j]:
            posicaoAchouAnti=j
            achou=1
            break
        if j==0:
            j=len(alfabeto)-1
        else:
            j=j-1
        passosAnti=passosAnti+1
        #print('anti-horario', letra, alfabeto[j], j, passosAnti)
    posicaoAtual=posicaoAchouHorario
    if passosAnti<passosHorario:
        passos=passos+passosAnti
    else:
        passos=passos+passosHorario
    #print(letra,posicaoAtual,passosAnti,passosHorario,passos)
print(passos)