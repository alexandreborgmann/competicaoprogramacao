vezes = int(input(""))
if vezes<1 or vezes>1000:
    exit(1)
for x in range(vezes):
    s = input("")
    trocou=0
    fezTroca=1
    while fezTroca==1:
        fezTroca=0
        for i in range(0,len(s)):
            if s[i:i+2]=='AB':
                s = s[0:i]+'BC'+s[i+2:]
                trocou += 1
                fezTroca = 1
            if s[i:i+2]=='BA':
                s = s[0:i]+'CB'+s[i+2:]
                trocou += 1
                fezTroca = 1
        #print(s,s[i:i+2],i,trocou)
    print(trocou)
