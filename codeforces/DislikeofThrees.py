vezes = int(input(""))
if vezes<1 or vezes>100:
    exit(1)
for i in range(vezes):
    k = int(input(""))
    i = 0
    j = 0
    while i<k:
        j += 1
        #print('l[-1]',l[-1],'i=',i,'j=',j)
        if j%3!=0 and j%10 != 3:
            i += 1
    print(j)