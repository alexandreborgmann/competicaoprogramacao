vezes = int(input(""))
if vezes > 100000 or vezes < 1:
    exit(1)
anterior=''
grupo=0
for i in range(vezes):
    domino = input("")
    if domino[1]!=anterior:
        anterior = domino[1]
        grupo += 1
print(grupo)
