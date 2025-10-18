def  triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

a, b, c, d = map(int, input("").split())
if triangulo(a,b,c) or triangulo(a,b,d) or triangulo(a,c,d) or triangulo(b,c,d):
    print('S')
else:
    print('N')