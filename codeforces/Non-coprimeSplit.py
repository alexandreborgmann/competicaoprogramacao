import math

vezes = int(input(""))
if vezes > 500 or vezes < 1:
    exit(1)
for i in range(vezes):
    l, r = map(int, input("").split())
    achou=-1
    for i in range(1,r):
        for j in range(1,r):
            if i+j>l and i+j<r and achou==-1:
                for x in range(2,max(i,j)):
                    if i%x==0 and j%x==0:
                        achou=1
                        print(i,j)
                    #print('l',l,'r',r,'i',i,'j',j,'x=',x)
