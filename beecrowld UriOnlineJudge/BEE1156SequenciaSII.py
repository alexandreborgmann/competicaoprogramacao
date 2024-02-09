s = 1
i = 3
j = 2
while i < 39:
    s += i/j
    i += 2
    j *= 2
print('{:.2f}'.format(s))