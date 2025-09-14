a, b = map(int, input("").split())
c = (a-b)
if c%10 == 9:
	c -= 1
else:
	c += 1
print(c)


