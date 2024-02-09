vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
for z in range(vezes):
    paes, x, d = map(int,input().split())
    print((int(paes/5/x)+d))