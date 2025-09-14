w = int(input(""))
if w<1 or w>100:
    exit(1)
multiplode2=0
for i in range(2,w):
    if i*2==w:
        multiplode2=1
        break
if multiplode2==1:
    print('YES')
else:
    print('NO')
