vezes = int(input(""))
if vezes<1 or vezes>1000:
    exit(1)
for z in range(vezes):
    hora, minuto = map(int, input("").split(":"))