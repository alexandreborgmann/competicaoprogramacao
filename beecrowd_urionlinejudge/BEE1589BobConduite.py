vezes = int(input(""))
if vezes > 100000 or vezes < 1:
    exit(1)
for z in range(vezes):
    r1, r2 = map(int, input("").split())
    print(r1+r2)
