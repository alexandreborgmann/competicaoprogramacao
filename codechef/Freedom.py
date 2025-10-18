vezes = int(input(""))
if vezes > 10 ** 3 and vezes < 1:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    lista = list(map(int, input("").split()))
    soma = 0
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            a = lista[i] - lista[j]
            b = lista[i] + lista[j]
            c = lista[i] * lista[j]
            if (3*(a+c))/2 == a+b+c:
                soma +=1
            #print(i,j,soma,lista,a,b,c)
    print(soma)

