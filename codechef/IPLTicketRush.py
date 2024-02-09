vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    x, y = map(int, input("").split())
    resultado = x - y
    if resultado < 0:
        resultado = 0
    print(resultado)
