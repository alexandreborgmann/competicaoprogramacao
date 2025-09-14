vezes = int(input(""))
if vezes > 100 or vezes < 1:
    exit(1)
for i in range(vezes):
    moedas = list(map(int, input("").split()))
    total = sum(moedas)/2
    gemeo = 0
    qtdMoedas = 0
    while gemeo<=total:
        if len(moedas)>0:
            maior = max(moedas)
            gemeo += maior
            moedas.remove(maior)
            qtdMoedas += 1
        #print(qtdMoedas,maior,'gemeo=',gemeo,moedas )
    print(qtdMoedas)
