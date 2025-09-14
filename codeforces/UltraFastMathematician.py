s = input("")
if len(s)>100:
    exit(1)
z = input("")
if len(z)>100:
    exit(1)
r = ''
for i in range(len(s)):
    if s[i] != z[i]:
        r= r + '1'
    else:
        r = r + '0'
print(r)