vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    x1, y1, x2, y2 = map(int, input("").split())
    v1 = x1 + y1
    v2 = x2 + y2
    if v1 < v2:
        print(v1)
    else:
        print(v2)