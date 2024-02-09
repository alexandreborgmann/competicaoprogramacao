vezes = int(input(""))
if vezes > 200 and vezes < 1:
    exit(1)
for i in range(vezes):
    (n, x) = map(int, input("").split())
    print(n-x)