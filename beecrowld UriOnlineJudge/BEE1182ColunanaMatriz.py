matriz=[[0 for _ in range(12)] for _ in range(12)]
for i in range(12):
    matriz.append([])
coluna = int(input(""))
if coluna<0 or coluna>11:
    exit(1)
operacao = input("")
for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input(""))
soma = 0
for i in range(12):
    soma += matriz[i][coluna]
if operacao == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/12))