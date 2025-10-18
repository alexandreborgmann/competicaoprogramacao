vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    if n==1 or n%2 == 0:
        print('YES')
    else:
        print('NO')