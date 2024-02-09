import math

a, b, c = map(float, input("").split())
try:
    x = b*b-(4*a*c)
    r1 = (-b + math.sqrt(x))/(2*a)
    r2 = (-b - math.sqrt(x))/(2*a)
except:
    print('Impossivel calcular')
    exit(0)
if r1==0:
    print('Impossivel calcular')
else:
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))