vezes = int(input(""))
if vezes > 36000 and vezes < 1:
    exit(1)
for i in range(vezes):
    a,b,c,d,e=map(int,input().split())
    if(a+b<=d) and (c<=e):
        print("YES")
    elif(b+c<=d) and (a<=e):
        print("YES")
    elif(a+c<=d) and (b<=e):
        print("YES")
    else:
        print("NO")