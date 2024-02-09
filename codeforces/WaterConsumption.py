vezes = int(input(""))
if vezes<1 or vezes>2000:
    exit(1)
for i in range(vezes):
    litros = int(input(""))
    if litros >= 2000:
        print('YES')
    else:
        print('NO')
