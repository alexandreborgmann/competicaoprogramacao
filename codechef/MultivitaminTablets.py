vezes = int(input(""))
if vezes > 2000 or vezes < 1:
    exit(1)
for i in range(vezes):
    dias, comprimidos = map(int, input("").split())

    if comprimidos >= dias * 3:
        print('YES')
    else:
        print('NO')
