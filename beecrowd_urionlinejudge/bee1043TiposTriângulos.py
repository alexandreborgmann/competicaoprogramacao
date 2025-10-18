lista = list(map(float, input("").split()))
lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]

if a >= b+c:
    print('NAO FORMA TRIANGULO')
    exit(0)
if a*a == (b*b) + (c*c):
    print('TRIANGULO RETANGULO')
if a*a > (b*b) + (c*c):
    print('TRIANGULO OBTUSANGULO')
if a*a < (b*b) + (c*c):
    print('TRIANGULO ACUTANGULO')
if a==b and b==c:
    print('TRIANGULO EQUILATERO')
if (a==b or b==c or a==c) and not (a==b and b==c):
    print('TRIANGULO ISOSCELES')