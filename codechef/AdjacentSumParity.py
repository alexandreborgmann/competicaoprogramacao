vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    b = list(map(int,input("").split()))