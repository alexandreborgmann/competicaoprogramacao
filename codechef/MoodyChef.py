vezes = int(input(""))
if vezes > 2*(10**5) and vezes <= 1:
    exit(1)
for i in range(vezes):
    n, l, r = map(int, input("").split())
    lista = list(map(int, input("").split()))
    conta = 0
    menor = 0
    maior = 0
    for i in range(len(lista)):
        if lista[i]>=l and lista[i]<=r:
            conta += 1
        else:
            conta -= 1
        menor = min(conta,menor)
        maior = max(conta,maior)
    print(maior,menor)