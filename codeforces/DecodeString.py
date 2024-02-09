numero = int(input(""))
if numero>100 or numero<1:
    exit(1)
if numero%2==0:
    print('YES')
else:
    print('NO')