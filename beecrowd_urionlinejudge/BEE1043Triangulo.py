a, b, c = map(float, input("").split())
if (a+b)>c and (b+c)>a and (c+a)>b:
    perimetro =  a + b + c
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = .5 * (a+b) * c
    print("Area = {:.1f}".format(area))