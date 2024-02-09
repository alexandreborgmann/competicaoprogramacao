lista = [0]*100
for i in range(100):
    lista[i] = int(input(""))
maior = max(lista)
print(maior)
print(lista.index(maior)+1)
