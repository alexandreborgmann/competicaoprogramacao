vezes = int(input(""))
if vezes<1 or vezes>10**3:
    exit(1)
for i in range(vezes):
    palavra = input("")
    if palavra.upper()=='YES':
        print("YES")
    else:
        print('NO')
