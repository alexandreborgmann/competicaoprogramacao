vezes = int(input(""))
if vezes > 10 or vezes < 1:
    exit(1)
for i in range(vezes):
    temperatura = int(input(""))
    if temperatura > 98:
        print('YES')
    else:
        print('NO')