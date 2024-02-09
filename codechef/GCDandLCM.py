vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
for z in range(vezes):
    x, y, k = map(int, input("").split())
    gcd = min(x,y)
    lcd = min(x,y)
    #print(x,y)
    while k:
        for j in range(2,max(x,y)+1):
            if x%j == 0 and y%j == 0 and j>gcd:
               gcd = j
            if x%j == 0 and y%j == 0 and (j<lcd or lcd ==-1):
                lcd = j
            if x<y:
                x = gcd
            else:
                y = gcd
            if x > y:
                x = lcd
            else:
                y = lcd
            print('j=',j,'x=',x,'y=',y,'gcd=',gcd,'lcd=',lcd,'k=',k)
        k -= 1
    print(x+y)