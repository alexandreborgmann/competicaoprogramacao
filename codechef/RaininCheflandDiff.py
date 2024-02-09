t = int(input())
if t<1 or t>20:
    exit(1)
for i in range(t):
    chuva = int(input(""))
    if chuva<3:
        print('LIGHT')
    elif chuva>=3 and chuva<7:
        print('MODERATE')
    elif chuva>=7:
        print('HEAVY')