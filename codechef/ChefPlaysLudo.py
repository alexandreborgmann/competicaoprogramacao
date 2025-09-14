vezes = int(input(""))
if vezes > 100 or vezes < 1:
    exit(1)
for i in range(vezes):
    x, y = map(int, input("").split())
    if x>=y:
        print('YES')
    else:
        print('NO')
