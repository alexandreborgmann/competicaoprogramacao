t = int(input())
if t<1 or t>100:
    exit(1)
for i in range(t):
    a = int(input(""))
    if a>100:
        print(a-10)
    else:
        print(a)