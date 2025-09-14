vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for x in range(vezes):
    residencia, anuncio = map(int, input("").split())
    maximoAnuncio = list(int, input("").split())
    custo = list(int, input("").split())