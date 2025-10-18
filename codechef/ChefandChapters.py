vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    x, y, z = map(int, input("").split())
    r = x*y*z
    print(r)