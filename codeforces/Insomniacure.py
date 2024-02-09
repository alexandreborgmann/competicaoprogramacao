k = int(input(""))
l = int(input(""))
m = int(input(""))
n = int(input(""))
qtd = int(input(""))

lista = [0]*(qtd+1)
lista[0] = 0
if k<=qtd:
    for i in range(1,qtd+1, k):
        lista[i] = 1
if l<=qtd:
    for i in range(1,qtd+1, l):
        lista[i] = 1
if m<=qtd:
    for i in range(1, qtd+1, m):
        lista[i] = 1
if n<=qtd:
    for i in range(1, qtd+1, n):
        lista[i] = 1
#print(lista)
print(lista.count(1))