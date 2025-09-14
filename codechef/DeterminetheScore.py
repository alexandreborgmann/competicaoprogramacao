vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    (x, n) = map(int, input("").split())
    print(int(x/10*n))