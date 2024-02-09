t = int(input())
if  t<1 or t>500:
    exit(1)
for i in range(t):
    (x, y) = map(int, input().split())
    if x>y:
        print('LOSS')
    elif x<y:
        print('PROFIT')
    else:
        print('NEUTRAL')