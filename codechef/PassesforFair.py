vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    n, k = map(int, input().split())
    if k>n:
        print('YES')
    else:
        print('NO')