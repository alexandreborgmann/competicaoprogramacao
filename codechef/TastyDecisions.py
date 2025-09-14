t = int(input())
if t<1 or t>100:
    exit(1)
for i in range(t):
    chocolate, candy = map(int, input("").split())
    chocolate *=2
    candy *=5
    if chocolate>candy:
        print('Chocolate')
    elif candy>chocolate:
        print('Candy')
    else:
        print('Either')
