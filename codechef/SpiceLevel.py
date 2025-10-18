vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    x = int(input(""))
    if x < 4:
        print('MILD')
    elif x >= 4 and x < 7:
        print('MEDIUM')
    else:
        print('HOT')

