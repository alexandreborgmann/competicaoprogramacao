'''
2
2 1
3 2
'''

def chef(a, b):
    l = [1, 2, a]
    m = [2 * a, (2 * a - 1), a + 1]
    if b in l:
        c = l.index(b)
        print(m[c])
    else:
        if b in m:
            d = m.index(b)
            print(l[d])

t = int(input())
if 1 <= t <= 1000:
    for i in range(t):
        (a, b) = map(int, input().split())
        chef(a, b)
