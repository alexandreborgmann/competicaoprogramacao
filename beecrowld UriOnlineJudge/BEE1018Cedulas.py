dinheiro = int(input(""))
if dinheiro<0 or dinheiro>1000000:
    exit(1)
valorNotas = [ 100, 50, 20, 10, 5, 2, 1]
nroNotas = [0]*len(valorNotas)
print(dinheiro)
for i in range(len(valorNotas)):
    if dinheiro>=valorNotas[i]:
        qtdNotas = dinheiro//valorNotas[i]
        nroNotas[i] = qtdNotas
        dinheiro -= valorNotas[i] * qtdNotas
for i in range(len(nroNotas)):
    print("{} nota(s) de R$ {:.2f}".format(nroNotas[i],valorNotas[i]).replace('.',','))
