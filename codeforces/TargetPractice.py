vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
matrizPontos = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
for x in range(vezes):
    lista = []
    pontos=0
    for i in range(10):
        lista.append(input(""))
        for j in range(len(lista[i])):
            if lista[i][j]=='X':
                pontos=pontos+matrizPontos[i][j]
                #print(i,j,pontos,matrizPontos[i][j])
    print(pontos)