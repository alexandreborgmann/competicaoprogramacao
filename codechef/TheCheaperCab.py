vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    (x, y) = map(int, input("").split())
    if x < y:
        print('FIRST')
    elif y < x:
        print('SECOND')
    else:
        print('ANY')