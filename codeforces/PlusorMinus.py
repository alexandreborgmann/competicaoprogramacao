vezes = int(input(""))
if vezes>162 or vezes<1:
    exit(1)
for i in range(vezes):
    a, b, c = map(int, input("").split())
    if a + b == c:
        print('+')
    else:
        print('-')