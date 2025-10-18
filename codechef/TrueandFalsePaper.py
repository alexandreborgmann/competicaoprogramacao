vezes = int(input(""))
if vezes > 2000 and vezes < 1:
    exit(1)
for z in range(vezes):
    n, k = map(int,input("").split())
    print(n-k)