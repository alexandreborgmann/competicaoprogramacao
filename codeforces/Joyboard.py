vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for x in range(vezes):
    nslots, mmaior, kdiferente = map(int, input("").split())