import math

carros = int(input(""))
passageiros = list(map(int,input("").split()))
portas = list(map(int,input("").split()))
permitidoCarro=math.ceil(sum(passageiros)/carros)
#print('inicio',permitidoCarro,passageiros)
trocas=0
i = 0
while max(passageiros)>permitidoCarro and i<len(passageiros):
    if passageiros[i]>permitidoCarro and portas[i]>0:
        for i
    while passageiros[menorindice]<permitidoCarro and max(passageiros)>permitidoCarro and i<len(passageiros):
        if portas[i]-menorindice>0 and passageiros[i]>permitidoCarro:
            adiciona=permitidoCarro-passageiros[menorindice]
            passageiros[menorindice]=passageiros[menorindice]+adiciona
            passageiros[i]=passageiros[i]-adiciona
            trocas=trocas+1
            #print('i',i,'menorindice',menorindice,'adiciona=',adiciona,passageiros[i],passageiros[menorindice],passageiros)
        i=i+1
#print('final',passageiros)
print(trocas)

