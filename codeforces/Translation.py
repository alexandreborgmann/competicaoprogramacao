a = input("")
b = input("")
i = len(b)-1
c = ""
while i>=0:
    c=c+(b[i])
    i = i -1

if a==c:
    print('YES')
else:
    print('NO')

