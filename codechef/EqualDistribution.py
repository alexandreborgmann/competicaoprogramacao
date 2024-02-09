vezes = int(input(""))
if vezes > 1000 or vezes < 1:
    exit(1)
for i in range(vezes):
    a, b = map(int, input("").split())
    if (a+b)%2 == 0:
        print('YES')
    else:
        print('NO')