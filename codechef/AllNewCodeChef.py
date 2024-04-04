x, y = map(int, input("").split())
if x > y:
    print('New')
elif y > x:
    print('Old')
else:
    print('Same')