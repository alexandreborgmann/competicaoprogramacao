acao = input("")
if acao not in ('S','M'):
    exit(1)
matriz = [0]*12
soma = 0
conta = 0
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input(""))
        #valor = j
        linha.append(valor)
        if j>i:
            soma += valor
            conta += 1
    matriz.append(linha)
#print(matriz)
media = soma / conta
if acao == 'S':
    print('{:.1f}'.format(soma))
else:
    print("{:.1f}".format(media))