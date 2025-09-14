a,b = map(int, input("").split())
if a<1 or a>10 or b<1 or b>10:
    exit(1)
ano=0
while a<=b:
    a=a*3
    b=b*2
    ano=ano+1
#    print(a,b,ano)
print(ano)

