a, b, c = map(int, input("").split())
if a == b + c or a == b - c:
    print('S')
elif b == a + c or b == a - c:
    print('S')
elif c == a + b or c == a - b:
    print('S')
elif a==b or a==c or b==c:
    print('S')
else:
    print('N')