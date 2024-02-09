vezes = int(input(""))
if vezes > 10**4 or vezes < 1:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    if n % 2 != 0:
        print((n - 1) // 2)
    else:
        print((n // 2) - 1)
