vezes = int(input(""))
if vezes > 100 or vezes < 1:
    exit(1)
a = 0
b = 0
c = 0
for i in range(vezes):
    x, y, z = map(int, input("").split())
    a += x
    b += y
    c += z
if a==0 and b==0 and c==0:
    print('YES')
else:
    print('NO')