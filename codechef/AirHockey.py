vezes = int(input(""))
if vezes > 50 and vezes < 1:
    exit(1)
for i in range(vezes):
    a, b = map(int,input("").split())
    print(7-max(a,b))