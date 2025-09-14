vezes = int(input(""))
if vezes<1 or vezes>10**5:
    exit(1)
for x in range(vezes):
    resultado = list(map(int, input("").split()))
