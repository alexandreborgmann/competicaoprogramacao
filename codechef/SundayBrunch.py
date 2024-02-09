vezes = int(input(""))
if vezes > 405 and vezes < 1:
    exit(1)
for i in range(vezes):
    x, y = map(int, input("").split())
    r = int(x/y)
    print(min(20,r))

