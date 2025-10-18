def gcd(a : int, b : int) -> int:
    #print('a=',a, 'b=',b,)
    if b == 0:
        return a
    else:
        #print('a%b=', a % b)
        return gcd(b, a%b)

vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
for z in range(vezes):
    x, y, k = map(int, input("").split())

    g = gcd(x, y)
    if k <= 1:
        print(g+min(x,y))
    else:
        print(2*g)
