vezes = int(input(""))
if vezes > 10**4 or vezes < 1:
    exit(1)
for i in range(vezes):
    a, b, c, d = map(int, input("").split())
    frente = 0
    if b>a:
        frente +=1
    if c>a:
        frente += 1
    if d>a:
        frente += 1
    print(frente)
