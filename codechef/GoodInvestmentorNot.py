vezes = int(input(""))
if vezes > 400 and vezes < 1:
    exit(1)
for z in range(vezes):
    x, y = map(int, input("").split())
    if x >= y*2:
        print('YES')
    else:
        print('NO')