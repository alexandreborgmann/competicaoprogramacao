matriz=[[0 for _ in range(12)] for _ in range(12)]
for i in range(12):
    matriz.append([])
linha = int(input(""))
if linha<0 or linha>11:
    exit(1)
operacao = input("")
for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input(""))
soma = 0
for i in range(12):
    soma += matriz[linha][i]
if operacao == 'S':
    print(soma)
else:
    print(soma/12)

