valor = int(input(""))
if valor>10**9 or valor<1:
    exit(1)
dinheiro = [100, 20, 10, 5, 1]
nronotas = 0
for i in range(len(dinheiro)):
    if valor<dinheiro[i]:
        continue
    inteiro = valor // dinheiro[i]
    valor = valor - inteiro*dinheiro[i]
    nronotas = nronotas + inteiro
print(nronotas)

