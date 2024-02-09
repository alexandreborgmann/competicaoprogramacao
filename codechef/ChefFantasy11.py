vezes = int(input(""))
if vezes > 10 and vezes < 1:
    exit(1)
for z in range(vezes):
    n = int(input())
    print(n*(n-1))