vezes = int(input(""))
if vezes<1 or vezes>10**3:
    exit(1)
for i in range(vezes):
    letra = input("")
    if letra in "codeforces":
        print("YES")
    else:
        print('NO')