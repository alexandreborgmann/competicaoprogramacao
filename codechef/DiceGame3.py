vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    soma = 0
    anterior = 0
    dados = [0]*n
    for i in range(n):
        if i % 2 == 0:
            dados[i] = 1
        else:
            dados[i] = 6
#    print(dados)
    for i in range(n):
        if anterior == 1:
            soma += dados[i]*2
        else:
            soma += dados[i]
        anterior = dados[i]
 #       print(anterior,soma,i,dados[i])
    print(soma)