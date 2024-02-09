a = list(map(int, input("").split()))
a.sort()
c = a[3]-a[0]
b = a[2]-c
a = a[3]-(b+c)
print('{} {} {}'.format(a,b,c))
