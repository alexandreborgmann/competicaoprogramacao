vezes = int(input(""))
if vezes>100 or vezes<1:
    exit(1)
listaValores = list(map(int, input("").split()))
maior = max(listaValores)
soma = 0
for i in range(len(listaValores)):
    if maior!=listaValores[i]:
        soma = soma + (maior-listaValores[i])
print(soma)


