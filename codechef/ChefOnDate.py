vezes = int(input(""))
if vezes > 6 or vezes < 1:
    exit(1)
for i in range(vezes):
    a = int(input(""))
    if a==6:
        print('YES')
    else:
        print('NO')
