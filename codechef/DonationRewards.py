vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    x = int(input(""))
    if x <= 3:
        print('BRONZE')
    elif x > 3 and x <=6:
        print('SILVER')
    else:
        print('GOLD')