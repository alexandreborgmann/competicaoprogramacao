n = int(input(""))
if n<2 or n>100:
    exit(1)
lista = map(int, input("").split())
maior = max(lista)
menor = min(lista)
while maior