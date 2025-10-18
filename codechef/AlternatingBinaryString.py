t = int(input())
if t<1 or t>10**5:
    exit(1)
for z in range(t):
    n = int(input(""))
    s = list(input(""))
    print(n,s)
    if n == 1:
        print(0)
    else:
        trocou = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                trocou += 1
                for j in range(i,len(s)):
                    if s[j] == '0':
                        s[j] = '1'
                    else:
                        s[j] = '0'

            print(trocou,s)
        print(trocou)