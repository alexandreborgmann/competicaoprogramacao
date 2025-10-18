dinheiro = float(input(""))
if dinheiro<0 or dinheiro>1000000:
    exit(1)
notas = [ 100, 50, 20, 10, 5, 2 ]
moedas = [ 1, 0.50, 0.25, 0.10, 0.05, 0.01 ]
nroNotas = [0]*len(notas)
nroMoedas = [0]*len(moedas)
for i in range(len(notas)):
    if dinheiro>=notas[i] and dinheiro>=2:
        qtdNotas = int(dinheiro)//notas[i]
        nroNotas[i] = qtdNotas
        dinheiro -= nroNotas[i] *  notas[i]
for i in range(len(moedas)):
    if dinheiro>=moedas[i]:
        qtdMoedas = dinheiro//moedas[i]
        nroMoedas[i] = qtdMoedas
        dinheiro -= nroMoedas[i] * moedas[i]
print('NOTAS:')
for i in range(len(nroNotas)):
    print("{} nota(s) de R$ {:.2f}".format(nroNotas[i],notas[i]))
print('MOEDAS:')
for i in range(len(nroMoedas)):
    print("{:.0f} moeda(s) de R$ {:.2f}".format(nroMoedas[i],moedas[i]))