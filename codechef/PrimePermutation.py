t = int(input())
if t<1 or t>1000:
    exit(1)
for i in range(t):
    x=int(input(""))
    print('achando x=',x)
    for j in range(1,x):
        n=x-j

        print('n',n,'x=',x,'j=',j)
        mult = 0
        for count in range(2, n):
            if (n % count == 0):
                mult += 1
                print(count, end=" ")
        if mult==0:
            print(-1)
    print()