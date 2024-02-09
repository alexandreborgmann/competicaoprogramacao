lista = list(map(int, input("").split()))
dict = {}
for i in range(len(lista)):
    if lista.count(lista[i])>1:
        if lista[i] not in dict:
            dict[lista[i]] = lista.count(lista[i])
soma = 0
for i in dict.values():
    soma += i-1
print(soma)