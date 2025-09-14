n= int(input(""))
if n>1439 or n<1:
    exit(1)

for i in range(n):
    (hora, minuto) = map(int, input("").split())
    print(1440-(hora*60+minuto))