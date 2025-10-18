vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    x = int(input(""))
    if x*10 < 3000:
        print(3000)
    else:
        print(x*10)