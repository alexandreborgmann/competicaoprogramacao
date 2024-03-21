vezes = int(input(""))
if vezes > 3*10**5 and vezes < 1:
    exit(1)
for z in range(vezes):
    days = int(input(""))
    vendas = list(map(int, input("").split()))
    soma = 0
    soma_vendas = []
    for i in range(len(vendas)):
        soma_vendas.append(soma+vendas[i]*2)
        soma += vendas[i]
    #print(vendas,soma_vendas)
    maior = 0
    for i in range(len(soma_vendas)):
        if soma_vendas[i] > maior:
            maior = soma_vendas[i]
    print(maior)
