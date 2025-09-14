n, t = map(int, input("").split())
s = list(input(""))
for i in range(t):
    j = 0
    while j<n-1:
        #print(i,'j=',j,s)
        if s[j] == 'B' and s[j+1] == 'G':
            s[j+1] = 'B'
            s[j] = 'G'
            j += 1
        j += 1

s1=''.join(s)
print(s1)
