vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    length, width, custo = map(int, input("").split())
    print((length*2+width*2)*custo)
