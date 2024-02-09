i = input("")
s = list(i)
perigoso=0
conta=1
anterior=s[0]
for i in range(len(s)):
    if s[i]!=anterior:
        anterior=s[i]
        conta=1
    else:
        conta=conta+1
        if conta==7:
            perigoso=1
            break
    #print(i,s[i],conta,perigoso)
if perigoso==1:
    print('YES')
else:
    print('NO')
