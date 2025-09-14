import math

vezes = int(input(""))
if vezes > 1000 or vezes < 1:
    exit(1)
lista = []
for i in range(vezes):
    tamanho, total = map(int, input("").split())
    if total<tamanho:
        print(-1)
        continue
    if total % tamanho == 0:
        par = total // tamanho - 2
        impar = total // tamanho - 1
    else:
        impar = math.ceil(total / tamanho)
        par = impar - 1
    resultado = []
    print(par,impar,total % tamanho, total // tamanho)
    for j in range(tamanho):
        if j%2 == 0:
            resultado.append(par)
        else:
            resultado.append(impar)
    if sum(resultado)==total:
        print(resultado)
    else:
        print(-1)