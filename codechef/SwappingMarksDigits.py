t = int(input())
if t<1 or t>10**4:
    exit(1)
for i in range(t):
    a,b  = map(str, input("").split())
    an = int(a)
    bn = int(b)
    ai = int(a[1] + a[0])
    bi = int(b[1] + b[0])
    #print('an=',an,'ai=',ai,'bn',bn,'bi',bi)
    if an > bn or ai > bn or an > bi or ai > bi:
        print('Yes')
    else:
        print('No')
