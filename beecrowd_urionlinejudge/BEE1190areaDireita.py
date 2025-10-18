acao = input("")
if acao not in ('S','M'):
    exit(1)
tamanho = 12
matriz = [0]*tamanho
soma = 0
conta = 0
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        valor = float(input(""))
        #valor = j
        linha.append(valor)
        if j > (tamanho-i)-1 and j>i:
            soma += valor
            conta += 1
    matriz.append(linha)
#print(matriz)
media = soma / conta
if acao == 'S':
    print('{:.1f}'.format(soma))
else:
    print("{:.1f}".format(media))