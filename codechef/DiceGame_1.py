vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    print(int(n/2*6*2 + n/2))