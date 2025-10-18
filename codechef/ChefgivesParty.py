vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    n, x, k = map(int, input("").split())

    if n * x <= k:
        print('YES')
    else:
        print('NO')