x = int(input(""))
numSorte = []
for i in range(1000):
    numstr = str(i)
    sorte = 1
    for j in numstr:
        if j!='4' and j!='7':
            sorte = 0
            break
    if sorte==1:
       numSorte.append(i)
sorte = 0
for i in range(len(numSorte)):
    if x%numSorte[i]==0:
        sorte = 1
if sorte==1:
    print('YES')
else:
    print('NO')
