vezes = int(input(""))
if vezes > 100 or vezes < 1:
    exit(1)
for i in range(vezes):
    g, b = map(int, input("").split())
    print(b-g)