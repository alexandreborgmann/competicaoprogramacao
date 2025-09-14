vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    a, b = map(int, input("").split())
    print(a+b)