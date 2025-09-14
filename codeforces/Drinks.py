tamanho = int(input(""))
lista = list(map(int, input("").split()))
percentual=0
for i in range(len(lista)):
    percentual += lista[i]
print(percentual/tamanho)
