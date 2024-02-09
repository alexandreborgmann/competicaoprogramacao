vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    a = list(map(int, input("").split()))
    b = list(map(int, input("").split()))