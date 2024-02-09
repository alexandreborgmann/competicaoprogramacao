import math

while True:
    try:
        a, b, percentual = map(int,input("").split())
        m = (a * b * 100) / percentual
        print(int(math.sqrt(m)))
    except:
        break
