a, b, c, d = map(int, input("").split())
ok = 0
if a/b == c/d:
    ok = 1
elif a/c == b/d:
    ok = 1
elif  a/d == b/c:
    ok = 1

if ok == 1:
    print('Possible')
else:
    print('Impossible')