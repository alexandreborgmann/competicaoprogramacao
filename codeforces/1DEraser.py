vezes = int(input(""))
if vezes<1 or vezes>1000:
    exit(1)
for x in range(vezes):
    n, k = map(int,input("").split())
    s = input("")
    l = list(s)
    trocou=0
    for i in range(n):
        if l[i] == 'B':
            for j in range(i,min(i+k,n)):
                l[j]='W'
            i +=k-1
            trocou+=1
    print(trocou)
'''
    i=0
    while i<len(s) and i!=-1:
        i=s.find('B')
        if i!=-1:
            s=s[0:i]+'W'*k+s[i+k:]
            trocou+=1
            #print(i,s,trocou)
    print(trocou)
'''
