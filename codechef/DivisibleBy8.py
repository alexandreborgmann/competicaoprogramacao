vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    n, m = map(int, input("").split())
    while m%8!=0:
        m +=1
    print(m)


