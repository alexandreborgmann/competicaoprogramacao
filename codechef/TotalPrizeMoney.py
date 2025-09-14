vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    (x, y) = map(int, input("").split())
    print(x*10+90*y)